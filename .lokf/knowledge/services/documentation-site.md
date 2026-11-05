---
type: Service
id: https://w3id.org/lmodel/iso29100/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/iso29100`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.
resource: website
dependsOn:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/iso29100/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: REPO, SITE, BASE and REDIRECTS
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# Documentation site

`website/` holds an Astro Starlight site with a page per concept, a health page, a graph, the schema's pages and the docs. Every page comes from a file the repository already holds.[^website-readme.md]

`REDIRECTS` keeps the retired mkdocs site's addresses, each redirected to a page of the site.[^site.config.mjs]

[^website-readme.md]: website/README.md
[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE and REDIRECTS
