# Useful Services

## Some information about repository and preparations
This repository provides Docker Compose configurations to deploy several <br>
useful self-hosted services.

> I use this on my VPS (OS: Ubuntu 22.04 | 12 vCores CPU | 24GB RAM | 720 GB NVMe) <br>
This guide may not be suitable for you if there are significant differences in <br>
operating systems, software versions, etc. I plan to add various guides and <br>
configuration templates for other systems or situations <br>
(for example, using Let's Encrypt instead of certificates and keys).

> Make sure, you have a correct and official version of Docker Engine.<br>
> You can install it following [this guide](https://docs.docker.com/engine/install/)<br>
> There are docs for [Immich](https://immich.app/docs/overview/welcome/), 
> [AFFiNE](https://docs.affine.pro/self-host-affine/) and
> [GitLab](https://docs.gitlab.com/install/docker/)

## Services

| Service   | Subdomain           | Description                         |
| --------- |---------------------| ----------------------------------- |
| GitLab CE | `git.example.com`   | Git hosting and DevOps platform     |
| WireGuard | `vpn.example.com`   | VPN access via `wg-easy`            |
| Immich    | `media.example.com` | Self-hosted photo and video manager |
| AFFiNE    | `notes.example.com` | Note-taking and documentation tool  |
---
## Structure

> `Storage` is only relevant if the location environment variables have not been changed.

```
useful-services/
├── .gitignore
├── LICENSE
├── README.md
└── services/
    ├── caddy/
    │   ├── Caddyfile
    │   ├── certs/
    │   │   ├── fullchain.crt
    │   │   └── private.key
    │   ├── config/
    │   └── data/
    ├── docker-compose.yml
    ├── .env
    ├── hash_gen.py
    └── storage/                        | Will be created after services are started
        ├── affine/                     | Will be created after services are started
        │   ├── config/                 | Will be created after services are started
        │   ├── postgres/               | Will be created after services are started
        │   │   └── pgdata/             | Will be created after services are started
        │   └── storage/                | Will be created after services are started
        ├── gitlab/                     | Will be created after services are started
        │   ├── config/                 | Will be created after services are started
        │   ├── data/                   | Will be created after services are started
        │   └── logs/                   | Will be created after services are started
        ├── immich/                     | Will be created after services are started
        │   ├── library/                | Will be created after services are started
        │   └── postgres/               | Will be created after services are started
        └── wg-config/                  | Will be created after services are started
```
---
## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DanyloH-01/useful-services.git
cd useful-services
```

### 2. Configure environment variables, docker-compose and Caddyfile

You must replace `example.com` in the `Caddyfile` and .env-files with your domain.

Edit environment variables in `.env` file.

Do not delete `deploy`-block in GitLab. This may result in loss of RAM!<br>
If necessary, add a deploy-block to other services for resource limitation/reservation

### 3. Generate a hashed password for WireGuard

Use the included `hash_gen.py` script:

```bash
python3 hash_gen.py
```

Paste the resulting hash into the `WG_PASSWORD_HASH` field in `wire-guard.env`.

### 4. Configure DNS

Point your subdomains to your machine's IP address if necessary:

* `git.example.com`
* `vpn.example.com`
* `immich.example.com`
* `affine.example.com`

### 5. Configure SSL/TLS Certification

> You have to download SSL-Certificate and your private.key by your provider. <br>
> Store it in `/useful-services/caddy/certs/`. Be careful with the names of your <br>
> certificate and key. It should be either the same as in the Caddyfile or you must <br>
> change references in the Caddyfile.

Caddy is used as a reverse proxy and certification manager.
Ensure that ports 80 and 443 are open. Configuration can be found in:

```
caddy/Caddyfile
```
Update it to match your domain setup if necessary.

### 6.Check syntax

```bash
docker compose config
```

---
## Start the stack

```bash
docker compose up -d
```
---

## UPDATE / UPGRADE

```bash
docker compose down
#Wait until all containers are stopped and removed
docker compose pull
```

## License

This project is licensed under the MIT License. Use, modify, and distribute it freely.

## Contributions

Feel free to open an issue or submit a pull request to contribute or report bugs.
