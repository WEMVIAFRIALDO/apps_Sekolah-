import os
from PIL import Image, ImageDraw, ImageFilter

def create_android_icons():
    logo_path = r"d:\proyek_applikasi\apps_sekolah\assets\images\logo_salut.png"
    res_base = r"d:\proyek_applikasi\apps_sekolah\android\app\src\main\res"

    if not os.path.exists(logo_path):
        print(f"Error: {logo_path} not found")
        return

    src_logo = Image.open(logo_path).convert("RGBA")

    # Android density mappings
    densities = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }

    # High-res master canvas size for crisp rendering
    master_size = 512

    for folder_name, size in densities.items():
        folder_path = os.path.join(res_base, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # ─── 1. STANDARD IC_LAUNCHER (Squircle / Rounded Box with glow) ────
        canvas = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(canvas)

        # Background squircle with rich dark obsidian tone
        bg_color = (10, 15, 29, 255) # #0A0F1D
        border_color = (56, 189, 248, 180) # Cyan glow accent
        corner_radius = int(master_size * 0.22) # ~22% squircle radius

        # Draw soft outer glow
        glow_layer = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_layer)
        glow_draw.rounded_rectangle(
            [(8, 8), (master_size - 8, master_size - 8)],
            radius=corner_radius,
            fill=(14, 165, 233, 60)
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))
        canvas.paste(glow_layer, (0, 0), glow_layer)

        # Draw main background
        draw.rounded_rectangle(
            [(12, 12), (master_size - 12, master_size - 12)],
            radius=corner_radius,
            fill=bg_color,
            outline=border_color,
            width=6
        )

        # Resize logo to fit inside safe zone (approx 72% of canvas)
        logo_target_size = int(master_size * 0.72)
        logo_resized = src_logo.resize((logo_target_size, logo_target_size), Image.Resampling.LANCZOS)
        offset = ((master_size - logo_target_size) // 2, (master_size - logo_target_size) // 2)
        canvas.paste(logo_resized, offset, logo_resized)

        # Downsample to target density
        final_standard = canvas.resize((size, size), Image.Resampling.LANCZOS)
        standard_path = os.path.join(folder_path, "ic_launcher.png")
        final_standard.save(standard_path, "PNG", optimize=True)

        # ─── 2. ROUND IC_LAUNCHER (Circular version for round launchers) ───
        round_canvas = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
        round_draw = ImageDraw.Draw(round_canvas)

        # Draw circle glow
        r_glow = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
        r_glow_draw = ImageDraw.Draw(r_glow)
        r_glow_draw.ellipse([(8, 8), (master_size - 8, master_size - 8)], fill=(14, 165, 233, 60))
        r_glow = r_glow.filter(ImageFilter.GaussianBlur(8))
        round_canvas.paste(r_glow, (0, 0), r_glow)

        # Draw circle background
        round_draw.ellipse(
            [(12, 12), (master_size - 12, master_size - 12)],
            fill=bg_color,
            outline=border_color,
            width=6
        )

        # Paste logo inside circle
        round_canvas.paste(logo_resized, offset, logo_resized)

        # Apply circular mask
        mask = Image.new("L", (master_size, master_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse([(6, 6), (master_size - 6, master_size - 6)], fill=255)
        
        round_final_master = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
        round_final_master.paste(round_canvas, (0, 0), mask)

        final_round = round_final_master.resize((size, size), Image.Resampling.LANCZOS)
        round_path = os.path.join(folder_path, "ic_launcher_round.png")
        final_round.save(round_path, "PNG", optimize=True)

        print(f"Generated {size}x{size} icons for {folder_name}")

if __name__ == "__main__":
    create_android_icons()
