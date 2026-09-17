# Website proposal — 6 September 2026

## Direction

**HopOS runs the machine. HOP runs the jobs. SURF brings them to the screen.**

Keep the existing dark palette, green/copper/blue product identities, static HTML, screenshots and documentation viewer. Introduce a shared product navigation and a home page that explains the relationship. Each product page leads with capabilities, shows the mechanism, then links to usage and source.

## Page changes

- **Home:** three equal entry points with a clear role for each project. Explain independent use and the combined system.
- **HopOS:** ownership, dedicated/SMP and cooperative sharing, FLIP, the caller/network/doorbell path, scoped source counts, hardware, Go apps and installation. Move architecture into the main reading flow.
- **HOP:** placement, updates, health checks, logs and recovery. Explain the in-process control plane, the committed snapshot and the separate election lease. Correct the Docker CLI example to use `--image`.
- **SURF:** keep the real screenshots and app examples. Lead with the distributed desktop and pixel/scene protocols. Describe recovery as a restarted app reconnecting, not live process-state migration. Retain the current development limits without making them the headline.

## Claim checks

HopOS descriptions use the local v2.2.2 source and new English docs. HOP descriptions were checked against the pinned `hop@v1.0.2` module (README, architecture and CLI source). SURF descriptions use its local README and existing project material.

- `go run ../tools/loc.go`, run from `hop-os/metal`, reports 11,214 shared metal source lines and 14,582–17,940 per headless board selection. Lean adds 10,744 selected lines. Comments and blanks are excluded. These counts exclude the Go runtime/standard library, TamaGo, HOP and other dependencies; they are not a claim about the complete executable's source footprint. The old 11,300 “whole OS” and unverified 7,550 HOP claims are removed.
- “Go-only” describes the application/system language. Small hardware assembly boundaries and TamaGo are explicitly acknowledged.
- One network IRQ is the intended receive model. QEMU implements it; physical boards currently poll. Architecture timers are separate.
- FLIP is presented as implemented, with repeated ARM resident/TCP preservation evidence. The revised RISC-V downloader and reported shared-core regression retain their open status.
- Approximately 4000 MB/s M4 writes is attributed to the developer, with unrecorded workload/cache/durability conditions stated.
- The apps section focuses on actual HopOS workloads. GoNet is no longer presented alongside them as though it were a verified HopOS workload.

The new HopOS docs links target the promoted `docs/` menu and page names. Publish the corresponding HopOS documentation changes when publishing the site so those routes resolve together.

## Review locally

From this repository: `python3 -m http.server 8765 --bind 127.0.0.1`, then open `http://127.0.0.1:8765/`.

This is an uncommitted local proposal. No release, commit, push or deployment is part of this change.

## Validation

All four landing pages checked in Chromium at 1440px and 390px: no horizontal overflow, missing images, broken section links or JavaScript errors. Mobile navigation opens on each product page. Local links, cross-page anchors and HopOS/HOP documentation routes resolve against their source trees. The source-count command completed successfully. `git diff --check` passes.
