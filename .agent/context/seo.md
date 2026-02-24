# SEO Stratejisi — parlakbeton.com

# Son güncelleme: 2026-02-24

---

## Terminoloji Standardı

| Katman | Terim | Nerede |
|--------|-------|--------|
| Marka iletişimi | "Parlak Beton uygulaması" | CRM, teklif, müşteri mesajları |
| SEO / teknik | "beton parlatma" | Sayfa başlıkları, meta, URL, schema |
| Global karşılık | "Polished Concrete" | Uluslararası içerik (gelecek faz) |

---

## Mevcut Sıralama Durumu

| Anahtar Kelime | Mevcut Konum | Hedef | Öncelik |
|----------------|-------------|-------|---------|
| parlak beton | ~1 | 1 (koru) | 🔴 |
| beton parlatma | ~10-30 | ≤ 3 | 🔴 |
| beton parlatma fiyatları | — | ≤ 5 | 🔴 |
| beton parlatma ankara | — | ≤ 3 | 🟠 |
| beton parlatma istanbul | — | ≤ 3 | 🟠 |
| beton parlatma izmir | — | ≤ 3 | 🟠 |
| parlatılmış beton | — | ≤ 5 | 🟡 |
| endüstriyel zemin | — | ≤ 10 | 🟡 |
| lityum silikat uygulama | — | ≤ 5 | 🟡 |
| beton parlatma nasıl yapılır | — | ≤ 3 | 🟡 |
| beton parlatma mı epoksi mi | — | ≤ 3 | 🟡 |

---

## Öncelikli Lokasyonlar

Taşeron ekip bulunduran şehirler — lokasyon sayfası önceliği:

1. **Ankara** (birincil)
2. **İstanbul** (birincil)
3. **İzmir** (birincil)
4. Diğer şehirler → ileriki fazda, talebe göre

---

## İçerik Mimarisi (Hedef URL Yapısı)

```
/beton-parlatma/                    ← ANA hedef sayfa
/beton-parlatma/fiyatlari/          ← En yüksek ticari niyet
/beton-parlatma/nasil-yapilir/      ← Bilgi içeriği, E-E-A-T
/beton-parlatma/ankara/             ← Lokasyon
/beton-parlatma/istanbul/           ← Lokasyon
/beton-parlatma/izmir/              ← Lokasyon
/blog/beton-parlatma-epoksi-karsilastirma/
/blog/lityum-silikat-nedir/
/blog/fabrika-zemini-cozumleri/
/blog/parlatilmis-beton-kac-yil-dayanir/
```

---

## Meta Şablonları

### Ana Sayfa (/)

- **Title:** `Parlak Beton | Profesyonel Beton Parlatma Uzmanı`
- **Description:** `15 yıllık deneyimle Parlak Beton uygulaması — fabrika, depo ve ofis zeminleriniz için profesyonel çözüm. Ankara, İstanbul, İzmir. Ücretsiz keşif için arayın: +90 507 218 5318`

### /beton-parlatma/

- **Title:** `Beton Parlatma Hizmeti | Parlak Beton A.Ş. | Ankara · İstanbul · İzmir`
- **Description:** `Türkiye'nin beton parlatma uzmanı. Lityum silikat teknolojisi, ANSI/NFSI standartları, 15+ yıl deneyim. Fabrika, depo, ofis. Ücretsiz keşif: 0507 218 5318`

### /beton-parlatma/fiyatlari/

- **Title:** `Beton Parlatma Fiyatları 2026 | m² Bazında Hesaplama | Parlak Beton`
- **Description:** `Beton parlatma fiyatları: alan m², zemin durumu ve parlaklık seviyesine göre belirlenir. Ücretsiz keşif ve fiyat teklifi için hemen arayın.`

---

## Backlink Stratejisi

### Mevcut Referans Firmalar (Potansiyel Backlink)

- Debak Denizli (debak.com.tr)
- Garanti İplik (garanti-iplik.com.tr)
- Tedak Elektrik (tedak.com.tr)
- Sabiha Gökçen İSG (sabihagokcen.aero)
- Kansai Altan (kansaialtan.com.tr)
- Sirmersan Mermer (sirmersan.com.tr)

**Not (Dr. Emre):** Mevcut müşterilere backlink isteği şu an uygun değil.
Yeni projelerde sözleşme aşamasında referans anlaşması yapılacak.

### Hedef Backlink Kaynakları

- Sektör dergileri (inşaat, endüstri)
- Mimarlık ofisleri blog/kaynak sayfaları
- Müteahhit firmaların tedarikçi listeleri

---

## Teknik SEO Kontrol Listesi (Yeni Site)

- [ ] robots.txt
- [ ] sitemap.xml (Astro otomatik üretecek)
- [ ] Schema.org: LocalBusiness + FAQPage + Service
- [ ] Canonical URL'ler
- [ ] Open Graph etiketleri (her sayfa)
- [ ] Hreflang (gelecek — uluslararası faz)
- [ ] Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1
- [ ] IndexNow (Bing anlık indeksleme)
- [ ] Breadcrumb schema

---

## Analytics Takibi

Tüm metrik takibi: `.agent/analytics/`
Haftalık otomatik raporlar: `scripts/` klasöründeki Python scriptleri (lxc-db cron)
