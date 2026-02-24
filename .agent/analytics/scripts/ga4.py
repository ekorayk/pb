#!/usr/bin/env python3
"""
Google Analytics 4 API — Haftalık Veri Toplayıcı
parlakbeton.com

Kurulum:
  pip install google-analytics-data google-auth

Gereksinim:
  GA4 Property ID → analytics panelinden (Yönetici → Mülk Ayarları)
  Service account JSON → Google Cloud Console

Cron (lxc-db):
  0 9 * * 1 /usr/bin/python3 /opt/analytics/ga4.py
"""

import os
from datetime import datetime, timedelta
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest
)

# Yapılandırma
GA4_PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "")  # .env'den al
# Format: "properties/420811600" (Site Kit'ten alınan property_id)
CREDENTIALS_FILE = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
OUTPUT_DIR = "/opt/analytics/reports"


def fetch_overview(client, property_id: str, days: int = 28) -> dict:
    """Genel trafik metriklerini çeker."""
    end_date = "today"
    start_date = f"{days}daysAgo"

    request = RunReportRequest(
        property=property_id,
        dimensions=[Dimension(name="sessionDefaultChannelGroup")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="totalUsers"),
            Metric(name="newUsers"),
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
            Metric(name="conversions"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    return client.run_report(request)


def fetch_top_pages(client, property_id: str, days: int = 28):
    """En çok ziyaret edilen sayfaları çeker."""
    request = RunReportRequest(
        property=property_id,
        dimensions=[
            Dimension(name="pagePath"),
            Dimension(name="pageTitle"),
        ],
        metrics=[
            Metric(name="sessions"),
            Metric(name="totalUsers"),
            Metric(name="bounceRate"),
        ],
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="today")],
        limit=20,
    )
    return client.run_report(request)


def fetch_traffic_sources(client, property_id: str, days: int = 28):
    """Trafik kaynaklarını çeker."""
    request = RunReportRequest(
        property=property_id,
        dimensions=[Dimension(name="sessionSource")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="totalUsers"),
            Metric(name="conversions"),
        ],
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="today")],
        limit=10,
    )
    return client.run_report(request)


def save_report(overview, pages, sources):
    """Raporu markdown olarak kaydeder."""
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{today}-ga4.md")

    content = f"# GA4 Raporu — {today}\nVeri aralığı: Son 28 gün\n\n"

    # Kanal bazlı trafik
    content += "## Kanal Bazlı Trafik\n\n"
    content += "| Kanal | Oturum | Kullanıcı | Yeni Kullanıcı | Hemen Çıkma |\n"
    content += "|-------|--------|-----------|----------------|-------------|\n"
    for row in overview.rows:
        dims = [d.value for d in row.dimension_values]
        mets = [m.value for m in row.metric_values]
        content += f"| {dims[0]} | {mets[0]} | {mets[1]} | {mets[2]} | {round(float(mets[3])*100,1)}% |\n"

    # Trafik kaynakları
    content += "\n## Trafik Kaynakları\n\n"
    content += "| Kaynak | Oturum | Kullanıcı | Dönüşüm |\n"
    content += "|--------|--------|-----------|--------|\n"
    for row in sources.rows:
        dims = [d.value for d in row.dimension_values]
        mets = [m.value for m in row.metric_values]
        content += f"| {dims[0]} | {mets[0]} | {mets[1]} | {mets[2]} |\n"

    # En iyi sayfalar
    content += "\n## En Çok Ziyaret Edilen Sayfalar\n\n"
    content += "| Sayfa | Oturum | Kullanıcı |\n"
    content += "|-------|--------|----------|\n"
    for row in pages.rows:
        dims = [d.value for d in row.dimension_values]
        mets = [m.value for m in row.metric_values]
        content += f"| {dims[0]} | {mets[0]} | {mets[1]} |\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Rapor kaydedildi: {filepath}")


def main():
    print("🔍 GA4 veri çekimi başlıyor...")
    property_id = f"properties/{GA4_PROPERTY_ID}"
    client = BetaAnalyticsDataClient()

    overview = fetch_overview(client, property_id)
    pages = fetch_top_pages(client, property_id)
    sources = fetch_traffic_sources(client, property_id)

    save_report(overview, pages, sources)


if __name__ == "__main__":
    main()
