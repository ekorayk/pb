# Göç Öncesi Arşivleme Kontrol Listesi

# parlakbeton.com → Yeni Astro Site

# YK Kararı: 2026-02-24

---

## 1. TEKNİK ARŞİV (CDO Can)

### 1.1 WordPress Veritabanı Yedeği

```
CyberPanel → Websites → parlakbeton.com → Backup
→ Full Backup (files + database)
→ Tarih etiketiyle kaydet: backup-parlakbeton-2026-02-24.tar.gz
→ Yerel kopyayı F:\code\parlakbeton.com\.agent\archive\wp-backup\ altına al
```

- [ ] CyberPanel backup alındı
- [ ] Yerel kopya indirildi
- [ ] Boyut doğrulandı (bozuk backup riski)

### 1.2 WordPress Medya Dosyaları (Fotoğraf Galerisi)

```
wp-content/uploads/ klasörünü tam olarak indir
→ SCP/SFTP: F:\code\parlakbeton.com\.agent\archive\media\
```

- [ ] Fotoğraflar indirildi
- [ ] Proje fotoğrafları yeni siteye hazırlandı
- [ ] Logo, favicon, marka görselleri ayrıştırıldı

### 1.3 WordPress Tema/Plugin Listesi

- [ ] Aktif tema adı kaydedildi
- [ ] Aktif plugin'ler listesi çıkartıldı (custom widget/shortcode içeriği için)

---

## 2. SEO KORUMA (CMO Serena + CDO Can)

### 2.1 Google Search Console Export

```
GSC → Performans → Son 16 ay → CSV İndir
→ F:\code\parlakbeton.com\.agent\analytics\baseline\search-console.md güncelle
```

- [ ] Son 16 ay trafik verisi export edildi
- [ ] En yüksek trafik alan 20 URL belirlendi
- [ ] Bu URL'ler redirect-map.md'de işaretlendi ✓ (yapıldı)

### 2.2 Google Analytics 4 Export

```
GA4 → Raporlar → Son 12 ay → Sayfalar raporu → CSV
→ .agent/analytics/baseline/analytics.md güncelle
```

- [ ] Sayfa bazlı trafik kaydedildi
- [ ] En yüksek dönüşüm oranı olan sayfalar tespit edildi

### 2.3 Backlink Audit (Ahrefs / Google Search Console)

```
GSC → Bağlantılar → En çok bağlantı verilen sayfalar
→ Hangi dış siteler hangi URL'e bağlantı veriyor?
```

- [ ] Backlinkli sayfalar tespit edildi
- [ ] Bu sayfalar kritik olarak işaretlendi ✓

### 2.4 Mevcut Sayfa Başlıkları ve Meta Açıklamaları

- [ ] Her sayfanın title ve description arşivlendi (→ content/ klasörü)

### 2.5 Schema.org Mevcut Durumu

- [ ] Yoast SEO tarafından eklenen schema'lar tespit edildi
- [ ] LocalBusiness schema var mı? → yeni siteye taşı

---

## 3. İÇERİK ARŞİVİ (CMO Serena + CTO Dr. Emre)

### 3.1 Metin İçerikleri

- [ ] Ana sayfa içeriği kaydedildi → `.agent/archive/content/anasayfa.md`
- [ ] /parlak-beton/ → `.agent/archive/content/parlak-beton.md`
- [ ] /hakkimizda/ → `.agent/archive/content/hakkimizda.md`
- [ ] /iletisim/ → `.agent/archive/content/iletisim.md`
- [ ] /beton-parlatma-referanslari/ → `.agent/archive/content/referanslar.md`
- [ ] Tüm blog yazıları → `.agent/archive/content/blog/`

### 3.2 Referans/Müşteri Yorumları (CSO Mehmet)

- [ ] Akgün Elektrik yorumu metin olarak kaydedildi
- [ ] Garanti İplik yorumu kaydedildi
- [ ] Debak Bağalit yorumu kaydedildi
- [ ] Tüm referans firma logoları indirildi

### 3.3 Teknik Belgeler (CTO Dr. Emre)

- [ ] Parlak Beton broşürü PDF kaydedildi
- [ ] "Mobil Robot Kullanan Fabrikalarda Parlak Beton" PDF kaydedildi
- [ ] SSS içeriği yeni siteye hazırlandı

---

## 4. YASAL ARŞİV (CLO Neslihan)

- [ ] Gizlilik Politikası metni arşivlendi
- [ ] KVKK Aydınlatma metni (varsa) arşivlendi
- [ ] İletişim formu KVKK onay metni arşivlendi
- [ ] Çerez politikası (varsa) arşivlendi

---

## 5. MARKA VARLIK (CMO Serena)

- [ ] Logo (SVG + PNG) indirildi
- [ ] Favicon indirildi
- [ ] Renk kodları tespit edildi (mevcut WordPress temadan)
- [ ] Kullanılan fontlar belirlendi

---

## 6. DIŞ SERVİS KAYITLARI (CDO Can)

### 6.1 Google Hizmetleri

- [ ] Google Search Console mülkiyet kodu not alındı
- [ ] Google Analytics ölçüm ID'si not alındı (G-XXXXXXXX)
- [ ] Google Business Profile güncel mi? → Kontrol et

### 6.2 Cloudflare

- [ ] Mevcut DNS kayıtları export edildi
- [ ] Mevcut Page Rules kayıt edildi
- [ ] Zone ID ve API Token hazırlandı

### 6.3 CyberPanel / Domain

- [ ] Domain kayıt süresi kontrol edildi (ne zaman yenileniyor?)
- [ ] SSL sertifikası durumu kontrol edildi
- [ ] E-posta yapılandırması (MX kayıtları) not alındı

---

## 7. WEB ARŞIV (CDO Can)

### 7.1 Wayback Machine (web.archive.org)

```
https://web.archive.org/save/https://parlakbeton.com/
```

- [ ] Ana sayfa arşivlendi
- [ ] /parlak-beton/ arşivlendi
- [ ] /beton-parlatma-referanslari/ arşivlendi
- [ ] /hakkimizda/ arşivlendi

### 7.2 Ekran Görüntüleri

- [ ] Her kritik sayfa screenshot alındı (desktop + mobile)
- [ ] Tarih damgalı kayıt yapıldı

---

## 8. GEÇIŞ PROTOKOLü (COO Levent + CDO Can)

### Geçiş Günü Plan

```
T-7 gün: Yeni site staging'de hazır ve test edilmiş
T-3 gün: Redirect map Caddy'ye yüklendi (staging test)
T-1 gün: CyberPanel son yedek alındı
T=0 gün (geçiş):
  08:00 → DNS TTL 60 saniyeye indirildi
  09:00 → Yeni site Caddy'de aktif
  09:05 → DNS A kayıtları güncellendi
  09:15 → Yönlendirmeler test edildi (curl -I)
  09:30 → GSC'de yeni sitemap gönderildi
  10:00 → Google Analytics akışı doğrulandı
T+7 gün: İlk GSC crawl raporu incelendi
T+30 gün: Organik trafik karşılaştırması yapıldı
```

### Geri Alma Planı (Rollback)

```
Eğer kritik sorun çıkarsa:
  → DNS TTL düşük olduğu için eski IP'ye 5 dakikada dönülebilir
  → WordPress hâlâ CyberPanel'de çalışıyor (silinmeyecek)
  → 30 gün sonra stabil görüldüğünde WordPress kaldırılacak
```

---

## ÖNEMLİ NOT

WordPress devre dışı bırakılmadan (en az 30 gün) ÖNCE:

- Tüm yönlendirmeler GSC'de hata üretmiyor
- Organik trafik düşüşü yok (±%10 tolerans)
- Core Web Vitals yeni sitede kabul edilebilir durumda
