#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate High-Quality Motion Graphic Slide Presentation GIF for ba-analyst-kit README
Standard: Senior Engineering Playbook & Visual Motion Design
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
HEIGHT = 440
FPS = 12
SLIDE_DURATION_SEC = 2.4  # seconds per slide
TRANSITION_SEC = 0.4      # transition duration
FRAMES_PER_SLIDE = int(FPS * SLIDE_DURATION_SEC)
NUM_SLIDES = 5
TOTAL_FRAMES = NUM_SLIDES * FRAMES_PER_SLIDE

def get_font(size, bold=False):
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

FONT_KICKER = get_font(12, bold=True)
FONT_TITLE = get_font(34, bold=True)
FONT_SUBTITLE = get_font(16, bold=False)
FONT_CARD_TITLE = get_font(15, bold=True)
FONT_CARD_BODY = get_font(12, bold=False)
FONT_TAG = get_font(11, bold=True)
FONT_FOOTER = get_font(11, bold=True)

def draw_base_background(draw):
    # Deep sleek tech background
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=(9, 15, 28))
    # Ambient corner glow
    for r in range(140, 0, -10):
        alpha = int(18 * (1 - r / 140))
        draw.ellipse([-r + 60, -r + 60, r + 60, r + 60], fill=(0, 40 + alpha, 100 + alpha*2))
        draw.ellipse([WIDTH - r - 40, HEIGHT - r - 40, WIDTH + r - 40, HEIGHT + r - 40], fill=(20 + alpha, 0, 80 + alpha*2))

    # Grid texture
    grid_color = (16, 27, 48)
    for x in range(0, WIDTH, 48):
        draw.line([(x, 0), (x, HEIGHT)], fill=grid_color, width=1)
    for y in range(0, HEIGHT, 48):
        draw.line([(0, y), (WIDTH, y)], fill=grid_color, width=1)

    # Frame border
    draw.rectangle([0, 0, WIDTH - 1, HEIGHT - 1], outline=(30, 50, 85), width=2)
    draw.rectangle([2, 2, WIDTH - 3, HEIGHT - 3], outline=(15, 30, 55), width=1)

def draw_top_timeline(draw, current_slide, slide_progress):
    # Slide progress bar at the top
    bar_y = 16
    tabs = [
        "01. OVERVIEW",
        "02. DELIVERABLES",
        "03. 320 CATALOG",
        "04. VIETNAM RULES",
        "05. AUTOMATION"
    ]
    tab_w = 210
    total_w = len(tabs) * tab_w + (len(tabs) - 1) * 12
    start_x = (WIDTH - total_w) // 2

    for i, tab in enumerate(tabs):
        tx = start_x + i * (tab_w + 12)
        is_active = (i == current_slide)
        is_past = (i < current_slide)

        # Background pill
        bg_col = (18, 36, 68) if is_active else ((14, 25, 45) if is_past else (11, 19, 34))
        border_col = (0, 210, 255) if is_active else ((40, 75, 120) if is_past else (25, 40, 65))
        draw.rounded_rectangle([tx, bar_y, tx + tab_w, bar_y + 24], radius=6, fill=bg_col, outline=border_col, width=1)

        # Active progress fill
        if is_active:
            fill_w = int(tab_w * slide_progress)
            draw.rounded_rectangle([tx, bar_y, tx + fill_w, bar_y + 24], radius=6, fill=(0, 180, 240, 60))

        text_col = (255, 255, 255) if is_active else ((140, 175, 215) if is_past else (85, 115, 150))
        tw = draw.textlength(tab, font=FONT_FOOTER)
        draw.text((tx + (tab_w - tw)//2, bar_y + 5), tab, fill=text_col, font=FONT_FOOTER)

def render_slide_1(draw, progress):
    # SLIDE 1: Hero & Vision
    # Kicker
    kicker = "ENTERPRISE AI AGENT SKILLS KIT • VERSION 2.0.0"
    draw.text((70, 65), kicker, fill=(0, 242, 254), font=FONT_KICKER)

    # Title
    draw.text((70, 88), "BA ANALYST KIT", fill=(255, 255, 255), font=FONT_TITLE)
    draw.rounded_rectangle([390, 96, 520, 124], radius=6, fill=(16, 185, 129), outline=(52, 211, 153), width=1)
    draw.text((404, 101), "VERIFIED EXIT 0", fill=(255, 255, 255), font=FONT_TAG)

    # Subtitle
    sub = "Biến AI Agent & Solo Developer thành Chuyên Gia Business Analyst Senior"
    draw.text((70, 142), sub, fill=(165, 195, 230), font=FONT_SUBTITLE)
    sub2 = "Đóng gói toàn diện chuẩn Bridging The Gap (Laura Brandenburg) & Hệ sinh thái pháp lý Việt Nam"
    draw.text((70, 168), sub2, fill=(120, 150, 185), font=get_font(13))

    # 3 Hero Metric Cards
    cards = [
        ("320 USE CASES", "12 Miền nghiệp vụ chuẩn hóa toàn ngành", "Bao quát 95% nghiệp vụ phần mềm", (0, 242, 254)),
        ("8 LIVING DELIVERABLES", "Trọn vòng đời phân tích từ A-Z", "Scope, Swimlane, UC, ERD, UAT", (16, 185, 129)),
        ("VIETNAM COMPLIANCE", "QĐ 2345, NĐ 13/2023, NĐ 30/2020", "Sinh trắc học CCCD & Xuất Word", (245, 158, 11))
    ]
    card_w = 335
    for i, (head, line1, line2, col) in enumerate(cards):
        cx = 70 + i * (card_w + 30)
        cy = 215
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 175], radius=12, fill=(13, 24, 46), outline=(35, 60, 100), width=1)
        # Accent top bar
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 5], radius=2, fill=col)
        # Content
        draw.text((cx + 20, cy + 24), head, fill=col, font=FONT_CARD_TITLE)
        draw.text((cx + 20, cy + 58), line1, fill=(225, 235, 248), font=get_font(13, bold=True))
        draw.text((cx + 20, cy + 86), line2, fill=(145, 175, 205), font=FONT_CARD_BODY)

        # Micro-tag pill
        draw.rounded_rectangle([cx + 20, cy + 125, cx + 180, cy + 152], radius=6, fill=(20, 36, 68), outline=col, width=1)
        draw.text((cx + 28, cy + 131), "PRODUCTION READY", fill=col, font=get_font(10, bold=True))

def render_slide_2(draw, progress):
    # SLIDE 2: 8 Living Deliverables
    draw.text((70, 65), "END-TO-END METHODOLOGY & TEMPLATES", fill=(16, 185, 129), font=FONT_KICKER)
    draw.text((70, 88), "8 Phân Hệ Nghiệp Vụ Sống (Living Deliverables)", fill=(255, 255, 255), font=FONT_TITLE)
    draw.text((70, 140), "Cung cấp sẵn 7 Template chuẩn Markdown/Mermaid và 6 Quy trình điều phối tự động", fill=(165, 195, 230), font=FONT_SUBTITLE)

    items = [
        ("UC-1: Elicitation Checklist", "5 trụ cột câu hỏi khơi gợi (User, Process, Data, Rules, Tech)"),
        ("UC-2: Scope Statement", "Business Objectives & phân định rạch ròi In/Out-of-Scope"),
        ("UC-3: Business Process", "Quy trình As-Is & To-Be kèm sơ đồ Mermaid Swimlane 4 làn"),
        ("UC-4: Use Case & User Story", "Happy Path, 3 Alternate Flows, 4 Exception Flows & Gherkin AC"),
        ("UC-5: Quality & Audit", "Ma trận kiểm toán chất lượng tài liệu theo Rubric Novice-Expert"),
        ("UC-6: Vietnam UAT Sign-off", "Biên bản nghiệm thu kỹ thuật theo thể thức Nghị định 30/2020"),
        ("UC-7: Data Dictionary & ERD", "Thuộc tính CSDL, validation rules, Data Masking & Mermaid ERD"),
        ("UC-8: API Data Mapping", "Ánh xạ Payload 2 chiều, Webhook đối soát, System Context")
    ]

    col_w = 515
    for i, (title, desc) in enumerate(items):
        col_idx = i // 4
        row_idx = i % 4
        ix = 70 + col_idx * (col_w + 30)
        iy = 185 + row_idx * 50

        draw.rounded_rectangle([ix, iy, ix + col_w, iy + 42], radius=8, fill=(14, 25, 48), outline=(30, 55, 90), width=1)
        # Bullet dot
        draw.ellipse([ix + 14, iy + 17, ix + 22, iy + 25], fill=(0, 242, 254) if col_idx == 0 else (16, 185, 129))
        draw.text((ix + 32, iy + 6), title, fill=(255, 255, 255), font=get_font(12, bold=True))
        draw.text((ix + 32, iy + 23), desc, fill=(140, 170, 205), font=get_font(11))

def render_slide_3(draw, progress):
    # SLIDE 3: 320 Master Use Cases Catalog
    draw.text((70, 65), "MASSIVE TAXONOMY • 12 BUSINESS DOMAINS", fill=(168, 85, 247), font=FONT_KICKER)
    draw.text((70, 88), "Đại Từ Điển 320 Use Cases Chuẩn Hóa", fill=(255, 255, 255), font=FONT_TITLE)
    draw.text((70, 140), "Tra cứu tức thời mã kịch bản, tác nhân, tiền điều kiện, luồng ngoại lệ và quy tắc biên", fill=(165, 195, 230), font=FONT_SUBTITLE)

    domains = [
        ("AUTH (30)", "Định danh, 2FA, SSO, RBAC/ABAC", (0, 242, 254)),
        ("ECOMM (35)", "Giỏ hàng, Flash Sale, Voucher, Đơn", (52, 211, 153)),
        ("PAY (25)", "VietQR, Visa, Ví điện tử, Hóa đơn VAT", (245, 158, 11)),
        ("FIN (35)", "eKYC CCCD chip, Chuyển 24/7, Vay", (239, 68, 68)),
        ("CRM (25)", "Lead Pipeline, Báo giá, Hợp đồng", (59, 130, 246)),
        ("CS (20)", "Helpdesk, SLA Ticket, AI Chatbot", (168, 85, 247)),
        ("HRM (30)", "Chấm công GPS/FaceID, Lương, BHXH", (20, 184, 166)),
        ("WMS (25)", "Nhập xuất kho PDA, Ô kệ, Wave Pick", (234, 179, 8)),
        ("CMS (20)", "Rich Text, Duyệt bài, Media, SEO", (139, 92, 246)),
        ("NOTIF (20)", "Push FCM, SMS Brandname, ZNS", (236, 72, 153)),
        ("DATA (25)", "Nạp Excel có file lỗi, Data Masking", (16, 185, 129)),
        ("ADMIN (30)", "Audit Trail bất biến, Feature Flags", (99, 102, 241)),
    ]

    d_w = 250
    d_h = 56
    for i, (code, desc, col) in enumerate(domains):
        col_i = i % 4
        row_i = i // 4
        dx = 70 + col_i * (d_w + 20)
        dy = 180 + row_i * (d_h + 14)

        draw.rounded_rectangle([dx, dy, dx + d_w, dy + d_h], radius=8, fill=(13, 23, 44), outline=(32, 54, 88), width=1)
        # Left color bar
        draw.rounded_rectangle([dx, dy, dx + 4, dy + d_h], radius=2, fill=col)
        draw.text((dx + 14, dy + 8), code, fill=col, font=get_font(13, bold=True))
        draw.text((dx + 14, dy + 29), desc, fill=(160, 185, 215), font=get_font(10))

def render_slide_4(draw, progress):
    # SLIDE 4: Vietnam Legal & Regulatory Ready
    draw.text((70, 65), "LOCALIZED COMPLIANCE & LEGAL INVARIANTS", fill=(245, 158, 11), font=FONT_KICKER)
    draw.text((70, 88), "Hệ Sinh Thái Pháp Lý & Quy Chuẩn Việt Nam", fill=(255, 255, 255), font=FONT_TITLE)
    draw.text((70, 140), "Tự động áp dụng các quy chuẩn bắt buộc của Ngân hàng Nhà nước và Chính phủ Việt Nam", fill=(165, 195, 230), font=FONT_SUBTITLE)

    pillars = [
        ("Quyết Định 2345/QĐ-NHNN", "SINH TRẮC HỌC KHUÔN MẶT CHIP CCCD", [
            "Bắt buộc xác thực Face khớp chip cho GD > 10M VNĐ/lần",
            "Cộng dồn > 20M VNĐ/ngày bắt buộc sinh trắc học",
            "Tiêu chuẩn chống giả mạo Liveness iBeta Level 2",
            "Khóa an toàn 60 phút khi quét sai quá 3 lần liên tiếp"
        ], (239, 68, 68)),
        ("Nghị Định 13/2023/NĐ-CP", "BẢO VỆ DỮ LIỆU CÁ NHÂN (PDPD)", [
            "Đồng ý tường minh (Explicit Consent - không tick sẵn)",
            "Chính sách che mờ (Data Masking) số CCCD và SĐT",
            "Quyền rút lại sự đồng ý & Xóa dữ liệu vĩnh viễn",
            "Cấm tuyệt đối lưu ảnh chụp khuôn mặt thô sau eKYC"
        ], (0, 242, 254)),
        ("Nghị Định 30/2020/NĐ-CP", "THỂ THỨC VĂN BẢN HÀNH CHÍNH", [
            "Tự động xuất file Word (.docx) chuẩn thể thức VN",
            "Font Times New Roman 13pt chuẩn mực",
            "Căn lề chuẩn: Trái 30mm, Phải 20mm, Trên 20mm, Dưới 20mm",
            "Bảng biểu zebra Navy chuyên nghiệp cho sếp duyệt"
        ], (16, 185, 129))
    ]

    p_w = 335
    for i, (law_id, tag, bullets, col) in enumerate(pillars):
        px = 70 + i * (p_w + 30)
        py = 180
        draw.rounded_rectangle([px, py, px + p_w, py + 215], radius=10, fill=(13, 24, 46), outline=(35, 60, 95), width=1)
        # Top badge
        draw.rounded_rectangle([px, py, px + p_w, py + 34], radius=6, fill=(18, 32, 60), outline=col, width=1)
        draw.text((px + 14, py + 9), law_id, fill=col, font=get_font(12, bold=True))
        draw.text((px + 14, py + 46), tag, fill=(255, 255, 255), font=get_font(11, bold=True))

        for j, b in enumerate(bullets):
            by = py + 78 + j * 32
            draw.ellipse([px + 16, by + 4, px + 22, by + 10], fill=col)
            draw.text((px + 30, by), b, fill=(160, 190, 220), font=get_font(10))

def render_slide_5(draw, progress):
    # SLIDE 5: Automation Tools & Verification
    draw.text((70, 65), "VERIFICATION-DRIVEN • BUILD THE LEVER", fill=(0, 242, 254), font=FONT_KICKER)
    draw.text((70, 88), "Bộ Công Cụ Dòng Lệnh & Nghiệm Thu Tự Động", fill=(255, 255, 255), font=FONT_TITLE)
    draw.text((70, 140), "Nghiệm thu bằng chứng thực nghiệm (Empirical Evidence) - 100% Green Test Runner", fill=(165, 195, 230), font=FONT_SUBTITLE)

    tools = [
        ("export_ba_docx.py", "XUẤT FILE WORD .DOCX CHUẨN NGHỊ ĐỊNH 30", [
            "Chuyển đổi Markdown sang Word chuyên nghiệp",
            "Tự động định dạng bảng zebra Navy, font Times New Roman 13pt",
            "Lệnh: python scripts/export_ba_docx.py -f file.md -o out.docx",
            "Đã xuất thành công 15+ tài liệu mẫu trong thư mục dist/docx/"
        ], (16, 185, 129)),
        ("generate_ui_spec.py", "SINH ĐẶC TẢ GIAO DIỆN & ASCII WIREFRAME", [
            "Phác thảo ASCII wireframe trực quan ngay trong tài liệu",
            "Tự động sinh bảng ràng buộc kiểu dữ liệu trường",
            "Tích hợp validation Việt Nam: CCCD 12 số, SĐT 10 số, MST, VNĐ",
            "Lệnh: python scripts/generate_ui_spec.py"
        ], (0, 242, 254)),
        ("run_full_verification.py", "MASTER VERIFICATION RUNNER 6 TẦNG", [
            "Kiểm tra tính toàn vẹn 8 chuyên đề nghiên cứu chuyên sâu",
            "Xác thực gói skill, 7 templates, 6 workflows, 320 use cases",
            "Chạy bài test đối kháng đa tác tử (Multi-Agent Cross-Validation)",
            "Cam kết 100% Green (Exit Code 0) cho toàn bộ hệ thống"
        ], (168, 85, 247))
    ]

    t_w = 335
    for i, (tool_cmd, subtitle, feats, col) in enumerate(tools):
        tx = 70 + i * (t_w + 30)
        ty = 180
        draw.rounded_rectangle([tx, ty, tx + t_w, ty + 215], radius=10, fill=(13, 24, 46), outline=(35, 60, 95), width=1)
        # Top title box
        draw.rounded_rectangle([tx, ty, tx + t_w, ty + 36], radius=6, fill=(18, 32, 60), outline=col, width=1)
        draw.text((tx + 14, ty + 10), tool_cmd, fill=col, font=get_font(13, bold=True))
        draw.text((tx + 14, ty + 48), subtitle, fill=(255, 255, 255), font=get_font(10, bold=True))

        for j, feat in enumerate(feats):
            fy = ty + 78 + j * 32
            draw.ellipse([tx + 16, fy + 4, tx + 22, fy + 10], fill=col)
            draw.text((tx + 30, fy), feat, fill=(160, 190, 220), font=get_font(10))

RENDERERS = [
    render_slide_1,
    render_slide_2,
    render_slide_3,
    render_slide_4,
    render_slide_5
]

def render_frame(frame_idx):
    current_slide = frame_idx // FRAMES_PER_SLIDE
    slide_frame = frame_idx % FRAMES_PER_SLIDE
    progress = slide_frame / FRAMES_PER_SLIDE

    img = Image.new("RGB", (WIDTH, HEIGHT), (9, 15, 28))
    draw = ImageDraw.Draw(img)

    draw_base_background(draw)
    draw_top_timeline(draw, current_slide, progress)

    # Call current slide renderer
    RENDERERS[current_slide](draw, progress)

    # Smooth cross-fade transition on the last 4 frames
    trans_frames = int(TRANSITION_SEC * FPS)
    if slide_frame >= (FRAMES_PER_SLIDE - trans_frames):
        next_slide = (current_slide + 1) % NUM_SLIDES
        alpha_factor = (slide_frame - (FRAMES_PER_SLIDE - trans_frames)) / trans_frames

        # Render next slide image
        next_img = Image.new("RGB", (WIDTH, HEIGHT), (9, 15, 28))
        next_draw = ImageDraw.Draw(next_img)
        draw_base_background(next_draw)
        draw_top_timeline(next_draw, next_slide, 0.0)
        RENDERERS[next_slide](next_draw, 0.0)

        # Blend
        img = Image.blend(img, next_img, alpha_factor)

    return img

def main():
    assets_dir = Path("assets")
    assets_dir.mkdir(exist_ok=True)
    temp_frames_dir = Path("temp_motion_frames")
    if temp_frames_dir.exists():
        shutil.rmtree(temp_frames_dir)
    temp_frames_dir.mkdir()

    print(f"Generating {TOTAL_FRAMES} motion graphic frames ({NUM_SLIDES} slides, {FPS} FPS, {TOTAL_FRAMES/FPS:.1f}s)...")
    for f in range(TOTAL_FRAMES):
        img = render_frame(f)
        frame_path = temp_frames_dir / f"mframe_{f:03d}.png"
        img.save(frame_path, "PNG")
        if f % 30 == 0:
            print(f"  Rendered frame {f}/{TOTAL_FRAMES}...")

    # Save static poster PNG (Slide 1)
    static_img = render_frame(10)
    static_img.save(assets_dir / "banner.png", "PNG")
    print(f"[PASS] Static poster updated: {assets_dir / 'banner.png'}")

    gif_path = assets_dir / "banner.gif"
    print(f"Compiling motion graphic animated GIF -> {gif_path}...")

    palette_path = temp_frames_dir / "palette.png"
    cmd_palette = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(temp_frames_dir / "mframe_%03d.png"),
        "-vf", "palettegen=max_colors=128:stats_mode=diff",
        str(palette_path)
    ]
    subprocess.run(cmd_palette, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cmd_gif = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(temp_frames_dir / "mframe_%03d.png"),
        "-i", str(palette_path),
        "-lavfi", "paletteuse=dither=bayer:bayer_scale=3",
        "-loop", "0",
        str(gif_path)
    ]
    subprocess.run(cmd_gif, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    shutil.rmtree(temp_frames_dir)
    gif_size = gif_path.stat().st_size
    print(f"[SUCCESS] Motion Graphic Slide GIF generated: {gif_path} ({gif_size:,} bytes)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
