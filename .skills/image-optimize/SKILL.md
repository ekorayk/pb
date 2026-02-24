---
name: image-optimize
description: Proje görsellerini WebP formatına dönüştürür, boyutlandırır ve lazy loading uygular.
---

# Image Optimize Skill

## Ne Zaman Kullanılır?

- Projeye yeni görsel eklendiğinde
- Performans skoru düşük çıktığında
- Deploy öncesi görsel optimizasyon adımı olarak

## Kurallar

### Format

- **Hedef format:** WebP (JPEG/PNG kaynaklı)
- **Fallback:** JPEG (WebP desteklemeyen eski tarayıcılar için `<picture>` kullan)

### Boyutlar

| Kullanım | Maks. Genişlik |
|----------|---------------|
| Hero görseli | 1920px |
| Kart / thumbnail | 800px |
| Avatar / ikon | 200px |
| OG Image | 1200x630px |

### Kalite

- WebP: **80** kalite (iyi denge)
- JPEG fallback: **75** kalite

### HTML Şablonu

```html
<picture>
  <source srcset="gorsel.webp" type="image/webp">
  <img
    src="gorsel.jpg"
    alt="Açıklayıcı metin buraya"
    width="800"
    height="600"
    loading="lazy"
    decoding="async"
  >
</picture>
```

### Hero (Above the fold) — Lazy loading KULLANMA

```html
<picture>
  <source srcset="hero.webp" type="image/webp">
  <img
    src="hero.jpg"
    alt="Parlak Beton — Kaliteli Hazır Beton"
    width="1920"
    height="1080"
    loading="eager"
    fetchpriority="high"
  >
</picture>
```

## Araçlar

- **squoosh.app** — Tarayıcı tabanlı görsel sıkıştırma
- **sharp (npm)** — Toplu dönüşüm scripti için
