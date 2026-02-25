# Yönetim Kurulu — Case Management System

**Versiyon:** 1.0
**Tarih:** 2026-02-25
**Durum:** ✅ Aktif

---

## 🎯 Sistem Amacı

Yönetim Kurulu'na danışılan **her konunun profesyonel olarak** kayıt altına alınması, aksiyon planlarının takip edilmesi ve iş akışına entegrasyonu.

---

## 📦 Sistem Bileşenleri

```
.agent/board/
├── cases/                  # Case dosyaları
│   ├── active/            # Aktif case'ler
│   ├── completed/         # Tamamlanan
│   ├── rejected/          # Reddedilen
│   ├── README.md          # Case sistemi kılavuzu
│   └── CASE_TEMPLATE.md   # Standart case şablonu
│
├── workflows/             # Onaylanan case'lerin aksiyon takibi
│   ├── README.md
│   └── YK-[no]-workflow.md
│
├── [KOD].md               # Yönetici persona dosyaları
│   ├── CEO.md
│   ├── CFO.md
│   ├── CMO.md
│   └── ...
│
└── CASE_SYSTEM.md         # Bu dosya (sistem özeti)
```

---

## 🔄 Case Akışı

### 1. Case Açılışı

Kullanıcı `/yk [konu]` komutunu çalıştırdığında:

```
1. Yeni case numarası üretilir (YK-YYYY-NNN)
2. İlgili yöneticiler belirlenir
3. Her yönetici görüşünü sunar
4. Case dosyası oluşturulur (cases/active/)
```

### 2. Karar Aşaması

```
CEO + İlgili Yöneticiler
    ↓
Karar: ONAYLANDI / REDDEDİLDİ / BEKLEMEDE
    ↓
Case durumu güncellenir
```

### 3. Onaylanan Case → Workflow

```
Aksiyon planı çıkarılır
    ↓
Workflow dosyası oluşturulur (workflows/)
    ↓
Departmanlara atanır
    ↓
KPI tracking başlar
```

### 4. Takip & Güncelleme

```
Aylık/haftalık progress update
    ↓
KPI'lar ölçülür
    ↓
Milestone'lar izlenir
    ↓
Deadline reminder'lar
```

### 5. Kapanış

```
Tüm aksiyonlar tamamlandı
    ↓
Final KPI raporu
    ↓
Case → completed/ klasörüne taşınır
    ↓
Lessons learned kaydedilir
```

---

## 📋 Case Durumları

| Durum | Icon | Açıklama |
|-------|------|----------|
| **Draft** | 📝 | Açıldı, görüşler alınıyor |
| **Under Review** | 🔍 | YK inceliyor |
| **Approved** | ✅ | Onaylandı, aksiyonlar başladı |
| **On Hold** | ⏸️ | Askıya alındı |
| **Completed** | ✔️ | Tamamlandı |
| **Rejected** | ❌ | Reddedildi/iptal |

---

## 🎯 Kullanım Senaryoları

### Senaryo 1: Basit Danışma

```bash
Kullanıcı: /yk fiyat artışı CFO CSO

→ CFO ve CSO görüş verir
→ Case açılır ama workflow'a girmez (bilgilendirme amaçlı)
→ cases/completed/ klasöründe arşivlenir
```

### Senaryo 2: Onaylanan Strateji

```bash
Kullanıcı: /yk yeni hizmet lansmanı

→ Tüm ilgili yöneticiler görüş verir
→ CEO onaylar
→ Case açılır + Workflow oluşturulur
→ Departmanlara aksiyonlar atanır
→ Aylık takip başlar
→ 6. ay review → Case tamamlanır
```

### Senaryo 3: Reddedilen Öneri

```bash
Kullanıcı: /yk [bir öneri]

→ Yöneticiler görüş verir
→ CEO red eder (risk/maliyet/öncelik)
→ Case → rejected/ klasörüne taşınır
→ Red gerekçesi kaydedilir
```

---

## 🚀 Otomatik Entegrasyonlar

### 1. Departman Bilgilendirme

Onaylanan case'de CMO'ya aksiyon düştüğünde:
- CMO.md dosyasına referans eklenir
- Aktif case listesi güncellenir

### 2. Deadline Reminder

```
Deadline - 3 gün → Warning
Deadline günü → Alert
Deadline geçti → Eskalasyon (CEO bilgilendirme)
```

### 3. KPI Dashboard

Her case için:
- Aylık KPI tracking
- Progress bar
- Risk değerlendirmesi

---

## 📊 Raporlama

### Aylık YK Raporu

```markdown
# Yönetim Kurulu — Aylık Özet (Şubat 2026)

## Case İstatistikleri
- Açılan: 5
- Onaylanan: 3
- Reddedilen: 1
- Devam eden: 4

## Departman Performansı
- CMO: 3/4 aksiyon tamamlandı (%75)
- CDO: 2/3 aksiyon tamamlandı (%67)
- CFO: 5/5 aksiyon tamamlandı (%100) ⭐

## KPI Başarı
- Hedeflere ulaşılan case: 2/3 (%67)
- Geciken aksiyon: 1
- Bütçe adherence: %98
```

---

## 🛠️ Bakım & İyileştirme

### Haftalık

- Aktif case'lerde progress update
- Deadline yaklaşan aksiyonları kontrol

### Aylık

- KPI raporu üretimi
- Risk değerlendirmesi
- Lesson learned kaydı

### Çeyreklik

- Case sistemi review (süreç iyileştirme)
- Template güncelleme (gerekirse)
- Departman feedback toplama

---

## 📚 Hızlı Referans

| İşlem | Komut / Yol |
|-------|-------------|
| **Yeni case aç** | `/yk [konu]` |
| **Case listesi** | `ls .agent/board/cases/active/` |
| **Workflow görüntüle** | `cat .agent/board/workflows/YK-[no]-workflow.md` |
| **Template kullan** | `cp CASE_TEMPLATE.md active/YK-[no]-[slug].md` |
| **KPI güncelle** | Workflow dosyasındaki tabloyu düzenle |

---

## 🎓 En İyi Pratikler

1. **Her danışma = Case:** Küçük bile olsa kayıt tut
2. **Standart format:** Template'den sapma
3. **Düzenli güncelleme:** Progress log boş kalmasın
4. **Şeffaflık:** Tüm yönetici görüşleri tam olarak kayda geçsin
5. **Ölçülebilirlik:** Her case için somut KPI tanımla
6. **Kapanış disiplini:** Tamamlanan case'leri completed/'a taşı

---

## 📞 Destek

Sistem hakkında sorular:
- CDO (Can Erdoğan) — Teknik
- CEO (Alexander Kaya) — Süreç & protokol

---

**Sistem Kurulumu:** 2026-02-25
**İlk Case:** YK-2026-001 (Multimedia Strategy)
**Aktif Case Sayısı:** 1
**Sistem Durumu:** ✅ Operasyonel
