# Deploying to a VPS

Target: one small Ubuntu 24.04 server (1 vCPU, 2 GB RAM is plenty) running Docker and Caddy.
The container image is built by GitHub Actions and published to GitHub Container Registry
(GHCR) on every push to `main` and on the first of each month.

## One-off server setup

```bash
# as root on the new server
apt update && apt install -y ca-certificates curl
curl -fsSL https://get.docker.com | sh
apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
apt update && apt install -y caddy

mkdir -p /opt/ccdash && cd /opt/ccdash
# copy deploy/docker-compose.yml here, then:
docker compose pull && docker compose up -d

# copy deploy/Caddyfile to /etc/caddy/Caddyfile, edit the hostname, then:
systemctl reload caddy
```

Point the domain's A record at the server before reloading Caddy so the certificate
request succeeds.

## Image visibility

The repository is private, so GHCR makes the package private too. Either:

- make the package public (GitHub: Packages, carrying-capacity-dashboard, Package settings,
  Change visibility), which is fine because the app itself is public; or
- `docker login ghcr.io` on the server with a personal access token that has `read:packages`.

## Updating

Push to `main`. When the Action finishes, on the server:

```bash
cd /opt/ccdash && docker compose pull && docker compose up -d
```

Rollback: `docker compose up -d` with the image tag changed to a previous run number
(every build is also tagged with its run number and commit SHA).

## Running locally without Docker

```bash
mvn package
# copy target/ROOT.war into any Tomcat 9 webapps/ directory and start Tomcat
```
