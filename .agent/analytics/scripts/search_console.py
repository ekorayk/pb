#!/usr/bin/env python3
"""
Google Search Console API — Haftalık Veri Toplayıcı
parlakbeton.com

Kurulum:
  pip install google-auth google-auth-httplib2 google-api-python-client

Gereksinim:
  Google Cloud Console'da service account veya OAuth credentials
  → credentials.json dosyasını /opt/analytics/ altına koyun

Cron (lxc-db):
  0 9 * * 1 /usr/bin/python3 /opt/analytics/search_console.py
"""

import os
import json
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Yapılandırma
SITE_URL = "https://parlakbeton.com/"
CREDENTIALS_FILE = "/opt/analytics/credentials.json"
TOKEN_FILE = "/opt/analytics/token.json"
OUTPUT_DIR = "/opt/analytics/reports"

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

# İzlenecek anahtar kelimeler
TARGET_KEYWORDS = [
    "parlak beton",
    "beton parlatma",
    "beton parlatma fiyatları",
    "beton parlatma ankara",
    "beton parlatma istanbul",
    "beton parlatma izmir",
    "beton parlatma uygulama",
    "parlatılmış beton",
    "endüstriyel zemin",
    "lityum silikat",
]


def authenticate():
    """Google OAuth ile kimlik doğrulama."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("webmasters", "v3", credentials=creds)


def fetch_keyword_data(service, days: int = 28) -> list:
    """Son X gün için anahtar kelime verilerini çeker."""
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    request = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["query"],
        "rowLimit": 100,
        "dimensionFilterGroups": [],
    }

    response = (
        service.searchanalytics()
        .query(siteUrl=SITE_URL, body=request)
        .execute()
    )

    return response.get("rows", [])


def save_report(rows: list):
    """Raporu markdown olarak kaydeder."""
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{today}-search-console.md")

    # Hedef kelimeleri bul
    keyword_map = {r["keys"][0]: r for r in rows}
    target_rows = []
    for kw in TARGET_KEYWORDS:
        if kw in keyword_map:
            r = keyword_map[kw]
            target_rows.append(
                f"| {kw} | {r.get('clicks',0)} | {r.get('impressions',0)} | "
                f"{round(r.get('ctr',0)*100,1)}% | {round(r.get('position',0),1)} |"
            )
        else:
            target_rows.append(f"| {kw} | 0 | 0 | — | — |")

    # Genel toplamlar
    total_clicks = sum(r.get("clicks", 0) for r in rows)
    total_impressions = sum(r.get("impressions", 0) for r in rows)

    content = f"""# Search Console Raporu — {today}
Veri aralığı: Son 28 gün

## Genel

| Metrik | Değer |
|--------|-------|
| Toplam Tıklama | {total_clicks} |
| Toplam Gösterim | {total_impressions} |

## Hedef Anahtar Kelimeler

| Kelime | Tıklama | Gösterim | CTR | Konum |
|--------|---------|----------|-----|-------|
{chr(10).join(target_rows)}

## En İyi 20 Kelime (Tüm)

| Kelime | Tıklama | Gösterim | CTR | Konum |
|--------|---------|----------|-----|-------|
"""
    top20 = sorted(rows, key=lambda r: r.get("clicks", 0), reverse=True)[:20]
    for r in top20:
        kw = r["keys"][0]
        content += (
            f"| {kw} | {r.get('clicks',0)} | {r.get('impressions',0)} | "
            f"{round(r.get('ctr',0)*100,1)}% | {round(r.get('position',0),1)} |\n"
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Rapor kaydedildi: {filepath}")


def main():
    print("🔍 Search Console veri çekimi başlıyor...")
    service = authenticate()
    rows = fetch_keyword_data(service)
    print(f"  → {len(rows)} kelime bulundu")
    save_report(rows)


if __name__ == "__main__":
    main()
