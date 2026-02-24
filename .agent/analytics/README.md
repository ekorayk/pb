# Analytics Sistemi — parlakbeton.com

## Amaç

Tüm dijital performans metriklerini tek bir yerde toplamak,
baseline oluşturmak ve zaman içindeki gelişimi ölçmek.

## Klasör Yapısı

```
.agent/analytics/
├── README.md               → Bu dosya
├── baseline/               → İlk snapshot (proje başlangıcı)
│   ├── pagespeed.md        → PageSpeed Insights sonuçları
│   ├── search-console.md   → GSC anahtar kelime ve trafik verileri
│   ├── analytics.md        → GA4 kullanıcı verileri
│   ├── bing.md             → Bing Webmaster verileri
│   └── cloudflare.md       → Cloudflare trafik verileri
├── reports/                → Otomatik haftalık/aylık raporlar
│   └── YYYY-MM-DD.md
└── scripts/                → API bağlantı Python scriptleri
    ├── pagespeed.py
    ├── search_console.py
    ├── ga4.py
    └── report_generator.py
```

## Veri Güncelleme Sıklığı

| Kaynak | Otomatik | Sıklık |
|--------|----------|--------|
| PageSpeed | ✅ API | Haftalık (Pazartesi) |
| Search Console | ✅ API | Haftalık |
| GA4 | ✅ API | Haftalık |
| Bing | ✅ API | Aylık |
| Cloudflare | ✅ API | Haftalık |

## Manuel Güncelleme (API kurulana kadar)

PageSpeed → pagespeed.web.dev → sonuçları baseline/pagespeed.md'ye yapıştır
Search Console → Google Search Console → Performans → CSV ihracat → baseline/search-console.md'ye yaz
GA4 → Analytics → Raporlar → baseline/analytics.md'ye yaz
