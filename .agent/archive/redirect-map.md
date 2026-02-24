# Yönlendirme Haritası (Redirect Map)

# Eski parlakbeton.com → Yeni Astro site

# Caddy config formatında — copy-paste hazır

## Caddy Redirect Konfigürasyonu

```caddyfile
# /etc/caddy/redirects.caddy
# parlakbeton.com yönlendirmeleri
# Bu dosya Caddyfile'a import edilir: import /etc/caddy/redirects.caddy

# ─── KRİTİK SAYFALAR (301 Permanent) ────────────────────────────
redir /parlak-beton/ /beton-parlatma/ 301
redir /parlak-beton  /beton-parlatma/ 301

redir /beton-parlatma-fiyatlari/ /beton-parlatma/fiyatlari/ 301
redir /beton-parlatma-fiyatlari  /beton-parlatma/fiyatlari/ 301

redir /ankara-beton-parlatma/ /beton-parlatma/ankara/ 301
redir /ankara-beton-parlatma  /beton-parlatma/ankara/ 301

redir /beton-parlatma-uygulamasi-fiyatlar/ /blog/beton-parlatma-uygulamasi-fiyatlar/ 301
redir /beton-parlatma-referanslari/ /referanslar/ 301

# ─── HIZMET SAYFALARI ────────────────────────────────────────────
redir /mobil-robotlar-icin-ozellestirilmis-zemin/ /hizmetler/mobil-robot-zemin/ 301
redir /endustriyel-tasiyicilar-ve-parlak-beton-zemin-cozumleri/ /hizmetler/endustriyel-tasiyici-zemin/ 301
redir /epoksi-zemin-bakimi/ /blog/epoksi-zemin-bakimi/ 301

# ─── KURUMSAL SAYFALAR ───────────────────────────────────────────
redir /hakkimizda/galeri/ /galeri/ 301
redir /gizlilik-politikasi/ /gizlilik-politikasi/ 301

# ─── BLOG YAZILARI ───────────────────────────────────────────────
redir /beton-parlatma-blog/ /blog/ 301
redir /beton-parlatma-makinesi/ /blog/beton-parlatma-makinesi/ 301
redir /beton-parlatma-makinesi-nasil-calisir/ /blog/beton-parlatma-makinesi-nasil-calisir/ 301
redir /talasli-imalat-beton-parlatma/ /blog/talasli-imalat-beton-parlatma/ 301
redir /beton-parlatma-sivi-yalitimi/ /blog/beton-parlatma-sivi-yalitimi/ 301
redir /fabrikalarda-kaymaz-zeminlerin-onemi-ve-parlak-beton-uygulamasi/ /blog/kaymaz-zemin-parlak-beton/ 301
redir /mobil-robot-zemin-secimi/ /blog/mobil-robot-zemin-secimi/ 301
redir /istanbulda-fabrika-zemini-uygulamasi/ /blog/istanbul-fabrika-zemini/ 301
redir /parlak-beton-fabrikalar-icin-ekonomik-avantajlarin-anahtari/ /blog/parlak-beton-ekonomik-avantajlar/ 301
redir /beton-nedir-modern-insaatin-temeli/ /blog/beton-nedir/ 301
redir /endustriyel-fabrika-zeminlerinin-uretim-kalitesine-etkisi-stratejik-bir-bakis/ /blog/fabrika-zemin-uretim-kalitesi/ 301
redir /elektrik-ve-enerji-sektoru-icin-ozel-zemin-cozumleri/ /blog/elektrik-enerji-zemin/ 301
redir /beton-parlatma-endustriyel-zeminlerin-yeniden-dogusu/ /blog/endustriyel-zemin-yenileme/ 301
redir /guc-transformatoru-uretim-tesisleri-icin-dayanikli-zemin-cozumleri/ /blog/transformator-tesisi-zemin/ 301
redir /mobil-robotlarin-performansini-artiran-zemin-cozumleri/ /blog/mobil-robot-performans-zemin/ 301
redir /beton-parlatma-uygulamasinin-cesitli-kullanim-alanlari/ /blog/beton-parlatma-kullanim-alanlari/ 301

# ─── TESTİMONİALS (WordPress özel tip) → Referanslar ────────────
redir /dt_testimonials/ /referanslar/ 301
redir /dt_testimonials/akgun-elektrik/ /referanslar/ 301
redir /dt_testimonials/garanti-iplik/ /referanslar/ 301
redir /dt_testimonials/debag-bagalit/ /referanslar/ 301
redir /dt_testimonials/diana-richards/ /referanslar/ 301

# ─── GALERİ ──────────────────────────────────────────────────────
redir /dt_gallery/ /galeri/ 301
redir /dt_gallery/fotograf-galerimiz/ /galeri/ 301

# ─── WORDPRESS ÖZEL URL'LER ──────────────────────────────────────
redir /wp-admin/* /404 302
redir /wp-login.php /404 302
redir /wp-content/* /404 302
redir /?p=* / 301
```

---

## Nginx Alternatif Format

```nginx
# /etc/nginx/redirects.conf (alternatif)

# Kritik sayfalar
rewrite ^/parlak-beton/?$ /beton-parlatma/ permanent;
rewrite ^/beton-parlatma-fiyatlari/?$ /beton-parlatma/fiyatlari/ permanent;
rewrite ^/ankara-beton-parlatma/?$ /beton-parlatma/ankara/ permanent;

# WordPress testimonials → referanslar
rewrite ^/dt_testimonials/.*$ /referanslar/ permanent;
rewrite ^/dt_gallery/.*$ /galeri/ permanent;

# WordPress admin engelle
rewrite ^/wp-(admin|login|content)/.*$ /404 last;
```

---

## Yönlendirme Doğrulama (Deploy Sonrası)

```bash
# Her kritik URL için test et
curl -I https://parlakbeton.com/parlak-beton/
# Beklenen: HTTP/2 301, Location: /beton-parlatma/

curl -I https://parlakbeton.com/beton-parlatma-fiyatlari/
# Beklenen: HTTP/2 301, Location: /beton-parlatma/fiyatlari/

curl -I https://parlakbeton.com/dt_testimonials/akgun-elektrik/
# Beklenen: HTTP/2 301, Location: /referanslar/
```

---

## ÖNEMLİ: Google Search Console Bildirimi

Yeni site yayına girdikten sonra:

1. GSC → Kaldırma Aracı → Eski WordPress URL'leri bildirme (gerekli değil, yönlendirme yeterli)
2. GSC → Sitemap → Yeni sitemap.xml gönder
3. GSC → URL Denetleme → Kritik sayfaları elle yeniden taramaya gönder
