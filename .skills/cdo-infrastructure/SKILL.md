---
name: cdo-infrastructure
description: Use when setting up, configuring, or troubleshooting Proxmox LXC containers, Caddy reverse proxy, Debian 12 server, FastAPI deployment, PostgreSQL setup, or any infrastructure task for Parlak Beton's self-hosted system. Activate with keywords like "LXC kur", "Caddy config", "Proxmox", "Debian", "sunucu kurulumu", "deployment", "nginx", "altyapı", "CDO infra".
---

# CDO Infrastructure — Parlak Beton Self-Hosted Altyapı

## Proxmox LXC Kurulum Rehberi

### LXC-PROXY Kurulumu (Caddy Master Gateway)

```bash
# Proxmox web UI → Create CT
# Template: debian-12-standard
# CT ID: 200 (örnek)
# Hostname: lxc-proxy
# RAM: 256MB | CPU: 1 core | Disk: 10GB
# Network: vmbr0 | IP: 192.168.1.200/24 | GW: 192.168.1.1

# LXC içinde (console):
apt update && apt upgrade -y
apt install -y curl wget gnupg2

# Caddy kurulum
apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
  | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
  | tee /etc/apt/sources.list.d/caddy-stable.list
apt update && apt install caddy -y

# Caddy Cloudflare DNS plugin (Cloudflare proxy arkası için)
apt install -y xcaddy
xcaddy build --with github.com/caddy-dns/cloudflare
mv caddy /usr/bin/caddy
```

### Caddyfile Şablonu (lxc-proxy)

```caddyfile
# /etc/caddy/Caddyfile

{
    email bilgi@parlakbeton.com
}

# Parlak Beton ana site
parlakbeton.com, www.parlakbeton.com {
    tls {
        dns cloudflare {env.CLOUDFLARE_API_TOKEN}
    }
    reverse_proxy 192.168.1.201:8080
}

# Parlak Beton API
api.parlakbeton.com {
    tls {
        dns cloudflare {env.CLOUDFLARE_API_TOKEN}
    }
    reverse_proxy 192.168.1.201:8000
}

# Müşteri siteleri → CyberPanel
musteri1.com, www.musteri1.com {
    tls {
        dns cloudflare {env.CLOUDFLARE_API_TOKEN}
    }
    reverse_proxy 192.168.1.100:80
}
```

```bash
# /etc/caddy/cloudflare.env
CLOUDFLARE_API_TOKEN=your_token_here

# Servis başlatma
systemctl enable caddy
systemctl start caddy
```

---

### LXC-WEB-API Kurulumu

```bash
# Proxmox: CT ID 201 | Hostname: lxc-web-api
# RAM: 1.5GB | CPU: 2 core | Disk: 20GB

apt update && apt upgrade -y
apt install -y curl wget git python3 python3-pip python3-venv

# Node.js (Astro build için)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs

# Python ortamı
python3 -m venv /opt/parlakbeton/venv
source /opt/parlakbeton/venv/bin/activate
pip install fastapi uvicorn[standard] psycopg2-binary python-dotenv \
            weasyprint pydantic[email] python-multipart slowapi emails

# Astro site klasörü
mkdir -p /var/www/parlakbeton
# Deploy: rsync/scp ile dist/ klasörü buraya kopyalanır
```

### FastAPI Systemd Servisi

```ini
# /etc/systemd/system/parlakbeton-api.service
[Unit]
Description=Parlak Beton FastAPI
After=network.target

[Service]
Type=exec
User=www-data
WorkingDirectory=/opt/parlakbeton
EnvironmentFile=/opt/parlakbeton/.env
ExecStart=/opt/parlakbeton/venv/bin/uvicorn main:app \
          --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl enable parlakbeton-api
systemctl start parlakbeton-api
```

---

### LXC-DB Kurulumu (PostgreSQL)

```bash
# Proxmox: CT ID 202 | Hostname: lxc-db
# RAM: 1GB | CPU: 1 core | Disk: 20GB

apt update && apt upgrade -y
apt install -y postgresql postgresql-contrib python3 python3-pip

# PostgreSQL yapılandırma
systemctl enable postgresql
systemctl start postgresql

# Veritabanı ve kullanıcı oluşturma
sudo -u postgres psql <<EOF
CREATE DATABASE parlakbeton;
CREATE USER pb_app WITH ENCRYPTED PASSWORD 'GÜÇLÜ_ŞİFRE';
GRANT ALL PRIVILEGES ON DATABASE parlakbeton TO pb_app;
\q
EOF

# Uzak bağlantı için
echo "host parlakbeton pb_app 192.168.1.201/32 scram-sha-256" \
  >> /etc/postgresql/15/main/pg_hba.conf

# postgresql.conf
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '192.168.1.202'/" \
  /etc/postgresql/15/main/postgresql.conf

systemctl restart postgresql
```

### Cron Görevleri (lxc-db)

```bash
# /etc/cron.d/parlakbeton
# Haftalık analytics raporları (Her Pazartesi 08:00)
0 8 * * 1 pb_app /opt/analytics/venv/bin/python /opt/analytics/pagespeed.py
0 9 * * 1 pb_app /opt/analytics/venv/bin/python /opt/analytics/search_console.py
0 10 * * 1 pb_app /opt/analytics/venv/bin/python /opt/analytics/ga4.py

# Günlük DB backup (03:00)
0 3 * * * root pg_dump -U pb_app parlakbeton | gzip > /backup/db-$(date +\%Y\%m\%d).sql.gz
```

---

## Deployment Protokolü (Her Güncelleme)

```bash
# Windows geliştirme makinesinden:
# 1. Astro build
npm run build

# 2. lxc-web-api'ye gönder (SSH key gerekli)
rsync -avz --delete dist/ pb_user@192.168.1.201:/var/www/parlakbeton/

# 3. FastAPI güncelleme varsa
rsync -avz api/ pb_user@192.168.1.201:/opt/parlakbeton/
ssh pb_user@192.168.1.201 "systemctl restart parlakbeton-api"

# 4. Doğrulama
curl -I https://parlakbeton.com
```

---

## Network Topolojisi

```
İnternet
    ↓
Cloudflare (CDN + DDoS + SSL edge termination)
    ↓
Statik IP (modem)
    ↓ port forward 80/443
Proxmox vmbr0 ağı
    ↓
lxc-proxy (192.168.1.200) — Caddy
    ├── parlakbeton.com → lxc-web-api (192.168.1.201:8080)
    ├── api.parlakbeton.com → lxc-web-api (192.168.1.201:8000)
    └── [müşteri domainleri] → lxc-cyberpanel (192.168.1.100:80)

lxc-web-api (192.168.1.201)
    └── PostgreSQL → lxc-db (192.168.1.202:5432)
```
