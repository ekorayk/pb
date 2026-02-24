# Cloudflare Analytics Baseline — parlakbeton.com

# Tarih: 2026-02-24 (Proje başlangıcı)

## Nasıl Doldurulur

Cloudflare Dashboard → parlakbeton.com → Analytics & Logs
→ Traffic → Son 30 gün

---

## Trafik Metrikleri (Son 30 Gün)

| Metrik | Değer |
|--------|-------|
| Toplam İstek | — |
| Benzersiz Ziyaretçi | — |
| Önbelleğe Alınan İstek % | — |
| Toplam Veri Transferi | — |
| Engellenen İstek (Güvenlik) | — |

---

## Coğrafi Dağılım (Top 5)

| Ülke | İstek % |
|------|---------|
| Türkiye | — |
| Diğer | — |

---

## Bot vs İnsan Trafik

| Tip | % |
|-----|---|
| İnsan | — |
| Bot | — |

---

## Güvenlik Olayları

| Tip | Sayı |
|-----|------|
| DDoS engelleme | — |
| Kötü bot engelleme | — |
| Firewall kuralı tetikleme | — |

---

## Cloudflare Ayar Kontrol Listesi

- [ ] SSL/TLS modu: Full (Strict)
- [ ] Always Use HTTPS: Açık
- [ ] HTTP/3 (QUIC): Açık
- [ ] Rocket Loader: Açık (WordPress ile dikkatli)
- [ ] Brotli sıkıştırma: Açık
- [ ] Cache TTL: Statik dosyalar 1 ay
- [ ] Page Rules: iletisim sayfası cache yok (form için)

---

## Notlar

Yeni Astro site kurulunca Cloudflare önbellek ayarları güncellenecek.
Astro statik → agresif cache → performans maksimum.
