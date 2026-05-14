#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
CONFIG_FILE = ROOT / "config" / "market_watchlist.json"
OUTPUT_FILE = ROOT / "outputs" / "market_snapshot.json"
PORTAL_OUTPUT_FILE = PROJECT_ROOT / "研究门户" / "market-snapshot-data.js"

YAHOO_QUOTE_URL = "https://query1.finance.yahoo.com/v7/finance/quote"
YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart"
SINA_QUOTE_URL = "https://hq.sinajs.cn/list="
USER_AGENT = "Mozilla/5.0 BambooLens/1.0"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return fallback


def fetch_yahoo_quotes(symbols: list[str]) -> dict[str, dict[str, Any]]:
    if not symbols:
        return {}

    query = urllib.parse.urlencode({"symbols": ",".join(symbols)})
    request = urllib.request.Request(
        f"{YAHOO_QUOTE_URL}?{query}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        payload = json.loads(response.read().decode("utf-8"))

    results = payload.get("quoteResponse", {}).get("result", [])
    return {item.get("symbol"): item for item in results if item.get("symbol")}


def fetch_yahoo_chart_quote(symbol: str) -> dict[str, Any] | None:
    encoded_symbol = urllib.parse.quote(symbol, safe="")
    request = urllib.request.Request(
        f"{YAHOO_CHART_URL}/{encoded_symbol}?range=5d&interval=1d",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        payload = json.loads(response.read().decode("utf-8"))

    result = (payload.get("chart", {}).get("result") or [None])[0]
    if not result:
        return None

    meta = result.get("meta", {})
    price = number(meta.get("regularMarketPrice"))
    previous_close = number(meta.get("previousClose") or meta.get("chartPreviousClose"))
    change = None
    change_percent = None
    if price is not None and previous_close not in (None, 0):
        change = price - previous_close
        change_percent = change / previous_close * 100

    return {
        "symbol": symbol,
        "shortName": meta.get("shortName") or symbol,
        "longName": meta.get("longName") or symbol,
        "fullExchangeName": meta.get("fullExchangeName") or meta.get("exchangeName") or meta.get("exchange"),
        "exchange": meta.get("exchange"),
        "currency": meta.get("currency"),
        "regularMarketPrice": price,
        "regularMarketPreviousClose": previous_close,
        "regularMarketChange": change,
        "regularMarketChangePercent": change_percent,
        "regularMarketTime": meta.get("regularMarketTime"),
        "marketCap": meta.get("marketCap"),
    }


def fetch_yahoo_chart_quotes(symbols: list[str]) -> dict[str, dict[str, Any]]:
    quotes: dict[str, dict[str, Any]] = {}
    for symbol in symbols:
        try:
            quote = fetch_yahoo_chart_quote(symbol)
            if quote:
                quotes[symbol] = quote
            time.sleep(0.2)
        except Exception:
            continue
    return quotes


def cn_market_code(symbol: str) -> str | None:
    if symbol.endswith(".SZ"):
        return f"sz{symbol.split('.')[0]}"
    if symbol.endswith(".SS"):
        return f"sh{symbol.split('.')[0]}"
    return None


def fetch_sina_cn_quotes(symbols: list[str]) -> dict[str, dict[str, Any]]:
    code_map = {cn_market_code(symbol): symbol for symbol in symbols if cn_market_code(symbol)}
    code_map = {code: symbol for code, symbol in code_map.items() if code}
    if not code_map:
        return {}

    request = urllib.request.Request(
        SINA_QUOTE_URL + ",".join(code_map.keys()),
        headers={
            "User-Agent": USER_AGENT,
            "Referer": "https://finance.sina.com.cn/",
            "Accept": "*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        text = response.read().decode("gb18030", errors="ignore")

    quotes: dict[str, dict[str, Any]] = {}
    for line in text.splitlines():
        if '="' not in line:
            continue
        code = line.split("=", 1)[0].rsplit("_", 1)[-1]
        symbol = code_map.get(code)
        if not symbol:
            continue
        raw = line.split('="', 1)[1].rstrip('";')
        fields = raw.split(",")
        if len(fields) < 32 or not fields[0]:
            continue

        price = number(fields[3])
        previous_close = number(fields[2])
        change = None
        change_percent = None
        if price is not None and previous_close not in (None, 0):
            change = price - previous_close
            change_percent = change / previous_close * 100

        market_time = None
        try:
            market_dt = datetime.strptime(f"{fields[30]} {fields[31]}", "%Y-%m-%d %H:%M:%S")
            market_time = int(market_dt.replace(tzinfo=ZoneInfo("Asia/Shanghai")).timestamp())
        except Exception:
            market_time = None

        quotes[symbol] = {
            "symbol": symbol,
            "shortName": fields[0],
            "longName": fields[0],
            "fullExchangeName": "深圳证券交易所" if symbol.endswith(".SZ") else "上海证券交易所",
            "exchange": "SZSE" if symbol.endswith(".SZ") else "SSE",
            "currency": "CNY",
            "regularMarketPrice": price,
            "regularMarketPreviousClose": previous_close,
            "regularMarketChange": change,
            "regularMarketChangePercent": change_percent,
            "regularMarketTime": market_time,
            "marketCap": None,
        }

    return quotes


def number(value: Any) -> float | None:
    if value is None:
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(result) or math.isinf(result):
        return None
    return result


def format_price(value: float | None, currency: str | None) -> str:
    if value is None:
        return "暂无"
    prefix = {
        "USD": "US$",
        "HKD": "HK$",
        "TWD": "NT$",
        "CNY": "¥",
    }.get(currency or "", "")
    return f"{prefix}{value:,.2f}"


def format_percent(value: float | None) -> str:
    if value is None:
        return "暂无"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def format_compact_money(value: float | None, currency: str | None) -> str:
    if value is None:
        return "暂无"
    prefix = {
        "USD": "US$",
        "HKD": "HK$",
        "TWD": "NT$",
        "CNY": "¥",
    }.get(currency or "", "")
    abs_value = abs(value)
    if abs_value >= 1_000_000_000_000:
        return f"{prefix}{value / 1_000_000_000_000:.2f}T"
    if abs_value >= 1_000_000_000:
        return f"{prefix}{value / 1_000_000_000:.2f}B"
    if abs_value >= 1_000_000:
        return f"{prefix}{value / 1_000_000:.2f}M"
    return f"{prefix}{value:,.0f}"


def normalize_quote(symbol: str, quote: dict[str, Any]) -> dict[str, Any]:
    price = number(quote.get("regularMarketPrice"))
    previous_close = number(quote.get("regularMarketPreviousClose"))
    change = number(quote.get("regularMarketChange"))
    change_percent = number(quote.get("regularMarketChangePercent"))
    currency = quote.get("currency")
    market_cap = number(quote.get("marketCap"))
    market_time = quote.get("regularMarketTime")

    return {
        "symbol": symbol,
        "shortName": quote.get("shortName") or quote.get("longName") or symbol,
        "exchange": quote.get("fullExchangeName") or quote.get("exchange") or "",
        "currency": currency or "",
        "price": price,
        "previousClose": previous_close,
        "change": change,
        "changePercent": change_percent,
        "marketCap": market_cap,
        "marketTime": market_time,
        "display": {
            "price": format_price(price, currency),
            "changePercent": format_percent(change_percent),
            "marketCap": format_compact_money(market_cap, currency),
        },
    }


def build_payload() -> dict[str, Any]:
    config = load_json(CONFIG_FILE, {"companies": []})
    previous = load_json(OUTPUT_FILE, {"companies": {}})
    watchlist = config.get("companies", [])
    symbols = sorted({symbol for company in watchlist for symbol in company.get("symbols", [])})

    quotes: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []
    errors: list[str] = []
    try:
        quotes = fetch_yahoo_quotes(symbols)
    except Exception as exc:  # Keep the portal usable even if the quote source fails.
        warnings.append(f"Yahoo quote fetch failed, falling back to chart API: {exc}")
        quotes = fetch_yahoo_chart_quotes(symbols)

    if not quotes:
        chart_quotes = fetch_yahoo_chart_quotes(symbols)
        if chart_quotes:
            quotes = chart_quotes

    missing_cn_symbols = [
        symbol for symbol in symbols
        if symbol not in quotes and (symbol.endswith(".SZ") or symbol.endswith(".SS"))
    ]
    if missing_cn_symbols:
        try:
            quotes.update(fetch_sina_cn_quotes(missing_cn_symbols))
        except Exception as exc:
            errors.append(f"Sina CN quote fallback failed: {exc}")

    companies: dict[str, Any] = {}
    for company in watchlist:
        company_id = company["id"]
        company_symbols = company.get("symbols", [])
        normalized_quotes = [
            normalize_quote(symbol, quotes[symbol])
            for symbol in company_symbols
            if symbol in quotes
        ]

        if normalized_quotes:
            primary_symbol = company.get("primary_symbol") or company_symbols[0]
            primary = next((item for item in normalized_quotes if item["symbol"] == primary_symbol), normalized_quotes[0])
            companies[company_id] = {
                "id": company_id,
                "name": company.get("name", company_id),
                "primarySymbol": primary["symbol"],
                "primary": primary,
                "quotes": normalized_quotes,
                "updatedAt": utc_now_iso(),
                "source": YAHOO_QUOTE_URL,
                "stale": False,
            }
        else:
            stale_company = previous.get("companies", {}).get(company_id)
            if stale_company:
                stale_company = {**stale_company, "stale": True}
                companies[company_id] = stale_company
            else:
                companies[company_id] = {
                    "id": company_id,
                    "name": company.get("name", company_id),
                    "primarySymbol": company.get("primary_symbol") or (company_symbols[0] if company_symbols else ""),
                    "primary": None,
                    "quotes": [],
                    "updatedAt": "",
                    "source": YAHOO_QUOTE_URL,
                    "stale": True,
                }

    return {
        "generated_at": utc_now_iso(),
        "source": f"{YAHOO_QUOTE_URL} / {YAHOO_CHART_URL} / {SINA_QUOTE_URL}",
        "warnings": warnings,
        "errors": errors,
        "companies": companies,
    }


def main() -> None:
    payload = build_payload()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_OUTPUT_FILE.write_text(
        "window.BAMBOO_LENS_MARKET_SNAPSHOT = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Market snapshot written to: {OUTPUT_FILE}")
    print(f"Portal market snapshot written to: {PORTAL_OUTPUT_FILE}")
    if payload.get("warnings"):
        print("\n".join(payload["warnings"]))
    if payload.get("errors"):
        print("\n".join(payload["errors"]))


if __name__ == "__main__":
    main()
