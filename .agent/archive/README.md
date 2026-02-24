# Mevcut Site Arşivi — parlakbeton.com

# Arşiv Tarihi: 2026-02-24

# Kaynak: WordPress (Yoast SEO Sitemap)

# Sorumlu: CDO Can Erdoğan

## Amaç

Yeni Astro sitesine geçmeden önce mevcut WordPress sitesinin
tüm URL'lerini, içeriklerini ve yönlendirme haritasını arşivlemek.

## Klasör Yapısı

```
.agent/archive/
├── README.md               → Bu dosya
├── url-inventory.md        → Tüm mevcut URL'ler + durum
├── redirect-map.md         → Eski URL → Yeni URL (Caddy config)
├── content/                → Sayfa içerikleri (metin arşivi)
│   ├── anasayfa.md
│   ├── parlak-beton.md
│   ├── hakkimizda.md
│   ├── iletisim.md
│   ├── referanslar.md
│   └── blog/               → Blog yazıları
├── media/                  → Medya dosyası listesi (URL'ler)
│   └── media-list.md
└── pre-migration-checklist.md
```

## Göç Öncesi Kontrol

**Tamamlanan:**

- [x] URL envanteri çıkarıldı (sitemap crawl)
- [x] Yönlendirme haritası oluşturuldu
- [x] Pre-migration checklist hazırlandı

**Bekleyen (manuel):**

- [ ] Tüm medya dosyaları indirildi
- [ ] Search Console verisi export edildi
- [ ] Google Analytics verisi export edildi
- [ ] WordPress veritabanı yedeği alındı (CyberPanel backup)
- [ ] Site ekran görüntüleri arşivlendi (Wayback Machine)
