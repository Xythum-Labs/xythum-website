from pathlib import Path
from html import escape
import json
import os

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
ORIGIN = os.environ.get("SITE_URL", "https://xythum.io").rstrip("/")
ASSET_VERSION = os.environ.get("ASSET_VERSION", "local")
IMAGE = f"{ORIGIN}/assets/xythum-official.jpeg"

routes = {
    "/": ("Xythum — Private Cross-Chain Execution for DeFi", "Xythum is building a private liquidity layer for cross-chain execution, combining protected intent, distributed coordination, and verifiable settlement."),
    "/protocol/": ("Xythum Protocol Architecture", "Explore the proposed Xythum private execution architecture, its components, boundaries, and open implementation questions."),
    "/privacy-model/": ("Xythum Privacy Model", "Explore Xythum's layered privacy design, protected information, potential observers, and the implementation questions behind precise guarantees."),
    "/threat-model/": ("Xythum Threat Model", "Review the Xythum protocol's adversaries, trust assumptions, failure modes, and verification questions."),
    "/security/": ("Xythum Security Progress", "Follow Xythum's published evidence, technical review priorities, cryptographic architecture, and assurance milestones."),
    "/research/": ("Xythum Research and Source Library", "Browse the original whitepaper, historical prototypes, public repositories, and later research without conflating their maturity."),
    "/developers/": ("Xythum Developer Resources", "Explore Xythum Labs public repositories, research implementations, licenses, technical reading, and the developer roadmap."),
    "/history/": ("Xythum Protocol History", "Follow the public record from Bifrost and Ozone terminology to the original Xythum protocol vision."),
    "/disclosures/": ("Xythum Website Disclosures", "Understand the scope, simulation boundaries, evidence limits, and status qualifications used throughout this Xythum research presentation."),
    "/contact/": ("Contact Xythum Labs", "Contact Xythum Labs about protocol research, future integrations, media, community, and general project enquiries."),
    "/community/": ("Xythum Community and Public Links", "Find Xythum's public profiles, research destinations, documentation, email, and current community invitations."),
    "/protocol/dark-pool/": ("Private Intent and Dark-Pool Processing — Xythum", "Explore Xythum's proposed dark-pool processing role, information boundaries, tradeoffs, and verification questions."),
    "/protocol/frost/": ("FROST Threshold Authorization — Xythum", "Understand how FROST threshold signatures could distribute authorization in Xythum, and what FROST does not prove or hide."),
    "/protocol/fhe/": ("Encrypted Computation and FHE — Xythum", "Explore proposed encrypted computation in Xythum, including key ownership, decryptor roles, workload limits, and open questions."),
    "/protocol/zk/": ("Zero-Knowledge Verification — Xythum", "Explore the role of zero-knowledge proofs in Xythum and the statement, inputs, circuits, and metadata that require verification."),
    "/protocol/tee/": ("Trusted Execution Environments — Xythum", "Review the potential TEE role in Xythum and the hardware, attestation, firmware, code, and side-channel assumptions it introduces."),
    "/protocol/cross-chain/": ("Cross-Chain Execution Boundaries — Xythum", "Review source observation, finality, authorization, replay, recovery, and destination failure in the proposed Xythum design."),
    "/protocol/bitcoin/": ("Bitcoin in the Xythum Protocol Vision", "Explore Bitcoin's role in the original Xythum vision and the custody, script, finality, and integration questions still requiring evidence."),
    "/protocol/node-network/": ("Xythum Distributed Node Coordination", "Review the proposed Xythum node network, operator visibility, corruption thresholds, membership, and liveness assumptions."),
    "/protocol/settlement/": ("Authorization, Verification, and Settlement — Xythum", "Separate threshold authorization, proof verification, and chain finality in the original Xythum design."),
    "/privacy/": ("Privacy Policy Draft — Xythum", "Draft privacy information for the Xythum website, pending operator and hosting review."),
    "/terms/": ("Terms Draft — Xythum", "Draft terms for the Xythum website, pending operator, jurisdiction, and rights review."),
    "/responsible-disclosure/": ("Responsible Disclosure Draft — Xythum", "Draft security reporting guidance for Xythum, pending confirmation of a monitored channel and handling process."),
}

organization = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Xythum Labs",
    "url": ORIGIN,
    "logo": IMAGE,
    "description": "Xythum Labs is building private cross-chain execution infrastructure for protected intent, distributed coordination, and verifiable settlement.",
    "sameAs": ["https://linktr.ee/xythum", "https://x.com/Xythum", "https://www.linkedin.com/company/xythum", "https://github.com/XYTHUM-LABS", "https://xythumlabs.medium.com"],
}

def document(route, title, description):
    canonical = ORIGIN + ("/" if route == "/" else route)
    noindex = route in {"/privacy/", "/terms/", "/responsible-disclosure/"}
    robots = "noindex,nofollow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    schema = dict(organization)
    if route != "/":
        schema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title,
            "description": description,
            "url": canonical,
            "isPartOf": {"@type": "WebSite", "name": "Xythum", "url": ORIGIN},
            "about": {"@type": "Organization", "name": "Xythum Labs"},
        }
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#080b0c">
  <meta name="color-scheme" content="dark">
  <meta name="robots" content="{robots}">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="keywords" content="Xythum, private liquidity, dark pool, DeFi, cross-chain, threshold signatures, zero knowledge, blockchain privacy">
  <meta name="author" content="Xythum Labs">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="icon" href="/assets/xythum-official.jpeg" type="image/jpeg">
  <link rel="apple-touch-icon" href="/assets/xythum-official.jpeg">
  <link rel="manifest" href="/site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Xythum">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{IMAGE}">
  <meta property="og:image:alt" content="The official white geometric Xythum emblem on black">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title, quote=True)}">
  <meta name="twitter:description" content="{escape(description, quote=True)}">
  <meta name="twitter:image" content="{IMAGE}">
  <script type="application/ld+json">{json.dumps(schema, separators=(',', ':'))}</script>
  <link rel="stylesheet" href="/styles.css?v={ASSET_VERSION}">
  <title>{escape(title)}</title>
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <div id="app"><main id="content" class="static-fallback"><article><p>XYTHUM LABS</p><h1>{escape(title)}</h1><p>{escape(description)}</p><nav aria-label="Core destinations"><a href="/protocol/">Protocol</a><a href="/research/">Research</a><a href="/developers/">Developers</a><a href="/community/">Community</a></nav></article></main></div>
  <noscript><p class="noscript">This site includes an interactive protocol visualization. All core pages and public source links remain available through the navigation above.</p></noscript>
  <script src="/app.js?v={ASSET_VERSION}" defer></script>
</body>
</html>
'''

for route, (title, description) in routes.items():
    target = DIST / (route.strip("/") or "") / "index.html"
    if route == "/":
        target = DIST / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(document(route, title, description), encoding="utf-8")

(DIST / "404.html").write_text(document("/404/", "Page Not Found — Xythum", "The requested page is outside the Xythum protocol research graph."), encoding="utf-8")

indexed = [r for r in routes if r not in {"/privacy/", "/terms/", "/responsible-disclosure/"}]
urls = "\n".join(f"  <url><loc>{ORIGIN}{'/' if r == '/' else r}</loc><lastmod>2026-10-08</lastmod><changefreq>{'weekly' if r in {'/', '/research/'} else 'monthly'}</changefreq><priority>{'1.0' if r == '/' else '0.8' if r in {'/protocol/', '/research/'} else '0.6'}</priority></url>" for r in indexed)
(DIST / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
''', encoding="utf-8")
(DIST / "robots.txt").write_text(f'''User-agent: *
Allow: /
Disallow: /privacy/
Disallow: /terms/
Disallow: /responsible-disclosure/
Sitemap: {ORIGIN}/sitemap.xml
''', encoding="utf-8")
(DIST / "site.webmanifest").write_text(json.dumps({
    "name": "Xythum — The Private Liquidity Layer",
    "short_name": "Xythum",
    "description": routes["/"][1],
    "start_url": "/",
    "display": "standalone",
    "background_color": "#080b0c",
    "theme_color": "#080b0c",
    "icons": [{"src": "/assets/xythum-official.jpeg", "sizes": "any", "type": "image/jpeg"}],
}, indent=2), encoding="utf-8")

print(f"Generated SEO pages for {len(routes)} routes")

