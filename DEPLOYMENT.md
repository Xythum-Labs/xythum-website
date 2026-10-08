# Deployment and domain runbook

This repository is ready for GitHub Pages and Cloudflare Pages. GitHub Pages is the simplest cutover for `xythum.io` because it can use the domain's existing DNS provider without changing nameservers.

## Current DNS snapshot

Observed on 8 October 2026:

- Authoritative nameservers: `ns1.dns-parking.com` and `ns2.dns-parking.com`
- Apex A records: `31.43.160.6` and `31.43.161.6`
- Mail: Zoho MX records are active
- TXT records include Zoho verification

Preserve every MX and TXT record during a website migration. Website hosting and email routing are separate.

## Recommended: GitHub Pages without changing nameservers

The included workflow publishes `dist/` from `main`.

1. In GitHub, open **Settings → Pages** and keep **Source: GitHub Actions**.
2. Add `xythum.io` under **Custom domain** before changing DNS.
3. In the current DNS provider, remove only the two existing apex website A records after confirming the new Pages deployment works.
4. Add these apex records:

   | Type | Name | Value |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |

5. Add the `www` record:

   | Type | Name | Value |
   | --- | --- | --- |
   | CNAME | `www` | `xythum-labs.github.io` |

6. Keep the existing Hostinger nameservers, Zoho MX records, SPF/DKIM/DMARC records, and verification TXT records.
7. Wait for GitHub's domain check, then enable **Enforce HTTPS**.
8. Verify:

```powershell
Resolve-DnsName xythum.io -Type A
Resolve-DnsName www.xythum.io -Type CNAME
curl.exe -I https://xythum.io
curl.exe -I https://www.xythum.io
```

GitHub may take up to 24 hours to observe DNS changes, though propagation is often faster. Do not add wildcard DNS records.

## Alternative: Cloudflare Pages

Cloudflare Pages can connect directly to this GitHub repository.

- Production branch: `main`
- Framework preset: None
- Build command: `python generate_seo.py`
- Build output directory: `dist`
- Environment variable: `SITE_URL=https://xythum.io`
- Environment variable: `ASSET_VERSION=$CF_PAGES_COMMIT_SHA`

For the apex `xythum.io` domain, Cloudflare Pages requires the domain to be a zone in the same Cloudflare account and normally requires changing the registrar's nameservers to the two nameservers Cloudflare assigns.

Before any nameserver change:

1. Add `xythum.io` to Cloudflare.
2. Compare Cloudflare's imported DNS records with the current provider.
3. Recreate and verify all Zoho MX, SPF, DKIM, DMARC, and verification TXT records.
4. Add the Pages custom domain in **Workers & Pages → Custom domains**.
5. Only then replace the nameservers at the registrar.

If nameservers must remain unchanged, use a subdomain such as `www.xythum.io`: add it in the Pages dashboard first, then create a CNAME at the current DNS provider pointing `www` to the assigned `<project>.pages.dev` hostname. Cloudflare's documentation requires the custom domain to be associated with the Pages project before the CNAME is created.

## Rollback

Record the current website A records before cutover. If the new site fails, restore `31.43.160.6` and `31.43.161.6` for the apex. Do not alter the mail records during a website rollback.

## Post-cutover checks

- Home, protocol, research, developer, security, contact, and community pages return HTTP 200.
- `https://xythum.io/robots.txt` references the production sitemap.
- `https://xythum.io/sitemap.xml` contains canonical `https://xythum.io` URLs.
- `www` redirects to the chosen canonical hostname.
- HTTPS is valid without warnings.
- Zoho inbound and outbound mail still works.
- Search Console and analytics use the final canonical domain.
