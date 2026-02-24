#!/usr/bin/env python3
"""
PageSpeed Insights API — Otomatik Veri Toplayıcı
parlakbeton.com | Haftalık cron: Her Pazartesi 08:00

Kurulum:
  pip install requests

Çalıştırma:
  python pagespeed.py

Cron (lxc-db):
  0 8 * * 1 /usr/bin/python3 /opt/analytics/pagespeed.py
"""

import requests
import json
import os
from datetime import datetime

# Yapılandırma
URL = "https://parlakbeton.com"
API_KEY = os.environ.get("PAGESPEED_API_KEY", "")  # .env'den al
OUTPUT_DIR = "/opt/analytics/reports"

CATEGORIES = ["performance", "seo", "best-practices", "accessibility"]


def fetch_pagespeed(strategy: str) -> dict:
    """PageSpeed API'den veri çeker."""
    params = {
        "url": URL,
        "strategy": strategy,
        "category": CATEGORIES,
    }
    if API_KEY:
        params["key"] = API_KEY

    resp = requests.get(
        "https://www.googleapis.com/pagespeedonline/v5/runPagespeed",
        params=params,
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def extract_metrics(data: dict) -> dict:
    """API yanıtından temel metrikleri çıkarır."""
    cats = data.get("lighthouseResult", {}).get("categories", {})
    audits = data.get("lighthouseResult", {}).get("audits", {})

    return {
        "performance": round(cats.get("performance", {}).get("score", 0) * 100),
        "seo": round(cats.get("seo", {}).get("score", 0) * 100),
        "best_practices": round(cats.get("best-practices", {}).get("score", 0) * 100),
        "accessibility": round(cats.get("accessibility", {}).get("score", 0) * 100),
        "lcp": audits.get("largest-contentful-paint", {}).get("displayValue", "—"),
        "inp": audits.get("interaction-to-next-paint", {}).get("displayValue", "—"),
        "cls": audits.get("cumulative-layout-shift", {}).get("displayValue", "—"),
        "fcp": audits.get("first-contentful-paint", {}).get("displayValue", "—"),
        "ttfb": audits.get("server-response-time", {}).get("displayValue", "—"),
    }


def save_report(metrics_mobile: dict, metrics_desktop: dict):
    """Raporu markdown dosyasına kaydeder."""
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{today}-pagespeed.md")

    content = f"""# PageSpeed Raporu — {today}

## Mobil

| Metrik | Değer |
|--------|-------|
| Performance | {metrics_mobile['performance']} |
| SEO | {metrics_mobile['seo']} |
| Best Practices | {metrics_mobile['best_practices']} |
| Accessibility | {metrics_mobile['accessibility']} |
| LCP | {metrics_mobile['lcp']} |
| INP | {metrics_mobile['inp']} |
| CLS | {metrics_mobile['cls']} |
| FCP | {metrics_mobile['fcp']} |
| TTFB | {metrics_mobile['ttfb']} |

## Masaüstü

| Metrik | Değer |
|--------|-------|
| Performance | {metrics_desktop['performance']} |
| SEO | {metrics_desktop['seo']} |
| Best Practices | {metrics_desktop['best_practices']} |
| Accessibility | {metrics_desktop['accessibility']} |
| LCP | {metrics_desktop['lcp']} |
| CLS | {metrics_desktop['cls']} |
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Rapor kaydedildi: {filepath}")


def main():
    print(f"🔍 PageSpeed analiz başlıyor: {URL}")

    print("  → Mobil analiz...")
    mobile_data = fetch_pagespeed("mobile")
    mobile_metrics = extract_metrics(mobile_data)

    print("  → Masaüstü analiz...")
    desktop_data = fetch_pagespeed("desktop")
    desktop_metrics = extract_metrics(desktop_data)

    save_report(mobile_metrics, desktop_metrics)

    print(f"\n📊 Özet:")
    print(f"  Mobil Performance:  {mobile_metrics['performance']}")
    print(f"  Mobil SEO:          {mobile_metrics['seo']}")
    print(f"  Desktop Performance:{desktop_metrics['performance']}")


if __name__ == "__main__":
    main()
