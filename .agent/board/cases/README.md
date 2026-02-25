# Yönetim Kurulu — Case Management System

Bu klasör, Yönetim Kurulu'na danışılan tüm konuların profesyonel olarak kayıt altına alındığı ve takip edildiği sistemdir.

---

## 📁 Klasör Yapısı

```
.agent/board/cases/
├── active/              # Aktif, uygulanması devam eden case'ler
├── completed/           # Tamamlanan ve kapanan case'ler
├── rejected/            # Reddedilen veya iptal edilen case'ler
└── README.md            # Bu dosya
```

---

## 🔢 Case Numaralandırma

Format: `YK-[YIL]-[SIRA]`

Örnekler:
- `YK-2026-001` → 2026 yılının ilk case'i
- `YK-2026-042` → 2026 yılının 42. case'i

---

## 📋 Case Yaşam Döngüsü

```
1. OLUŞTURULDU
   ↓
   Danışma toplantısı gerçekleşir
   İlgili yöneticiler görüş verir
   ↓
2. KARAR VERİLDİ
   ↓
   ┌─────────────┬──────────────┬─────────────┐
   │             │              │             │
   ONAYLANDI  BEKLEMEDE    REDDEDİLDİ
   │             │              │
   active/    active/      rejected/
   │             │
   Aksiyon planı │ Ek bilgi/karar
   Workflow    │ bekleniyor
   ↓             ↓
   TAMAMLANDI  [cycle continues]
   │
   completed/
```

---

## 📄 Case Dosya Formatı

Her case bir markdown dosyasıdır:

```
YK-2026-001-multimedia-strategy.md
│
├── Header (meta bilgi)
├── Özet
├── Yönetici Görüşleri (tam transcript)
├── Final Karar
├── Aksiyon Planı (TODO listesi)
├── KPI'lar (ölçüm hedefleri)
└── Tarihçe (güncelleme logları)
```

Detaylı template: `CASE_TEMPLATE.md`

---

## 🔄 Workflow Entegrasyonu

Case'ler **onaylandığında** otomatik olarak:

1. ✅ Aksiyonlar `/workflows/` klasörüne taşınır
2. ✅ Sorumlu departmanlar bilgilendirilir (dosyalarına referans eklenir)
3. ✅ KPI takip sistemi aktive edilir
4. ✅ Deadline reminder sistemine eklenir

---

## 📊 Case Durumları

| Durum | Icon | Klasör | Anlamı |
|-------|------|--------|--------|
| **Draft** | 📝 | active/ | Case açıldı, henüz tamamlanmadı |
| **Under Review** | 🔍 | active/ | YK görüşleri alınıyor |
| **Approved** | ✅ | active/ | Onaylandı, aksiyonlar başladı |
| **On Hold** | ⏸️ | active/ | Askıya alındı (geçici) |
| **Completed** | ✔️ | completed/ | Tamamlandı ve kapatıldı |
| **Rejected** | ❌ | rejected/ | Reddedildi veya iptal edildi |

---

## 🎯 Hızlı Komutlar

```bash
# Yeni case oluştur
/yk [konu]                    → Otomatik case açılır

# Case durumu güncelle
# (Manuel: case dosyasını edit et, Status: alanını değiştir)

# Aktif case'leri listele
ls .agent/board/cases/active/

# Tamamlanan case'leri listele
ls .agent/board/cases/completed/
```

---

## 📈 Raporlama

### Aylık YK Raporu

```bash
# Ay sonunda otomatik üretilir:
.agent/board/reports/2026-02-monthly-summary.md

İçerik:
- Açılan case sayısı
- Onaylanan/reddedilen case'ler
- Tamamlanan aksiyonlar
- KPI başarı oranları
```

---

## 🔐 Veri Yönetimi

- Tüm case'ler **git ile versiyon kontrolü** altında
- Hassas bilgi içeren case'ler `.gitignore` ile korunabilir
- Case'ler **markdown formatında** → okunabilir, aranabilir

---

## 📚 İlgili Dosyalar

- Case Template: `CASE_TEMPLATE.md`
- Workflow şablonları: `.agent/board/workflows/`
- Yönetici profilleri: `.agent/board/[KOD].md`
- Genel YK bilgisi: `CLAUDE.md` (root)

---

**Son Güncelleme:** 2026-02-25
**Sistem Versiyonu:** 1.0
