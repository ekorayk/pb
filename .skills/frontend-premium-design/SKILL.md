---
name: frontend-premium-design
description: Use when designing or building Parlak Beton's premium web frontend. Covers liquid glass effects, 3D concrete visualization, GSAP animations, scroll interactions, dark industrial aesthetic, responsive design, and performance optimization. Activate with keywords like "tasarım", "frontend", "animasyon", "liquid glass", "3D", "hero", "bileşen tasarla", "web görünümü", "mobil tasarım", "UI".
---

# Frontend Premium Design — Parlak Beton

## Tasarım Felsefesi: "Polished Dark"

Koyu endüstriyel estetik + premium cam efektleri + 3D beton görselleştirme.
Ziyaretçi siteye girdiğinde 3 saniyede "premium, güvenilir, uzman" mesajını almalı.

---

## Renk Sistemi (Design Tokens)

```css
:root {
  /* Zemin */
  --bg-deep:        #080808;
  --bg-surface:     #111111;
  --bg-elevated:    #1A1A1A;

  /* Metalik Gri Skalası */
  --metal-100:      #F0F0F0;
  --metal-200:      #E8E8E8;  /* parlatılmış yüzey */
  --metal-400:      #A0A0A0;  /* orta ton */
  --metal-600:      #505050;  /* derin gölge */
  --metal-900:      #1C1C1C;

  /* Vurgu */
  --accent:         #D4A853;  /* altın/amber — premium */
  --accent-glow:    rgba(212, 168, 83, 0.3);

  /* Liquid Glass */
  --glass-bg:       rgba(255, 255, 255, 0.06);
  --glass-border:   rgba(255, 255, 255, 0.12);
  --glass-blur:     24px;
  --glass-saturate: 180%;

  /* Tipografi */
  --font-sans:      'DM Sans', 'Inter', system-ui, sans-serif;
  --font-display:   'DM Sans', sans-serif;

  /* Boşluk */
  --space-section:  clamp(80px, 12vw, 160px);
  --space-gap:      clamp(24px, 4vw, 48px);

  /* Animasyon */
  --ease-out-expo:  cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out:    cubic-bezier(0.87, 0, 0.13, 1);
  --duration-fast:  200ms;
  --duration-mid:   500ms;
  --duration-slow:  1000ms;
}
```

---

## Liquid Glass Bileşeni

```css
.glass {
  background: var(--glass-bg);
  backdrop-filter: blur(var(--glass-blur)) saturate(var(--glass-saturate));
  -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(var(--glass-saturate));
  border: 1px solid var(--glass-border);
  border-radius: 16px;
}

/* Apple Liquid Glass — SVG refraksiyon filtresi */
.liquid-glass {
  filter: url(#liquid-glass-filter);
  position: relative;
}
```

```html
<!-- SVG filtre tanımı (body başına ekle) -->
<svg style="display:none" aria-hidden="true">
  <defs>
    <filter id="liquid-glass-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2"
                    result="noise" seed="2"/>
      <feDisplacementMap in="SourceGraphic" in2="noise"
                         scale="8" xChannelSelector="R" yChannelSelector="G"
                         result="displaced"/>
      <feComposite in="displaced" in2="SourceGraphic" operator="atop"/>
    </filter>
  </defs>
</svg>
```

---

## Tipografi Sistemi

```css
/* Responsive fluid typography */
.text-display {
  font-size: clamp(3rem, 8vw, 7rem);
  font-weight: 300;
  letter-spacing: -0.03em;
  line-height: 1.05;
  color: var(--metal-200);
}

.text-hero-accent {
  background: linear-gradient(135deg, var(--metal-100) 0%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-body {
  font-size: clamp(1rem, 2vw, 1.125rem);
  line-height: 1.7;
  color: var(--metal-400);
}
```

---

## GSAP Animasyon Şablonları

```javascript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

// Hero reveal
export function heroReveal() {
  const tl = gsap.timeline({ delay: 0.3 });
  tl.from(".hero-eyebrow", { y: 20, opacity: 0, duration: 0.6 })
    .from(".hero-title", { y: 40, opacity: 0, duration: 0.8,
                            ease: "power3.out" }, "-=0.3")
    .from(".hero-subtitle", { y: 20, opacity: 0, duration: 0.6 }, "-=0.4")
    .from(".hero-cta", { y: 20, opacity: 0, duration: 0.5 }, "-=0.3");
}

// Scroll fade-in (her section için)
export function scrollReveal(selector = ".reveal") {
  gsap.utils.toArray(selector).forEach((el) => {
    gsap.from(el, {
      y: 50,
      opacity: 0,
      duration: 0.8,
      ease: "power2.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
        toggleActions: "play none none none",
      },
    });
  });
}

// Paralaks arka plan
export function parallaxBg(selector = ".parallax-bg") {
  gsap.utils.toArray(selector).forEach((el) => {
    gsap.to(el, {
      yPercent: -20,
      ease: "none",
      scrollTrigger: {
        trigger: el.parentElement,
        scrub: 1,
      },
    });
  });
}
```

---

## 3D Entegrasyon (Spline)

```astro
---
// src/components/ConcreteScene.astro
// Spline kullanımı — lazy load
---
<div id="spline-container" class="spline-wrapper">
  <div class="spline-placeholder">
    <!-- Fallback: CSS animated gradient -->
  </div>
</div>

<script>
  // IntersectionObserver ile lazy load
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      // WebGL desteği var mı?
      const canvas = document.createElement('canvas');
      const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

      if (gl) {
        import('@splinetool/runtime').then(({ Application }) => {
          const app = new Application(canvas);
          app.load('https://prod.spline.design/[SCENE-ID]/scene.splinecode');
          document.getElementById('spline-container').appendChild(canvas);
        });
      }
      // WebGL yoksa placeholder kalır
      observer.disconnect();
    }
  }, { threshold: 0.1 });

  observer.observe(document.getElementById('spline-container'));
</script>

<style>
.spline-wrapper {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 24px;
  overflow: hidden;
  position: relative;
}
.spline-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(
    135deg,
    var(--bg-elevated) 0%,
    var(--metal-900) 50%,
    var(--bg-elevated) 100%
  );
  background-size: 200% 200%;
  animation: shimmer 3s ease-in-out infinite;
}
@keyframes shimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
</style>
```

---

## Responsive Kurallar

```css
/* Mobile-first breakpoints */
/* sm: 640px | md: 768px | lg: 1024px | xl: 1280px */

/* Navigasyon */
@media (max-width: 768px) {
  /* Hamburger menü — tam ekran glass overlay */
  .nav-mobile {
    position: fixed;
    inset: 0;
    background: rgba(8, 8, 8, 0.95);
    backdrop-filter: blur(40px);
    z-index: 100;
  }
}

/* 3D sahneler — mobilde devre dışı */
@media (max-width: 768px) {
  .spline-wrapper {
    display: none;
  }
  .mobile-3d-replacement {
    display: block; /* CSS gradient alternatif */
  }
}

/* Sabit CTA (mobil) */
.floating-cta-mobile {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 50;
  display: none;
}
@media (max-width: 768px) {
  .floating-cta-mobile { display: flex; }
}
```

---

## Navbar (Liquid Glass)

```astro
<nav class="navbar glass" role="navigation">
  <a href="/" class="logo" aria-label="Parlak Beton Ana Sayfa">
    <!-- Logo SVG -->
  </a>
  <ul class="nav-links" role="list">
    <li><a href="/hizmetler">Hizmetler</a></li>
    <li><a href="/projeler">Projeler</a></li>
    <li><a href="/hakkimizda">Hakkımızda</a></li>
  </ul>
  <a href="/iletisim" class="nav-cta" id="nav-contact-cta">
    Keşif Talep Et
  </a>
</nav>

<style>
.navbar {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: min(95vw, 1200px);
  padding: 16px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 100;
  border-radius: 100px; /* pill shape */
  transition: background var(--duration-fast) ease;
}

.nav-cta {
  background: var(--accent);
  color: #000;
  padding: 10px 24px;
  border-radius: 100px;
  font-weight: 600;
  font-size: 0.875rem;
  transition: transform var(--duration-fast) var(--ease-out-expo),
              box-shadow var(--duration-fast) ease;
}

.nav-cta:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 32px var(--accent-glow);
}
</style>
```

---

## Performans Kontrol Listesi

Geliştirme sonrası her seferinde:

- [ ] Lighthouse Mobile ≥ 90 | Desktop ≥ 95
- [ ] LCP < 2.5s (hero image/text)
- [ ] CLS < 0.1 (layout shift yok)
- [ ] INP < 200ms (mobil dokunma tepkisi)
- [ ] 3D lazy load çalışıyor (DevTools Network)
- [ ] WebGL fallback test: `about:config` → webgl.disabled = true
- [ ] Tüm animasyonlar `prefers-reduced-motion` dikkate alıyor
- [ ] Form mobilde 2 scroll içinde görünüyor
- [ ] WhatsApp butonu mobilde sabit
