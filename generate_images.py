"""
Re-render Smash Burgery's real IG food photos into high-res, premium web imagery
using OpenAI gpt-image-1 (image edit). Outputs PNG, then optimizes to responsive WebP.
"""
import os, sys, base64, io, time
import requests
from PIL import Image

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    sys.exit("No OPENAI_API_KEY in environment")

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "ig-source")
GEN = os.path.join(BASE, "assets", "gen")
os.makedirs(GEN, exist_ok=True)

EDIT_URL = "https://api.openai.com/v1/images/edits"

# Each job: (source file, output name, size, prompt)
JOBS = [
    (
        "ig5.webp", "hero", "1536x1024",
        "Premium commercial food photography of a smash burger and Nashville hot "
        "chicken spread, arranged on branded burger paper over a dark charcoal "
        "surface. Juicy beef smash patties with melted cheese, crispy red-spiced "
        "Nashville hot chicken, slaw and loaded fries. Dramatic moody side lighting, "
        "glistening textures, rich shadows, subtle warm glow, shallow depth of field, "
        "ultra sharp, appetizing, hero shot. Keep the dark background clean."
    ),
    (
        "ig6.webp", "beef", "1536x1024",
        "Premium commercial food photography of a single juicy beef smash burger on a "
        "dark slate board, toasted brioche bun, crispy seared patty edges, melted "
        "American cheese pull, fresh lettuce, tomato and onion. Dramatic studio side "
        "lighting on a dark charcoal background, glistening, ultra sharp, high "
        "resolution, shallow depth of field. Appetizing close-up."
    ),
    (
        "ig2.webp", "chicken", "1024x1536",
        "Premium commercial food photography of a Nashville hot chicken box: crispy "
        "deep-red spiced fried chicken fillets, brioche bun, fresh slaw with red "
        "cabbage, golden fries, creamy mac and cheese, and a cup of dipping sauce. "
        "Dark moody background, dramatic lighting, steam and glisten, ultra sharp, "
        "high resolution, appetizing top-down angle."
    ),
    (
        "ig3.webp", "fries", "1536x1024",
        "Premium commercial food photography of loaded fries topped with crispy "
        "Nashville fried chicken pieces, pickles and drizzled sauce, served in a "
        "kraft box, with dipping sauces beside. Dark charcoal background, dramatic "
        "moody lighting, glistening textures, ultra sharp, high resolution, appetizing."
    ),
]

def to_png(path):
    im = Image.open(path).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    buf.seek(0)
    return buf

def generate(src, name, size, prompt):
    src_path = os.path.join(SRC, src)
    print(f"[{name}] editing from {src} -> {size}")
    png = to_png(src_path)
    files = {"image": (f"{src}.png", png, "image/png")}
    data = {"model": "gpt-image-1", "prompt": prompt, "size": size, "quality": "high", "n": "1"}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    r = requests.post(EDIT_URL, headers=headers, files=files, data=data, timeout=420)
    if r.status_code != 200:
        print(f"[{name}] ERROR {r.status_code}: {r.text[:500]}")
        return None
    b64 = r.json()["data"][0]["b64_json"]
    raw = base64.b64decode(b64)
    out_png = os.path.join(GEN, f"{name}.png")
    with open(out_png, "wb") as f:
        f.write(raw)
    print(f"[{name}] saved {out_png} ({len(raw)//1024} KB)")
    return out_png

ok = []
for src, name, size, prompt in JOBS:
    try:
        if generate(src, name, size, prompt):
            ok.append(name)
    except Exception as e:
        print(f"[{name}] EXCEPTION: {e}")
    time.sleep(1)

print("DONE:", ok)
