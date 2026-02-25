# Workflow Entegrasyon Sistemi

YK case'lerinden **onaylanan aksiyonların** iş akışına otomatik entegrasyonu.

---

## 🔄 Nasıl Çalışır?

```
Case ONAYLANDI
    ↓
Aksiyon Planı Oluşturuldu
    ↓
Workflow Dosyası Üretildi (.agent/board/workflows/[case-no].md)
    ↓
İlgili Departman Dosyalarına Referans Eklendi
    ↓
Todo/Reminder Sistemi Aktive Edildi
```

---

## 📁 Workflow Dosya Formatı

Her onaylanan case için bir workflow dosyası:

```
YK-2026-001-workflow.md
│
├── Case özeti (bağlantılı)
├── Aksiyon listesi (departman bazlı)
├── Deadline timeline
├── KPI tracking tablosu
└── Progress update log
```

---

## 🎯 Departman Entegrasyonu

Workflow oluşturulduğunda, ilgili departman dosyalarına **otomatik referans** eklenir:

### Örnek: CMO Dosyasına Eklenen Referans

```markdown
## 📋 Aktif Case'ler

- [YK-2026-001: Multimedia Strategy](.agent/board/cases/active/YK-2026-001-multimedia-strategy.md)
  - **Sorumlu Aksiyon:** 3 pilot konu seç + içerik takvimi
  - **Deadline:** 2026-03-01
  - **Durum:** ⏳ Bekliyor
```

---

## ⏰ Reminder Sistemi

Workflow'daki her aksiyon için:

1. **Deadline yaklaşırken (3 gün kala):** Hatırlatma
2. **Deadline günü:** Acil uyarı
3. **Deadline geçerse:** Eskalasyon (CEO bilgilendirme)

---

## 📊 Progress Tracking

Her workflow dosyası şunları takip eder:

```markdown
## Progress

| Aksiyon | Durum | Tamamlanma % | Son Güncelleme |
|---------|-------|--------------|----------------|
| Aksiyon 1 | 🔄 Devam Ediyor | 60% | 2026-02-28 |
| Aksiyon 2 | ⏳ Bekliyor | 0% | 2026-02-25 |
```

---

## 🚀 Örnek Workflow

Detaylı örnek: `YK-2026-001-workflow.md`

---

**Son Güncelleme:** 2026-02-25
