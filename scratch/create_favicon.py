import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Ensure target directories exist
os.makedirs("images", exist_ok=True)

# 1. Create SVG Favicon
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#26201B"/>
      <stop offset="60%" stop-color="#161311"/>
      <stop offset="100%" stop-color="#0E0C0A"/>
    </linearGradient>
    
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE59F"/>
      <stop offset="40%" stop-color="#E6B34D"/>
      <stop offset="100%" stop-color="#C28A28"/>
    </linearGradient>

    <linearGradient id="terracotta" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F7A790"/>
      <stop offset="100%" stop-color="#E07A5F"/>
    </linearGradient>

    <linearGradient id="olive" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A5DAC2"/>
      <stop offset="100%" stop-color="#81B29A"/>
    </linearGradient>

    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Outer Squircle Base -->
  <rect width="512" height="512" rx="116" fill="url(#bg)"/>
  
  <!-- Subtle Inner Border -->
  <rect x="12" y="12" width="488" height="488" rx="104" fill="none" stroke="url(#gold)" stroke-width="6" stroke-opacity="0.35"/>

  <!-- Glowing Aura Circle -->
  <circle cx="256" cy="256" r="190" fill="#E6B34D" fill-opacity="0.04"/>

  <!-- Icon Graphic Group -->
  <g filter="url(#shadow)">
    <!-- Decorative Leaf Ring Accent -->
    <path d="M 120 256 C 120 180 180 120 256 120 C 332 120 392 180 392 256" fill="none" stroke="url(#olive)" stroke-width="4" stroke-linecap="round" stroke-dasharray="8 12" opacity="0.4"/>
    
    <!-- Central Wheat Sheaf / Leaf Emblem -->
    <!-- Center Stalk -->
    <path d="M 256 375 L 256 145" stroke="url(#gold)" stroke-width="12" stroke-linecap="round"/>
    
    <!-- Top Spire Grain -->
    <path d="M 256 125 C 240 100 256 75 256 75 C 256 75 272 100 256 125 Z" fill="url(#gold)"/>

    <!-- Left Grains (Golden Harvest) -->
    <path d="M 250 160 C 205 135 180 165 242 195 Z" fill="url(#gold)"/>
    <path d="M 250 215 C 190 190 165 225 242 255 Z" fill="url(#gold)"/>
    <path d="M 250 270 C 195 245 175 280 242 305 Z" fill="url(#terracotta)"/>

    <!-- Right Grains (Fresh Olive Leaves) -->
    <path d="M 262 160 C 307 135 332 165 270 195 Z" fill="url(#gold)"/>
    <path d="M 262 215 C 322 190 347 225 270 255 Z" fill="url(#olive)"/>
    <path d="M 262 270 C 317 245 337 280 270 305 Z" fill="url(#olive)"/>

    <!-- Artisanal Hand Cradle Base -->
    <path d="M 150 320 C 180 385 332 385 362 320 C 330 360 182 360 150 320 Z" fill="url(#gold)"/>

    <!-- Warm Star Accents -->
    <path d="M 130 150 L 134 165 L 149 169 L 134 173 L 130 188 L 126 173 L 111 169 L 126 165 Z" fill="url(#terracotta)"/>
    <path d="M 382 150 L 386 165 L 401 169 L 386 173 L 382 188 L 378 173 L 363 169 L 378 165 Z" fill="url(#olive)"/>
  </g>
</svg>
'''

with open("images/favicon.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("SVG favicon created successfully.")

# 2. Render high resolution PNGs with PIL
def draw_favicon(size):
    # Supersample by 4x for extreme smoothness
    scale = 4
    w = size * scale
    img = Image.new("RGBA", (w, w), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    bg_color = (22, 19, 17, 255)
    border_color = (230, 179, 77, 200)
    gold_color = (230, 179, 77, 255)
    gold_light = (252, 229, 159, 255)
    terracotta_color = (224, 122, 95, 255)
    olive_color = (129, 178, 154, 255)

    # Corner radius
    rx = int(w * 0.22)
    draw.rounded_rectangle([0, 0, w-1, w-1], radius=rx, fill=bg_color, outline=border_color, width=int(w * 0.015))

    # Center Stalk
    cx = w / 2
    cy = w / 2
    stalk_w = max(4, int(w * 0.025))
    draw.line([(cx, cy + w * 0.22), (cx, cy - w * 0.22)], fill=gold_color, width=stalk_w)

    # Top spire
    top_y = cy - w * 0.25
    spire_r = int(w * 0.04)
    draw.ellipse([cx - spire_r, top_y - spire_r*1.5, cx + spire_r, top_y + spire_r*0.5], fill=gold_light)

    # Left & Right Leaves / Grains
    grain_offsets = [
        (-w * 0.14, -w * 0.15, gold_light),
        (-w * 0.16, -w * 0.04, gold_color),
        (-w * 0.15, w * 0.07, terracotta_color),
        (w * 0.14, -w * 0.15, gold_light),
        (w * 0.16, -w * 0.04, olive_color),
        (w * 0.15, w * 0.07, olive_color),
    ]

    for ox, oy, color in grain_offsets:
        gx = cx + ox
        gy = cy + oy
        gr_w = int(w * 0.08)
        gr_h = int(w * 0.045)
        draw.ellipse([gx - gr_w, gy - gr_h, gx + gr_w, gy + gr_h], fill=color)

    # Hand Cradle
    cradle_y = cy + w * 0.16
    cradle_w = int(w * 0.22)
    cradle_h = int(w * 0.06)
    draw.chord([cx - cradle_w, cradle_y - cradle_h, cx + cradle_w, cradle_y + cradle_h*2], start=0, end=180, fill=gold_color)

    # Downsample using LANCZOS filter
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

# Generate PNG variations
sizes = {
    "images/favicon-16x16.png": 16,
    "images/favicon-32x32.png": 32,
    "images/apple-touch-icon.png": 180,
    "images/favicon.png": 512,
}

img_objs = {}
for path, sz in sizes.items():
    im = draw_favicon(sz)
    im.save(path, "PNG")
    img_objs[sz] = im
    print(f"Saved {path} ({sz}x{sz})")

# Save ICO containing multiple icon resolutions
ico_16 = img_objs[16]
ico_32 = img_objs[32]
ico_48 = draw_favicon(48)
ico_64 = draw_favicon(64)
ico_128 = draw_favicon(128)
ico_256 = draw_favicon(256)

ico_16.save("favicon.ico", format="ICO", append_images=[ico_32, ico_48, ico_64, ico_128, ico_256])
ico_16.save("images/favicon.ico", format="ICO", append_images=[ico_32, ico_48, ico_64, ico_128, ico_256])
print("Saved root and images favicon.ico successfully.")
