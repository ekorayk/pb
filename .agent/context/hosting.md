# Hosting & Altyapı Bilgileri

> ⚠️ Şifre ve hassas bilgileri bu dosyaya YAZMAYIN. `.env` veya şifre yöneticisi kullanın.

---

## Fiziksel Altyapı

| Alan | Değer |
|------|-------|
| **Sunucu Tipi** | Self-hosted / On-premise |
| **Hypervisor** | Proxmox VE |
| **Donanım** | 6GB RAM / 4 Core CPU |
| **İnternet** | Fiber 100Mbps down / 50Mbps up |
| **IP** | Statik IP (modem → Proxmox ağı) |
| **DNS / CDN** | Cloudflare (tüm domainler) |

---

## LXC Mimarisi (Hedef)

| LXC | OS | RAM | Rol |
|-----|----|-----|-----|
| `lxc-cyberpanel` | Ubuntu (mevcut) | ~2.5GB | CyberPanel — müşteri siteleri + e-posta geçiş |
| `lxc-proxy` | Debian 12 | 256MB | Caddy — master reverse proxy / SSL |
| `lxc-web-api` | Debian 12 | 1.5GB | Astro + FastAPI (CRM, form, teklif) |
| `lxc-db` | Debian 12 | 1GB | PostgreSQL + cron otomasyonu |

### Trafik Akışı

```
İnternet → Cloudflare → Statik IP → Modem (80/443)
    ↓
lxc-proxy (Caddy)
    ├── parlakbeton.com     → lxc-web-api:8080
    ├── [diğer domainler]   → lxc-cyberpanel
    └── [gelecek projeler]  → lxc-yeni
```

---

## Domain & DNS

| Alan | Değer |
|------|-------|
| **Ana Domain** | parlakbeton.com |
| **DNS Yönetimi** | Cloudflare |
| **SSL** | Caddy (Let's Encrypt otomatik) |
| **MX Kayıtları** | Zoho Mail (değiştirilmeyecek) |

---

## E-posta Sistemi

| Alan | Değer |
|------|-------|
| **Sağlayıcı** | Zoho Mail Free (5 kullanıcı) |
| **Aktif Adresler** | <erhan.karaman@parlakbeton.com> |
| **Alias** | <info@parlakbeton.com> → erhan.karaman@ yönlendirilmiş |
| **SMTP (Otomasyon için)** | smtp.zoho.com:587 (TLS) |
| **Kimlik** | <erhan.karaman@parlakbeton.com> |
| **Şifre** | → `.env` dosyasından okunacak |

### Otomasyon E-posta Kullanımı

```python
# lxc-web-api içinde FastAPI → Zoho SMTP
SMTP_HOST = "smtp.zoho.com"
SMTP_PORT = 587
SMTP_USER = "erhan.karaman@parlakbeton.com"
SMTP_PASS = env("ZOHO_SMTP_PASS")  # .env'den
FROM_NAME = "Parlak Beton"
```

---

## Mevcut Durum (Geçiş Öncesi)

| Alan | Durum |
|------|-------|
| Web sitesi | WordPress (The7 tema) — CyberPanel üzerinde |
| WP SMTP | ❌ Bozuk (Zoho kimlik doğrulama hatası) |
| Google Analytics | ✅ GA4 bağlı |
| Search Console | ✅ Bağlı ve doğrulanmış |
| Cloudflare | ✅ Aktif |
| CyberPanel | ✅ Çalışıyor |

---

## Güvenlik Notları

- CyberPanel paneli Cloudflare'de `proxy: off` (gray cloud) yapılmamalı
- lxc-cyberpanel dışarıya direkt açık olmamalı — trafik lxc-proxy üzerinden geçmeli
- SSH erişimi yalnızca yerel ağ veya VPN üzerinden
- `.env` dosyaları asla Git'e eklenmeyecek
