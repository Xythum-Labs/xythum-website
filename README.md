# Xythum website

[![Deploy website](https://github.com/Xythum-Labs/xythum-website/actions/workflows/pages.yml/badge.svg)](https://github.com/Xythum-Labs/xythum-website/actions/workflows/pages.yml)

The official website source for Xythum Labs: private cross-chain execution infrastructure for protected intent, distributed coordination, and verifiable settlement.

## Project structure

- `dist/` contains the complete static website and all 23 routes.
- `dist/app.js` contains the interactive website content and behavior.
- `dist/styles.css` contains the visual system and responsive layout.
- `generate_seo.py` regenerates route HTML, canonical metadata, structured data, the sitemap, robots policy, and the web manifest.
- `.github/workflows/pages.yml` validates and deploys `dist/` through GitHub Pages.
- `DEPLOYMENT.md` contains the production-domain and DNS runbook.

## Run locally

```bash
python generate_seo.py
python -m http.server 4173 --directory dist
```

Open `http://127.0.0.1:4173`.

To generate metadata for another deployment origin:

```bash
SITE_URL=https://preview.example.com ASSET_VERSION=preview python generate_seo.py
```

PowerShell equivalent:

```powershell
$env:SITE_URL='https://preview.example.com'
$env:ASSET_VERSION='preview'
python generate_seo.py
```

## Deployment

Every push to `main` runs syntax, route-count, and sitemap validation before deploying the static `dist/` directory. Production metadata is generated for `https://xythum.io`, keeping the repository independent from any temporary hosting URL.

Read [DEPLOYMENT.md](DEPLOYMENT.md) before changing DNS. The current domain uses Hostinger nameservers and Zoho Mail records, so an unplanned nameserver change could interrupt email.

## Content provenance

Claims about protocol status, awards, source repositories, and research are linked to public evidence within the site. Draft legal and responsible-disclosure pages remain excluded from search indexing until the operator, jurisdiction, and monitored security channel are finalized.

Copyright © Xythum Labs. No open-source license is granted for the brand assets or website source unless Xythum Labs publishes one separately.
