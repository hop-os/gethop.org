#!/usr/bin/env python3
"""Controle van gethop.org: elke link, elk anker en elke docs-route.

Gebruik (vanuit de root van deze repo):  python3 tools/check.py
Exit 0 als alles klopt, 1 als er iets kapot is. Zie UPDATING.md.

- lokale paden (/hop/, /style.css, surf/img/x.png) moeten bestaan;
- ankers (#x, /hopos/#x) moeten als id op de doelpagina staan;
- docs-routes (/hopos/docs/#pagina[:anker]) moeten als Markdown op
  raw.githubusercontent.com staan, in de repo en map die de docs-pagina
  noemt (data-repo, data-docs), en een anker moet als kop bestaan;
- externe links (GitHub, releases, gui.gethop.org) moeten 200 geven
  na redirects.
"""
import concurrent.futures as cf
import html.parser
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = {"User-Agent": "gethop.org-linkcheck"}


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.body = set(), [], {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "body":
            self.body = a
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


def fetch(url, method="HEAD"):
    req = urllib.request.Request(url, headers=UA, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, (r.read().decode("utf-8", "replace") if method == "GET" else "")
    except urllib.error.HTTPError as e:
        if method == "HEAD" and e.code in (403, 405):
            return fetch(url, "GET")
        return e.code, ""
    except Exception as e:  # netwerk, DNS, time-out
        return str(e), ""


def slug(s):  # dezelfde slug als viewer.js
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", s.lower()))


def local_target(page_path, link):
    path = link.split("#")[0].split("?")[0]
    if path.startswith("/"):
        t = ROOT / path.lstrip("/")
    else:
        t = page_path.parent / path
    if t.is_dir() or path.endswith("/"):
        t = t / "index.html"
    return t


def main():
    pages = sorted(p for p in ROOT.rglob("*.html") if "vendor" not in p.parts)
    parsed = {p: parse(p) for p in pages}
    errors, external, docs = [], set(), set()

    for page, info in parsed.items():
        rel = page.relative_to(ROOT)
        for link in info.links:
            if link.startswith(("mailto:", "data:", "javascript:")):
                continue
            if re.match(r"https?://", link):
                external.add(link)
                continue
            if link.startswith("#"):
                if link[1:] and link[1:] not in info.ids:
                    errors.append(f"{rel}: anker {link} bestaat niet op deze pagina")
                continue
            target = local_target(page, link)
            if not target.exists():
                errors.append(f"{rel}: {link} -> {target.relative_to(ROOT)} bestaat niet")
                continue
            anchor = link.split("#", 1)[1] if "#" in link else ""
            if not anchor or target.suffix != ".html":
                continue
            tinfo = parsed.get(target) or parse(target)
            if "data-repo" in tinfo.body:  # een docs-viewer: #pagina[:anker]
                docs.add((str(rel), link, tinfo.body["data-repo"], tinfo.body.get("data-docs", "docs/"), anchor))
            elif anchor not in tinfo.ids:
                errors.append(f"{rel}: {link}: anker #{anchor} bestaat niet")

    def check_ext(url):
        status, _ = fetch(url)
        return url, status

    def check_doc(item):
        rel, link, repo, folder, anchor = item
        page, _, head = anchor.partition(":")
        url = f"https://raw.githubusercontent.com/{repo}/main/{folder}{page}.md"
        status, text = fetch(url, "GET")
        if status != 200:
            return f"{rel}: {link} -> {url} geeft {status}"
        if head:
            heads = {slug(m) for m in re.findall(r"^#{1,4}\s+(.*)", text, re.M)}
            if head not in heads:
                return f"{rel}: {link}: kop #{head} staat niet in {page}.md"
        return None

    with cf.ThreadPoolExecutor(16) as ex:
        for url, status in ex.map(check_ext, sorted(external)):
            if status != 200:
                errors.append(f"extern: {url} geeft {status}")
        errors += [e for e in ex.map(check_doc, sorted(docs)) if e]

    print(f"{len(pages)} pagina's, {len(external)} externe links, {len(docs)} docs-routes")
    for e in errors:
        print("FOUT", e)
    print("groen" if not errors else f"{len(errors)} fout(en)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
