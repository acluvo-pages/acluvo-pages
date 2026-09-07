# Acluvo website

This repository is a static GitHub Pages site. There is **one** deployment workflow:

- `.github/workflows/deploy.yml`

It deploys the repository root directly to GitHub Pages. No build step and no `gh-pages` branch are required.

## Live demo routes

Once `acluvo.com` is configured as the GitHub Pages custom domain, the capability demos are available at:

- `https://acluvo.com/examples/business-kpi-dashboard/`
- `https://acluvo.com/examples/automated-reporting/`
- `https://acluvo.com/examples/operations-analysis/`

The landing page links to all three from the **Demos** navigation item and the **Live Capability Demos** section.

## GitHub Pages setting

Repository → **Settings → Pages → Build and deployment → Source: GitHub Actions**.

The site entry file is `/index.html`.
