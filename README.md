# Find the Original

A shitpost: a parody storefront where you have to find the original *Needle In A Haystack Simulator* among its look-alikes.

**[haystack.jethachan.net](https://haystack.jethachan.net)**

Not affiliated with Nas Nakarus, Studio Bitdot, Polden Publishing or Valve. Every other game in it is made up. The real one is [on Steam](https://store.steampowered.com/app/5159870/Needle_In_A_Haystack_Simulator/).

## Build

`vapor.html` is the page. `python build.py` (needs Pillow) inlines the capsule art in `capsules/` and the post screenshot in `assets/` and writes a single-file `site/index.html` plus `site/CNAME`. Commit `site/`; GitHub Actions deploys it to Pages.

Clone capsule art was generated to the brief in `capsules/SPEC.md`, which follows Steam's graphical asset rules.

## Hosting

GitHub Pages (Actions deploy of `site/`), custom domain `haystack.jethachan.net`, fronted by Cloudflare: a proxied `CNAME haystack → jethac.github.io`. Cloudflare terminates HTTPS, so GitHub's "Enforce HTTPS" stays off.
