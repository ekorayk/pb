# Master Plan — Parlak Beton AI Yönetim Sistemi

# Versiyon 1.0 | Tarih: 2026-02-24

Bu dosya; sistemin tüm bileşenlerini, mimarisini ve geliştirme yol haritasını içerir.
Herhangi bir teknik karar buradaki planla çelişiyorsa bu dosya referans alınır.

---

## Vizyon

Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş.'nin tüm dijital ve
operasyonel süreçlerini; self-hosted, AI yönetimli, uçtan uca otomatize
bir sistem üzerinde yönetmek.

**Hedef:** 12 ay içinde 5.000.000 ₺ net kâr
**Model:** Tek kişi (Erhan Karaman) + taşeron ağı + AI yönetim sistemi

---

## Altyapı Mimarisi

```
PROXMOX (6GB RAM / 4 Core / Self-hosted)
│
├── lxc-cyberpanel    Ubuntu | ~2.5GB | Mevcut müşteri siteleri (~5 site)
│
├── lxc-proxy         Debian 12 | 256MB | 1 Core | 10GB
│   └── Caddy (Reverse Proxy + Let's Encrypt via Cloudflare DNS API)
│
├── lxc-web-api       Debian 12 | 1.5GB | 1-2 Core | 20GB
│   ├── Caddy (iç servis, port 8080)
│   ├── Node.js + Astro (statik site build & serve)
│   └── Python FastAPI (CRM, form, teklif, webhook)
│
└── lxc-db            Debian 12 | 1GB | 1 Core | 20GB
    ├── PostgreSQL (tüm veri)
    └── Cron jobs (otomasyon görevleri)

DNS/CDN: Cloudflare (orange cloud — tüm domainler)
E-posta: Zoho Mail Free (5 kullanıcı — dış servis, korunur)
WhatsApp: Meta Cloud API (doğrudan Meta — SaaS değil, altyapı)
```

---

## Trafik Akışı

```
İnternet → Cloudflare (CDN + DDoS + SSL edge)
    ↓
Statik IP → Modem port forward (80/443)
    ↓
lxc-proxy (Caddy — SSL terminasyon)
    ├── parlakbeton.com      → lxc-web-api:8080 (Astro statik)
    ├── api.parlakbeton.com  → lxc-web-api:8000 (FastAPI)
    └── [müşteri domainleri] → lxc-cyberpanel:80
```

---

## E-posta Hesapları

| Adres | Amaç | Gönderim |
|-------|------|---------|
| <erhan.karaman@parlakbeton.com> | Kişisel | Manuel — sistem kullanmaz |
| <bilgi@parlakbeton.com> | Müşteri iletişimi, form yanıtı | FastAPI → Zoho SMTP |
| <teklif@parlakbeton.com> | Teklif gönderimi | Alias → bilgi@ |
| <noreply@parlakbeton.com> | Sistem bildirimleri | Alias → bilgi@ |
| <destek@parlakbeton.com> | Rezerv | - |

SMTP: smtp.zoho.com:587 (TLS) | Kimlik: <bilgi@parlakbeton.com>

---

## Sistem Bileşenleri

### 1. Web Sitesi (Astro)

- **Framework:** Astro (statik)
- **Stil:** Vanilla CSS + Design Tokens (Tailwind YOK — AstroWind YOK)
- **Deploy:** lxc-web-api içinde build → Caddy serve
- **AI yönetimi:** İçerik .md dosyaları, bileşenler .astro — bu proje üzerinden güncellenir

**Sayfalar:**

```
/                         Ana Sayfa
/hizmetler                Hub
/hizmetler/beton-parlatma Detay
/hizmetler/lityum-silikat Detay
/hizmetler/zemin-tamiri   Detay
/projeler                 Referanslar
/hakkimizda               Kurumsal
/iletisim                 Form + Keşif talebi
/blog/[slug]              İçerik (SEO)
```

### 2. CRM (Custom)

- **Veritabanı:** PostgreSQL (lxc-db)
- **API:** FastAPI REST (lxc-web-api)
- **Tablolar:**

```sql
leads          -- Gelen talepler
  id, ad, telefon, email, alan_m2, lokasyon,
  zemin_durumu, tarih_tercihi, kaynak,
  durum (yeni/keşif/teklif/kapandı/iptal),
  created_at, updated_at

projects       -- Aktif / tamamlanan projeler
  id, lead_id, taşeron, başlangıç, bitiş,
  tutar_kdv_haric, tutar_kdv_dahil, durum

proposals      -- Teklifler
  id, lead_id, pdf_path, gönderildi_at,
  tutar, geçerlilik, durum

followups      -- Takip görevleri
  id, lead_id, tarih, not, yapıldı

communications -- Tüm iletişim geçmişi
  id, lead_id, kanal (email/whatsapp/telefon),
  yön (gelen/giden), içerik, tarih
```

### 3. Form & Lead Yakalama

- Web formu → FastAPI endpoint
- Qualifying sorular (alan m², lokasyon, tarih, açıklama)
- Anlık bildirim: WhatsApp (Erhan'a) + e-posta (bilgi@)
- CRM'e otomatik kayıt

### 4. Teklif Sistemi

```
AI (offer-generator skill) → teklif içeriği
    ↓
FastAPI → WeasyPrint → PDF (markalı şablon)
    ↓
Otomatik gönderim:
  → bilgi@ → müşteri e-postası
  → WhatsApp Business API → müşteri telefonu
Süre hedefi: 10 dakika
```

### 5. WhatsApp (MVP → Sonraki Faz Otomasyonu)

**MVP:** Web sitesinde click-to-chat butonu

```
wa.me/+90XXXXXXXXX?text=Merhaba, Parlak Beton uygulaması hakkında bilgi almak istiyorum.
```

Müşteri yazar → Erhan manuel yanıtlar. Sıfır kurulum.

**Sonraki Faz (MVP sonrası):** Meta Cloud API ile tam otomasyon

- Lead bildirimi, teklif gönderimi, takip mesajları
- Gereksinim: Ayrı telefon numarası (prepaid SIM veya Twilio)

### 6. E-posta Otomasyonu (Zoho SMTP)

- Form onayı → müşteriye anlık otomatik yanıt
- Keşif randevusu teyidi
- Teklif gönderimi
- Teslim sonrası bakım rehberi
- 30 gün sonra memnuniyet + review talebi

### 7. Raporlama & Dashboard

- Python script → haftalık rapor e-postası (Erhan'a)
- Lead kaynak analizi
- Dönüşüm hunisi durumu
- Aylık gelir projeksiyonu

---

## Teknoloji Stack (Özet)

| Katman | Teknoloji | Neden |
|--------|-----------|-------|
| Web | Astro (statik) | SEO mükemmel, sıfır JS bloat |
| Backend | Python FastAPI | Hızlı, async, AI entegrasyonu kolay |
| Veritabanı | PostgreSQL | Güvenilir, AI sorgulanabilir |
| Proxy | Caddy | Otomatik SSL, AI-config |
| PDF | WeasyPrint | HTML/CSS → PDF, AI şablon yönetimi |
| E-posta | Zoho SMTP | Deliverability garantili |
| WhatsApp | Meta Cloud API | Resmi, ücretsiz başlangıç |
| DNS/CDN | Cloudflare | Mevcut, orange cloud açık |
| OS | Debian 12 | Kararlı, hafif, LXC ideal |

---

## Geliştirme Yol Haritası

```
FAZ 1 — Altyapı (Hafta 1-2)
  □ lxc-proxy kur, Caddy yapılandır
  □ lxc-web-api kur, Node.js + Python ortamı
  □ lxc-db kur, PostgreSQL başlat
  □ Cloudflare DNS API token al
  □ Müşteri siteleri lxc-proxy üzerinden test et

FAZ 2 — Web Sitesi (Hafta 2-4)
  □ Astro proje yapısı kur
  □ Tasarım sistemi (design tokens, layout)
  □ Ana sayfa + İletişim sayfası
  □ Tüm servis sayfaları
  □ Referanslar + Blog altyapısı
  □ SEO: meta, schema.org, sitemap, robots.txt

FAZ 3 — Backend & CRM (Hafta 4-6)
  □ PostgreSQL şeması kur
  □ FastAPI: lead endpoint
  □ FastAPI: CRM CRUD API
  □ Form → CRM → e-posta + WhatsApp bildirimi
  □ Qualifying form entegrasyonu (web sitesi ↔ API)

FAZ 4 — Teklif Sistemi (Hafta 6-8)
  □ WeasyPrint PDF şablonu (markalı)
  □ FastAPI: /api/proposals endpoint
  □ AI → teklif taslağı → PDF → gönderim
  □ WhatsApp Business API kurulumu + test

FAZ 5 — Otomasyon (Hafta 8-10)
  □ Takip cron jobları (3gün, 7gün, 30gün)
  □ Haftalık rapor e-postası
  □ Lead kaynak takibi
  □ Google Ads entegrasyonu (UTM parametreleri)

FAZ 6 — SEO & Büyüme (Hafta 10-12)
  □ İçerik üretimi (blog makaleleri)
  □ Google Ads kampanya kurulumu
  □ LinkedIn B2B outreach şablonları
  □ Performans ölçümü ve optimizasyon
```

---

## Başarı Kriterleri (12 Ay)

| Metrik | Hedef |
|--------|-------|
| Aylık lead | 15-20 |
| Dönüşüm oranı | %25+ |
| Aylık proje | 3-4 |
| Ortalama proje değeri | 400K-500K ₺ |
| Yıllık ciro | 12-15M ₺ |
| Net kâr | 5M ₺ |
| Lighthouse (mobile) | ≥ 90 |
| Organik trafik (ay) | 2.000+ ziyaret |
| Teklif hazırlama süresi | ≤ 10 dakika |
| Lead yanıt süresi | ≤ 2 saat |
