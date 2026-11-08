# gethop.org

The feature and documentation site for **HopOS**, **HOP** and **SURF**. Static HTML and CSS; the documentation viewer reads Markdown from each project's repository and uses the bundled Mermaid renderer for diagrams.

- `/` — how the three projects fit together
- `/hopos/` — the v3 kernel in Rust: ownership, the kernel flip, networking, Go compatibility, apps and hardware
- `/hop/` — placement, workload drivers, updates, operations and recovery
- `/surf/` — distributed windows, display protocol and desktop applications
- `/hopos/docs/`, `/hop/docs/` — repository-backed documentation

## Local preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/`. Documentation content is fetched from the repositories' `main` branches; unpublished local docs do not appear automatically. The viewer reads `menu.md` from the docs folder when there is one, and otherwise builds the menu from the links in the README of that folder (`data-docs` on the page body names the folder; empty means the repository root).

gethop.org is served through Cloudflare (the Pages project also at `gethop-org.pages.dev`); GitHub Pages builds `main` as well. See step 5 of [UPDATING.md](UPDATING.md) for checking what is live. To bring the site up to date with HopOS, HOP and SURF, follow [UPDATING.md](UPDATING.md); `python3 tools/check.py` checks every link, anchor and docs route. [PROPOSAL.md](PROPOSAL.md) is the log of past updates, content decisions and measurement scope.
