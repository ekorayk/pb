---
name: seo-audit
description: Bir HTML sayfasının SEO denetimini yapar; eksik meta etiketleri, başlık hiyerarşisi, Schema.org ve Core Web Vitals uyumunu kontrol eder.
---

# SEO Audit Skill

## Ne Zaman Kullanılır?

- Yeni bir sayfa oluşturulduğunda
- Mevcut sayfa güncellenmeden önce
- Deploy öncesi son kontrol olarak

## Kontrol Listesi

### 1. Meta Etiketler

- [ ] `<title>` — 50-60 karakter arası, anahtar kelime içermeli
- [ ] `<meta name="description">` — 150-160 karakter, CTA içermeli
- [ ] `<meta name="robots" content="index, follow">`
- [ ] `<link rel="canonical">`

### 2. Open Graph

- [ ] `og:title`
- [ ] `og:description`
- [ ] `og:image` — 1200x630px
- [ ] `og:url`
- [ ] `og:type`

### 3. Başlık Hiyerarşisi

- [ ] Sayfada tek `<h1>` var mı?
- [ ] `<h2>` → `<h3>` sırası bozulmuyor mu?
- [ ] Başlıklar anahtar kelime içeriyor mu?

### 4. Görsel SEO

- [ ] Tüm `<img>` etiketlerinde `alt` var mı?
- [ ] Görseller WebP formatında mı?
- [ ] Boyut belirtilmiş mi (`width` / `height`)?

### 5. Schema.org

- [ ] `LocalBusiness` yapısal verisi var mı?
- [ ] `BreadcrumbList` eklendi mi?
- [ ] JSON-LD formatı doğru mu? ([validator](https://validator.schema.org/))

### 6. Teknik

- [ ] Sayfa hızı: [PageSpeed Insights](https://pagespeed.web.dev/) skoru 90+
- [ ] robots.txt erişilebilir mi?
- [ ] sitemap.xml mevcut mu?
- [ ] SSL aktif mi (HTTPS)?

## Hız Referansı (parlakbeton.com için hedefler)

| Metrik | Hedef |
|--------|-------|
| LCP | < 2.5s |
| FID / INP | < 200ms |
| CLS | < 0.1 |
| Mobile Score | ≥ 90 |
| Desktop Score | ≥ 95 |
