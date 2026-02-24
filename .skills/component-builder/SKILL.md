---
name: component-builder
description: Yeni HTML/CSS bileşeni oluştururken takip edilmesi gereken adımlar ve şablonlar.
---

# Component Builder Skill

## Ne Zaman Kullanılır?

- Yeni bir UI bileşeni (kart, modal, hero, vb.) oluşturulacağında
- Mevcut bileşen refactor edilecekken
- Tasarım tutarlılığını sağlamak için

## Bileşen Geliştirme Adımları

1. **İsimlendir:** `kebab-case` kullan (ör: `service-card`, `hero-section`)
2. **HTML yaz:** Semantic elementler kullan (`<section>`, `<article>`, `<nav>`)
3. **CSS yaz:** BEM veya utility-first yaklaşım — projeye hangisi hakimse onu kullan
4. **Erişilebilirlik:** `aria-*` attribute ve `role` ekle
5. **Responsive:** Mobile-first media query yaz
6. **SEO:** Uygunsa heading, alt text ekle

## Şablon — Servis Kartı

```html
<!-- service-card.html -->
<article class="service-card" aria-label="Hizmet adı">
  <div class="service-card__icon" aria-hidden="true">
    <!-- SVG ikon -->
  </div>
  <h3 class="service-card__title">Hizmet Başlığı</h3>
  <p class="service-card__desc">Kısa açıklama metni.</p>
  <a href="/hizmetler/hizmet-adi" class="service-card__link">
    Detayları Gör
    <span class="sr-only">— Hizmet adı hakkında</span>
  </a>
</article>
```

```css
/* service-card.css */
.service-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  padding: var(--space-6);
  background: var(--color-surface);
  border-radius: var(--radius-md);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

@media (prefers-reduced-motion: reduce) {
  .service-card {
    transition: none;
  }
}
```

## CSS Değişkenleri (Design Tokens)

Projedeki global CSS tokenları `src/styles/tokens.css` dosyasında tanımla:

```css
:root {
  /* Renkler */
  --color-primary: #1a1a2e;
  --color-accent: #e94560;
  --color-surface: #ffffff;
  --color-text: #2d2d2d;
  --color-muted: #6b7280;

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.12);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.15);
}
```
