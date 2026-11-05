---
type: Policy
id: https://w3id.org/lmodel/iso29100/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in the standard belongs with its committee.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/iso29100/knowledge/datasets/iso29100-linkml-schema
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:12:24Z"
status: draft
---

# Security policy

Report through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The watch streams ISO Open Data's file and reads DPV's mapping file with no token. It follows a redirect only over https to a listed host, and caps what it reads. The overlap check runs by hand and refuses a copy inside the repository.[^security.md] The surface table in the file says what holds each workflow.[^security.md]

[^security.md]: SECURITY.md
