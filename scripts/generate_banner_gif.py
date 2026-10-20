#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Beat-Synced Animated Banner GIF for ba-analyst-kit README
Standard: Senior Engineering Playbook & Visual Design
"""

import math
import os
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

WIDTH = 1200
HEIGHT = 380
FPS = 20
DURATION_SEC = 2.8125  # Exactly 6 beats at 128 BPM (beat period = 0.46875s)
TOTAL_FRAMES = int(FPS * DURATION_SEC)
BPM = 128
BEAT_PERIOD = 60.0 / BPM

def get_font(size, bold=False):
    # Try standard Windows fonts
    font_candidates = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\tahomabd.ttf" if bold else "C:\\Windows\\Fonts\\tahoma.ttf",
    ]
    for fc in font_candidates:
        if os.path.exists(fc):
            try:
                return ImageFont.truetype(fc, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_frame(frame_idx):
    t = frame_idx / FPS
    # Calculate beat phase (0 to 1)
    beat_progress = (t % BEAT_PERIOD) / BEAT_PERIOD
    # Pulse hits on beat (beat_progress ~ 0)
    pulse = math.exp(-6.0 * beat_progress)

    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 14, 26))
    draw = ImageDraw.Draw(img)

    # 1. Background Grid & Ambient Glow
    # Top subtle radial gradient glow
    glow_intensity = int(35 + 25 * pulse)
    for r in range(160, 0, -10):
        alpha = int((glow_intensity * (1 - r / 160)))
        draw.ellipse([WIDTH//2 - r*2.5, -r + 40, WIDTH//2 + r*2.5, r*2 + 40], fill=(10 + alpha//2, 25 + alpha, 45 + alpha*2))

    # Grid lines
    grid_color = (18, 30, 52)
    for x in range(0, WIDTH, 40):
        draw.line([(x, 0), (x, HEIGHT)], fill=grid_color, width=1)
    for y in range(0, HEIGHT, 40):
        draw.line([(0, y), (WIDTH, y)], fill=grid_color, width=1)

    # Outer border with neon pulse
    border_blue = int(140 + 100 * pulse)
    border_cyan = int(200 + 55 * pulse)
    draw.rectangle([0, 0, WIDTH - 1, HEIGHT - 1], outline=(20, 50, 90), width=2)
    draw.rectangle([2, 2, WIDTH - 3, HEIGHT - 3], outline=(0, border_cyan // 3, border_blue // 2), width=1)

    # 2. Top Kicker Tag
    font_tag = get_font(13, bold=True)
    tag_text = "⚡ ENTERPRISE AI AGENT SKILLS KIT • BRIDGING THE GAP STANDARD ⚡"
    tag_w = draw.textlength(tag_text, font=font_tag)
    tag_x = (WIDTH - tag_w) // 2
    tag_y = 25
    # Tag badge box
    draw.rounded_rectangle([tag_x - 16, tag_y - 4, tag_x + tag_w + 16, tag_y + 20], radius=10, fill=(14, 30, 58), outline=(0, 210, 255), width=1)
    draw.text((tag_x, tag_y), tag_text, fill=(0, 240, 255), font=font_tag)

    # 3. Main Title: BA ANALYST KIT
    font_title = get_font(52, bold=True)
    title_text = "BA ANALYST KIT"
    title_w = draw.textlength(title_text, font=font_title)
    title_x = (WIDTH - title_w) // 2
    title_y = 65

    # Glowing drop shadow for title on beat
    shadow_offset = 2
    shadow_color = (0, int(120 * pulse), int(200 * pulse))
    draw.text((title_x + shadow_offset, title_y + shadow_offset), title_text, fill=shadow_color, font=font_title)
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=font_title)

    # Version pill next to title
    font_ver = get_font(14, bold=True)
    ver_text = "v2.0.0"
    ver_x = title_x + title_w + 14
    ver_y = title_y + 12
    draw.rounded_rectangle([ver_x, ver_y, ver_x + 65, ver_y + 26], radius=6, fill=(16, 185, 129), outline=(52, 211, 153), width=1)
    draw.text((ver_x + 10, ver_y + 4), ver_text, fill=(255, 255, 255), font=font_ver)

    # 4. Subtitle
    font_sub = get_font(18, bold=False)
    sub_text = "Universal Business Analysis Super-Skill for AI Coding Agents & Solo Engineers"
    sub_w = draw.textlength(sub_text, font=font_sub)
    draw.text(((WIDTH - sub_w) // 2, 142), sub_text, fill=(160, 185, 215), font=font_sub)

    # 5. Badges Bar (4 High-Impact Stat Badges)
    badges = [
        ("320 USE CASES", "12 Miền Nghiệp Vụ", (0, 242, 254)),
        ("7 TEMPLATES", "Bridging The Gap (CBAP)", (16, 185, 129)),
        ("6 WORKFLOWS", "Elicitation → UAT Sign-off", (168, 85, 247)),
        ("VIETNAM READY", "QĐ 2345 & NĐ 13/2023", (245, 158, 11)),
    ]

    badge_w = 260
    badge_h = 68
    total_bar_w = len(badges) * badge_w + (len(badges) - 1) * 20
    start_x = (WIDTH - total_bar_w) // 2
    badge_y = 195

    font_b_title = get_font(16, bold=True)
    font_b_sub = get_font(12, bold=False)

    for i, (b_title, b_sub, b_color) in enumerate(badges):
        bx = start_x + i * (badge_w + 20)
        # Pulse highlight on badge sequentially per beat
        active_badge = int(t / BEAT_PERIOD) % len(badges)
        is_highlighted = (i == active_badge) and (pulse > 0.3)
        bg_fill = (22, 40, 75) if is_highlighted else (13, 24, 46)
        border_col = b_color if is_highlighted else (40, 65, 105)

        draw.rounded_rectangle([bx, badge_y, bx + badge_w, badge_y + badge_h], radius=10, fill=bg_fill, outline=border_col, width=2 if is_highlighted else 1)

        # Indicator dot
        dot_r = 4 + (2 if is_highlighted else 0)
        draw.ellipse([bx + 16 - dot_r, badge_y + 24 - dot_r, bx + 16 + dot_r, badge_y + 24 + dot_r], fill=b_color)

        draw.text((bx + 32, badge_y + 14), b_title, fill=b_color, font=font_b_title)
        draw.text((bx + 32, badge_y + 38), b_sub, fill=(180, 200, 225), font=font_b_sub)

    # 6. Audio Waveform Beat Pulse at the Bottom
    wave_y = 310
    wave_points = []
    num_bars = 48
    bar_width = 16
    spacing = (WIDTH - 120) / num_bars

    for i in range(num_bars):
        bx = 60 + i * spacing
        # Sine wave frequency with beat pulse
        wave_height = 8 + 26 * math.sin(i * 0.35 + t * 5.0) * math.cos(i * 0.15) * (0.6 + 0.8 * pulse)
        wave_height = max(4, abs(wave_height))
        # Color transition from cyan to purple
        ratio = i / num_bars
        r_c = int(0 + 160 * ratio)
        g_c = int(220 * (1 - ratio * 0.5))
        b_c = int(255)
        draw.rounded_rectangle([bx, wave_y + 25 - wave_height, bx + bar_width - 4, wave_y + 25 + wave_height], radius=3, fill=(r_c, g_c, b_c, 220))

    # Bottom status caption
    font_foot = get_font(12, bold=False)
    foot_text = "SYNCHRONIZED BEAT ENGINE • AGENT PROTOCOL TESTED 100% GREEN (EXIT CODE 0)"
    foot_w = draw.textlength(foot_text, font=font_foot)
    draw.text(((WIDTH - foot_w) // 2, 355), foot_text, fill=(100, 130, 165), font=font_foot)

    return img

def main():
    assets_dir = Path("assets")
    assets_dir.mkdir(exist_ok=True)
    temp_frames_dir = Path("temp_frames")
    if temp_frames_dir.exists():
        shutil.rmtree(temp_frames_dir)
    temp_frames_dir.mkdir()

    print(f"Generating {TOTAL_FRAMES} beat-synced frames at {FPS} FPS (128 BPM)...")
    for f in range(TOTAL_FRAMES):
        img = draw_frame(f)
        frame_path = temp_frames_dir / f"frame_{f:03d}.png"
        img.save(frame_path, "PNG")

    # Save static poster PNG
    static_img = draw_frame(0)
    static_img.save(assets_dir / "banner.png", "PNG")
    print(f"[PASS] Static poster saved: {assets_dir / 'banner.png'}")

    gif_path = assets_dir / "banner.gif"
    print(f"Compiling animated GIF via ffmpeg palettegen -> {gif_path}...")

    # Two-pass high quality GIF with palettegen to avoid color banding
    palette_path = temp_frames_dir / "palette.png"
    cmd_palette = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(temp_frames_dir / "frame_%03d.png"),
        "-vf", "palettegen=max_colors=128:stats_mode=diff",
        str(palette_path)
    ]
    subprocess.run(cmd_palette, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cmd_gif = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(temp_frames_dir / "frame_%03d.png"),
        "-i", str(palette_path),
        "-lavfi", "paletteuse=dither=bayer:bayer_scale=3",
        "-loop", "0",
        str(gif_path)
    ]
    subprocess.run(cmd_gif, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Clean up temp frames
    shutil.rmtree(temp_frames_dir)

    gif_size = gif_path.stat().st_size
    print(f"[SUCCESS] Animated Beat-Synced Banner generated: {gif_path} ({gif_size:,} bytes)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
