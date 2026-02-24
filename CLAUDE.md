# parlakbeton.com — AI Yönetim Sistemi Kılavuzu

Bu dosya; Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş. firmasının
**tüm dijital operasyonlarını AI destekli yönetmek** için hazırlanmış
otoriter talimat dosyasıdır.

Web sitesi geliştirme, SEO, içerik üretimi, müşteri iletişimi şablonları,
teklif süreçleri ve marka yönetimi bu sistem üzerinden koordine edilir.

---

## Firma Kimliği

| Alan | Değer |
|------|-------|
| **Ticari Unvan** | Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş. |
| **Domain** | parlakbeton.com |
| **Telefon** | +90 507 218 5318 |
| **Sektör** | Endüstriyel Zemin — Beton Parlatma & Zemin Teknolojileri |
| **Uzmanlık** | Mekanik beton parlatma, lityum silikat kristalizasyon |
| **Deneyim** | 15+ yıl |
| **Standartlar** | ANSI A137.1, NFSI, DCOF 0.42+ |

---

## Yönetim Alanları (Sistemin Kapsamı)

Bu proje aşağıdaki tüm operasyonları AI desteğiyle yönetir:

```
parlakbeton.com/
├── 📁 .agent/
│   ├── workflows/              # Otomasyon iş akışları (/slash komutları)
│   └── context/               # Tüm operasyonel bağlam verileri
│       ├── project.md         # Marka, palet, kurumsal kimlik
│       ├── hosting.md         # Sunucu & domain yönetimi
│       ├── seo.md             # SEO stratejisi & anahtar kelimeler
│       ├── llm-context.md     # AI/LLM sistemleri için kurumsal veri
│       ├── services.md        # Hizmet kataloğu & teknik detaylar
│       ├── references.md      # Referans projeler & müşteri hikayeleri
│       └── crm.md             # Müşteri şablonları & satış süreçleri
│
├── 📁 .skills/                # Yeniden kullanılabilir AI beceri modülleri
│   ├── seo-audit/             # Sayfa SEO denetimi
│   ├── image-optimize/        # Görsel optimizasyon
│   ├── component-builder/     # UI bileşen geliştirme
│   ├── content-writer/        # SEO uyumlu içerik yazımı
│   └── offer-generator/       # Müşteri teklif şablonları
│
├── 📁 src/                    # Astro + AstroWind web sitesi
│   ├── components/
│   ├── content/
│   ├── layouts/
│   └── pages/
│       ├── index.astro
│       ├── hizmetler/
│       ├── projeler.astro
│       ├── hakkimizda.astro
│       └── iletisim.astro
│
└── 📁 public/
```

---

## Teknoloji Stack

| Katman | Teknoloji |
|--------|-----------|
| **Framework** | Astro (statik) |
| **Stil** | Vanilla CSS + Design Tokens |
| **Dil** | TypeScript + Astro components |
| **Backend** | Python FastAPI (lxc-web-api) |
| **Veritabanı** | PostgreSQL (lxc-db) |
| **Python Env** | Miniconda → `pb-env` (`.conda/envs/pb-env`) |
| **PDF** | WeasyPrint (sunucu) / fpdf2 (Windows geliştirme) |
| **Deploy** | → bkz. `.agent/context/hosting.md` |

> **KURAL:** AstroWind'in mevcut bileşenlerini önce kontrol et.
> Varsa özelleştir, yoksa Astro bileşen yapısına uygun yaz.

---

## Sayfa Haritası & Öncelikler

| Sayfa | URL | SEO Hedef Kelime | Öncelik |
|-------|-----|-----------------|---------|
| Ana Sayfa | `/` | beton parlatma | 🔴 Kritik |
| Hizmetler Hub | `/hizmetler` | beton parlatma hizmetleri | 🔴 Kritik |
| Beton Parlatma | `/hizmetler/beton-parlatma` | beton parlatma fiyatları | 🔴 Kritik |
| Lityum Silikat | `/hizmetler/lityum-silikat` | lityum silikat uygulama | 🟠 Yüksek |
| Zemin Tamiratı | `/hizmetler/zemin-tamiratı` | zemin tamiratı | 🟡 Orta |
| Referans Projeler | `/projeler` | beton parlatma referansları | 🟠 Yüksek |
| Hakkımızda | `/hakkimizda` | parlak beton A.Ş. | 🟡 Orta |
| İletişim & Keşif | `/iletisim` | beton parlatma keşif | 🔴 Kritik |
| Blog / İçerik | `/blog` | endüstriyel zemin (long-tail) | 🟠 Yüksek |

---

## Geliştirme Kuralları

### Astro Kuralları

- Sayfa bileşenleri `.astro` uzantılı, `PascalCase` isimlendirme
- İstemci JS gerekiyorsa `client:visible` tercih et (performans)
- Görsel için `<Image />` bileşeni — WebP otomatik, lazy loading dahil
- Hero görseli: `loading="eager"` + `fetchpriority="high"`

### Tailwind Kuralları

- AstroWind `tailwind.config.mjs` token'larına bağlı kal
- Yeni marka renkleri config'e ekle — inline style YAZMA
- `dark:` prefix ile dark mode desteği zorunlu

### İçerik & Metin Kuralları

- **Ton:** Teknik otorite + güven veren profesyonellik
- **Dil:** Türkçe — sade, net, jargon açıklamalı
- Teknik terimler (lityum silikat, DCOF, Mohs) ilk kullanımda açıklanmalı
- İçerik üretiminde `.skills/content-writer/SKILL.md` kullan

### SEO Zorunlulukları

- Her sayfa: benzersiz `<title>` (50-60 kar.) + `<meta description>` (150-160 kar.)
- Sayfada tek `<h1>`, hiyerarşi korunmalı
- Tüm görseller `alt` attribute içermeli
- Schema.org: `LocalBusiness` + sayfa tipine özgü type
- FAQ sayfaları için `FAQPage` schema (mevcut sitede var, korunmalı)

### Performans Hedefleri

- Lighthouse Mobile ≥ 90
- LCP < 2.5s | INP < 200ms | CLS < 0.1

---

## Önemli Bağlam Dosyaları (Her Görevde Önce Oku)

| Dosya | Ne İçerir |
|-------|-----------|
| `.agent/context/services.md` | Hizmet kataloğu, teknik detaylar, fiyatlandırma mantığı |
| `.agent/context/references.md` | Referans projeler — Debak, Garanti İplik, Tedak, diğerleri |
| `.agent/context/llm-context.md` | SSS, Schema.org, LLM/AI sistemleri için kurumsal özet |
| `.agent/context/seo.md` | Anahtar kelimeler, meta şablonları, sayfa bazlı hedefler |
| `.agent/context/crm.md` | Müşteri şablon mesajları, teklif süreci, takip protokolleri |
| `.agent/context/project.md` | Marka kimliği, renk paleti, tipografi |
| `.agent/context/hosting.md` | Sunucu, deploy, domain bilgileri |

---

## AI Yönetim Kurulu

Her karar, strateji veya aksiyon öncesinde ilgili yönetici(ler)in görüşü alınır.
Yönetim Kurulu protokolü ve tüm persona dosyaları için → `.agent/board/README.md`

| Kod | İsim | Unvan | Dosya |
|-----|------|-------|-------|
| CEO | Alexander Kaya | Genel Müdür | `board/ceo.md` |
| CFO | Dilek Aksoy | Mali İşler Direktörü | `board/cfo.md` |
| CMO | Serena Öztürk | Pazarlama Direktörü | `board/cmo.md` |
| CSO | Mehmet Çelik | Satış Direktörü | `board/cso.md` |
| CTO | Dr. Emre Yıldız | Teknik Direktör | `board/cto.md` |
| COO | Levent Arslan | Operasyon Direktörü | `board/coo.md` |
| CHRO | Ayşe Demirkan | İK Direktörü | `board/chro.md` |
| CDO | Can Erdoğan | Dijital Dönüşüm Direktörü | `board/cdo.md` |
| CLO | Av. Neslihan Şahin | Baş Hukuk Danışmanı | `board/clo.md` |
| CXO | Pınar Koç | Müşteri Deneyimi Direktörü | `board/cxo.md` |

---

## Slash Komutları

| Komut | Açıklama |
|-------|----------|
| `/dev-server` | Astro geliştirme sunucusu |
| `/build` | Prodüksiyon build |
| `/deploy` | Deploy işlemi |

---

## Skill Ekosistemi

37 skill aktif. Manifest: `.claude-plugin/marketplace.json`

### YK Advisor Skills (her üye için özel)

| Skill | Tetikleyici | Üye |
|-------|-------------|-----|
| `ceo-advisor` | strateji, vizyon, büyüme, CEO | Alexander |
| `cfo-advisor` + `cfo-tr-advisor` | finans, KDV, e-fatura, maliyet, CFO | Dilek |
| `cmo-advisor` | pazarlama, marka, kampanya, CMO | Serena |
| `cso-advisor` + `cso-whatsapp-scripts` | satış, teklif, WhatsApp, CSO | Mehmet |
| `cto-advisor` | teknik, zemin, lityum, DCOF, CTO | Dr. Emre |
| `coo-advisor` + `coo-project-flow` | operasyon, proje akışı, saha, COO | Levent |
| `chro-advisor` | IK, personel, taşeron, CHRO | Ayşe |
| `cdo-advisor` + `cdo-infrastructure` | dijital, API, Proxmox, deploy, CDO | Can |
| `clo-advisor` + `clo-tr-templates` | hukuk, sözleşme, KVKK, CLO | Neslihan |
| `customer-success` | müşteri memnuniyeti, CXO | Pınar |

### Frontend & Tasarım Skills (Anthropic Resmi + Custom)

`frontend-design` · `frontend-premium-design` · `theme-factory` · `canvas-design`
`brand-guidelines` · `web-artifacts-builder`

### Belge Üretimi Skills (Anthropic Resmi)

`pdf` · `docx` · `pptx` · `skill-creator`

### Pazarlama & Büyüme Skills

`seo-audit` · `content-strategy` · `copywriting` · `page-cro` · `form-cro`
`programmatic-seo` · `schema-markup` · `social-content` · `email-sequence`
`cold-email` · `paid-ads` · `analytics-tracking` · `marketing-psychology`
`launch-strategy` · `referral-program` · `churn-prevention` · `competitor-alternatives`

### Satış & Gelir Skills

`pricing-strategy` · `sales-advisor` · `revenue-operations` · `offer-generator` · `risk-management`

### Geliştirme & Test Skills

`webapp-testing` · `component-builder` · `content-writer` · `image-optimize`
`shared-miniconda-project-env` · `skill-scout`
