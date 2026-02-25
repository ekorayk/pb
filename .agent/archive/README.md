# Mevcut Site Arşivi — parlakbeton.com

# Arşiv Tarihi: 2026-02-25 (Güncelleme: 2026-02-25)

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
- [x] Yönlendirme haritası oluşturuldu (Caddy + Nginx)
- [x] Pre-migration checklist hazırlandı
- [x] Tüm statik sayfa içerikleri arşivlendi (content/ klasörü)
- [x] 17 blog yazısının içerikleri arşivlendi (content/blog/ klasörü)
- [x] Referans firma bilgileri ve müşteri yorumları kaydedildi
- [x] Gizlilik politikası metni arşivlendi (CLO onaylı)
- [x] Broşür URL'si tespit edildi (indirme bekliyor)

**Bekleyen (manuel — acil):**

- [ ] WordPress veritabanı yedeği alındı (CyberPanel backup)
- [ ] Medya dosyaları indirildi (wp-content/uploads/)
- [ ] Broşür PDF'leri indirildi
- [ ] Search Console verisi export edildi
- [ ] Google Analytics verisi export edildi
- [ ] Wayback Machine arşivi oluşturuldu
- [ ] Ekran görüntüleri alındı (desktop + mobile)
- [ ] 6 blog yazısının tam içeriği WordPress'ten export edildi (makinesi, nasıl-calisir, yeniden-dogusu, elektrik-enerji, kullanim-alanlari, uretim-kalitesi)
