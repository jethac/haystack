"""Build site/index.html from vapor.html, inlining capsule art from capsules/<id>.png|jpg.
original.jpg is the real game's Steam capsule; the rest are generated."""
import base64, io, json, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).parent
SIZE = (462, 174)
caps = {}
for png in sorted(p for p in (ROOT / "capsules").iterdir() if p.suffix.lower() in (".png", ".jpg") and not p.name.startswith("_")):
    img = Image.open(png).convert("RGB")
    if img.size != SIZE:
        w, h = img.size
        target = SIZE[0] / SIZE[1]
        if w / h > target:
            nw = round(h * target); img = img.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else:
            nh = round(w / target); img = img.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
        img = img.resize(SIZE, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "WEBP", quality=82, method=6)
    caps[png.stem] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="One game went viral. Thirty showed up. Find the original Needle In A Haystack Simulator in a store full of clones.">
<meta property="og:title" content="Find the Original">
<meta property="og:description" content="One game went viral. Thirty showed up. Can you find the real one?">
<meta property="og:url" content="https://haystack.jethachan.net">
<meta name="twitter:card" content="summary_large_image">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}[hidden]{display:none!important}img{max-width:100%}</style>
<script>window.HAYSTACK_CAPSULES=""" + json.dumps(caps) + """;</script>
</head>
<body>
"""
page = (ROOT / "vapor.html").read_text(encoding="utf-8")
# inline the tweet screenshot so the site stays one file
tw = Image.open(ROOT / "assets" / "tweet.png").convert("RGB")
buf = io.BytesIO(); tw.save(buf, "WEBP", quality=85, method=6)
page = page.replace('src="assets/tweet.png"', 'src="data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode() + '"')

out = ROOT / "site" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(head + page + "\n</body>\n</html>\n", encoding="utf-8")
(out.parent / "CNAME").write_text("haystack.jethachan.net\n", encoding="utf-8")
print(f"built {out} with {len(caps)} capsule images ({out.stat().st_size // 1024} KB)")
