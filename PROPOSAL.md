# Update — 2 October 2026: HopOS v3 and HOP v3 in Rust

The site now describes the Rust generation: HopOS v3 (`xinix00/HopOS` main, `Cargo.toml` workspace 3.0.0, tags up to `v3.0.0-alpha.18`) and HOP v3 (`xinix00/hop` main, 3.0.0). The Go generations live in `OLD/` in both repositories and are still the newest signed releases (HopOS v2.2.8, HOP v1.0.7); the download sections say that the links resolve to the newest signed release and that v3 builds from source. SURF is unchanged on the site.

Claim sources:

- Execution model, kernel-as-mechanism and HOP as first resident: HopOS `README.md`.
- Kernel flip and what carries over: `docs/flip.md`; the hardware status per board: `ALLES.md` (first green node Pi 5 on 30 September 2026; repeated warm flips on Pi 4, Radxa Zero 3E, O6N and M4; Altra and LicheeRV v3 bring-up still open).
- Go compatibility: `docs/go-apps.md` (ABI 1 equals Go slot ABI 10; TamaGo welcome proven on QEMU on 2 October 2026).
- Interrupt-driven NICs per board: the support table in `ALLES.md` and `docs/boards.md`.
- Measurements (6,380 MB/s app to app and 4,950 MB/s raw NVMe writes on the M4, 85.7 fps 4K decode on the O6N, Pi 4 and Radxa app-to-app ranges): `docs/measurements.md` and `ALLES.md`, 30 September to 1 October 2026.
- Rust rules (one owner, no mutex, denied `unwrap`/`panic`/`todo`, SAFETY comments, import direction): `rustdoc/README.md` and the `[workspace.lints]` block in `Cargo.toml`.
- HOP: `hop/README.md` (binaries `agentd` and `hop`, the `hop` CLI, cluster via hoplockserver or S3) and `cli/src/main.rs` for the CLI output in the terminal example. The 17.3 s Altra recovery figure is kept with its scope: measured with the previous generation.
- The source-line counts of the Go generation are removed; v3 counts wait for `cargo run -p loc`.

Docs viewer: both repositories' `main` no longer carry `docs/menu.md`, which broke `/hopos/docs/` and `/hop/docs/`. `viewer.js` now falls back to the README of the docs folder (`data-docs` on the page body; empty for the HOP repository root) and builds the menu from its sections and links. A `menu.md` keeps precedence when one returns.

Validation: all four landing pages and both docs viewers rendered headless in Chrome at 1440px and 390px; no horizontal overflow at 390px (measured `scrollWidth`); all in-page anchors resolve; the five linked HopOS docs pages return 200 on `raw.githubusercontent.com`; `node --check viewer.js` and `git diff --check` pass. Not committed.

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
- The storage highlight uses the recorded O6N hardware result: 3056.8 MB/s raw NVMe writes. The expanded scope states the device, date, transfer size, short run length, cache policy and separate app-path measurements. Source: HopOS `docs/v1/technical/release-evidence/2026-09-18-o6n-nvme.json`.
- The apps section focuses on actual HopOS workloads. GoNet is no longer presented alongside them as though it were a verified HopOS workload.

The new HopOS docs links target the promoted `docs/` menu and page names. Publish the corresponding HopOS documentation changes when publishing the site so those routes resolve together.

## Review locally

From this repository: `python3 -m http.server 8765 --bind 127.0.0.1`, then open `http://127.0.0.1:8765/`.

This is an uncommitted local proposal. No release, commit, push or deployment is part of this change.

## Validation

All four landing pages checked in Chromium at 1440px and 390px: no horizontal overflow, missing images, broken section links or JavaScript errors. Mobile navigation opens on each product page. Local links, cross-page anchors and HopOS/HOP documentation routes resolve against their source trees. The source-count command completed successfully. `git diff --check` passes.
