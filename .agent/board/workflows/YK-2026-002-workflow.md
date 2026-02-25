# Workflow: YK-2026-002 — v5+ Web Sitesi Revizyonu

**Case Referansı:** [YK-2026-002-v5plus-website-revision.md](../cases/active/YK-2026-002-v5plus-website-revision.md)

---

## 📋 Özet

v5+ web sitesi: İnteraktivite + SEO mimari + build-free içerik yönetimi

**Bütçe:** 31.000 ₺
**Süre:** 8 hafta (3 sprint)
**Proje Lideri:** CDO (Can Erdoğan)
**İçerik Desteği:** CMO (Serena Öztürk)

---

## 🎯 Sprint Yapısı

### Sprint 1: MVP (Hafta 1-2)
**Hedef:** Lead almaya başla
**Deadline:** 2026-03-11

### Sprint 2: İnteraktivite (Hafta 3-4)
**Hedef:** Form dönüşüm optimize
**Deadline:** 2026-03-25

### Sprint 3: İçerik Motoru (Hafta 5-8)
**Hedef:** SEO organik trafik başlat
**Deadline:** 2026-04-22

---

## ✅ Aksiyonlar (Departman Bazlı)

### 💻 CDO (Can Erdoğan)

#### Sprint 1: MVP
| # | Aksiyon | Deadline | Durum | Progress |
|---|---------|----------|-------|----------|
| 1 | Astro proje kurulumu | 2026-02-26 | ⏳ | 0% |
| 3 | Ana sayfa + layout | 2026-03-02 | ⏳ | 0% |
| 4 | 3 hizmet sayfası | 2026-03-05 | ⏳ | 0% |
| 5 | Referans projeler (5) | 2026-03-07 | ⏳ | 0% |
| 6 | İletişim + form | 2026-03-09 | ⏳ | 0% |
| 7 | **MVP DEPLOY** | **2026-03-11** | ⏳ | **0%** |

#### Sprint 2: İnteraktivite
| # | Aksiyon | Deadline | Durum | Progress |
|---|---------|----------|-------|----------|
| 8 | Fiyat hesaplayıcı | 2026-03-15 | ⏳ | 0% |
| 9 | Quiz component | 2026-03-18 | ⏳ | 0% |
| 10 | Before/after slider | 2026-03-21 | ⏳ | 0% |
| 11 | **Sprint 2 DEPLOY** | **2026-03-25** | ⏳ | **0%** |

#### Sprint 3: İçerik Altyapısı
| # | Aksiyon | Deadline | Durum | Progress |
|---|---------|----------|-------|----------|
| 13 | Blog altyapısı | 2026-04-01 | ⏳ | 0% |
| 14 | Decap CMS (opsiyonel) | 2026-05-31 | ⏸️ | 0% |
| 16 | Schema.org markup | 2026-04-12 | ⏳ | 0% |
| 17 | Sitemap + Analytics | 2026-04-15 | ⏳ | 0% |
| 18 | Lighthouse CI | 2026-04-17 | ⏳ | 0% |
| 19 | **Sprint 3 DEPLOY** | **2026-04-22** | ⏳ | **0%** |

---

### 📢 CMO (Serena Öztürk)

| # | Aksiyon | Deadline | Durum | Progress |
|---|---------|----------|-------|----------|
| 2 | v5+ mockup wireframe (interaktif) | 2026-02-28 | ⏳ | 0% |
| 12 | İlk 10 blog konu seçimi | 2026-03-27 | ⏳ | 0% |
| 15 | İlk 10 blog yazısı (AI) | 2026-04-10 | ⏳ | 0% |
| 20 | İlk aylık SEO raporu | 2026-05-01 | ⏳ | 0% |

---

### 🎯 CEO (Alexander Kaya)

| # | Aksiyon | Deadline | Durum | Progress |
|---|---------|----------|-------|----------|
| 21 | 3 aylık CEO Review Toplantısı | 2026-07-25 | ⏳ | 0% |

---

## 📅 Timeline (Gantt)

```
Şubat 2026
└── 25-28: Hazırlık (proje setup + mockup wireframe)

Mart 2026
├── 02: Sprint 1 başlangıç
├── 11: MVP DEPLOY 🎯 (Milestone 1)
├── 12: Sprint 2 başlangıç
└── 25: İnteraktivite DEPLOY 🎯 (Milestone 2)

Nisan 2026
├── 01: Sprint 3 başlangıç
├── 10: İlk 10 blog yazısı hazır
└── 22: Full Site DEPLOY 🎯 (Milestone 3 — FINAL)

Mayıs 2026
└── 01: İlk aylık SEO raporu

Temmuz 2026
└── 25: 3 Aylık CEO Review 📊
```

---

## 📊 KPI Tracking

| KPI | Baseline | 1 Ay | 3 Ay | 6 Ay | Hedef (6 ay) |
|-----|----------|------|------|------|-------------|
| MVP canlı | ❌ | - | - | - | ✅ |
| Lead/ay | 0 | - | 20+ | - | 40+ |
| Organik trafik/ay | 0 | - | 500+ | - | 2.000+ |
| "beton parlatma fiyatları" sırası | N/A | - | ≤20 | - | ≤5 |
| Featured snippet | 0 | - | 1+ | - | 3+ |
| Blog yazısı | 0 | - | 10+ | - | 25+ |
| Lighthouse Mobile | N/A | - | 90+ | - | 95+ |

**Güncelleme:** Her ay CMO + CDO tarafından

---

## 🚨 Risk & Engeller

| Risk | Olasılık | Etki | Önlem | Sorumlu |
|------|----------|------|-------|---------|
| Sprint 1 süre aşımı | Orta | Yüksek | SADECE MVP — scope freeze | CDO |
| Markdown öğrenme eğrimi | Orta | Düşük | Decap CMS web UI (WYSIWYG) | CDO |
| İçerik üretim ritmi düşer | Orta | Orta | İlk 3 ay AI toplu üretim | CMO |
| Performans (JS yükü) | Düşük | Orta | Lazy loading + islands | CDO |
| Odak dağılması (Multimedia case) | Orta | Orta | Farklı timeline'lar | CEO |

---

## 📝 Progress Log

| Tarih | Güncelleme | Kimin Tarafından |
|-------|------------|------------------|
| 2026-02-25 | Workflow oluşturuldu, Can ve Serena bilgilendirildi | AI Agent |
| [Tarih] | [Sprint update] | [CDO/CMO] |

---

## 🎯 Milestones

- ✅ **2026-02-25:** Case onaylandı
- ⏳ **2026-02-26:** Proje kurulumu başladı
- ⏳ **2026-03-11:** MVP DEPLOY (Sprint 1) 🚀
- ⏳ **2026-03-25:** İnteraktivite DEPLOY (Sprint 2) 🚀
- ⏳ **2026-04-22:** Full Site DEPLOY (Sprint 3) 🚀
- ⏳ **2026-05-01:** İlk aylık SEO raporu
- ⏳ **2026-07-25:** 3 Aylık CEO Review

---

**Workflow Durumu:** 🔄 Aktif
**Son Güncelleme:** 2026-02-25
**Sonraki Milestone:** 2026-03-11 (MVP DEPLOY)
**Proje Completion:** 0% (21/21 aksiyon bekliyor)
