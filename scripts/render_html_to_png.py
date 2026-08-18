#!/usr/bin/env python3
"""Render a one-page-science hand-drawn HTML deliverable to PNG images.

For each `.page` section in the HTML, produce one PNG (page-01.png, page-02.png, ...).
Uses Playwright (chromium) for deterministic, Chinese-safe rendering.

Usage:
    python render_html_to_png.py <input.html> [--out DIR]

If Playwright/chromium is unavailable, prints manual-export instructions and
exits non-zero (so the caller can fall back to browser print/screenshot).
"""
import argparse
import os
import sys


def _launch(p):
    """Try bundled chromium first, then fall back to system Edge (common on Windows)."""
    try:
        return p.chromium.launch()
    except Exception:
        return p.chromium.launch(channel="msedge")


def _manual_fallback(html_path: str, out_dir: str, err: str = "") -> str:
    lines = []
    lines.append("[warn] 无法用 Playwright 渲染（未安装 playwright 或 chromium）。")
    if err:
        lines.append(f"       原因: {err}")
    lines.append("")
    lines.append("手动导出 PNG 的方法（零依赖）：")
    lines.append(f"  1. 用浏览器打开: file://{html_path}")
    lines.append("  2. 按 Ctrl+P 打印 → 目标选『另存为 PDF』（每个 .page 自动分页），")
    lines.append("     或逐页用系统截图工具保存为 PNG")
    lines.append(f"  3. 保存到: {out_dir}")
    lines.append("")
    lines.append("安装 Playwright 以获得一键渲染：")
    lines.append("  pip install playwright && playwright install chromium")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Render hand-drawn HTML to PNG per .page section.")
    ap.add_argument("html", help="Path to the one-page-science HTML deliverable")
    ap.add_argument("--out", default=None, help="Output directory (default: <html_dir>/png)")
    args = ap.parse_args()

    html_path = os.path.abspath(args.html)
    if not os.path.isfile(html_path):
        print(f"[error] file not found: {html_path}")
        return 2

    out_dir = args.out or os.path.join(os.path.dirname(html_path), "png")
    os.makedirs(out_dir, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(_manual_fallback(html_path, out_dir))
        return 3

    try:
        with sync_playwright() as p:
            browser = _launch(p)
            # device_scale_factor=2 → 高清；viewport 宽度贴合 .book(820)
            page = browser.new_page(viewport={"width": 900, "height": 1200}, device_scale_factor=2)
            page.goto("file://" + html_path)
            els = page.query_selector_all(".page")
            if not els:
                els = [page.query_selector("body")]
            for i, el in enumerate(els):
                out = os.path.join(out_dir, f"page-{i + 1:02d}.png")
                el.screenshot(path=out)
                print(f"[ok] {out}")
            browser.close()
        print(f"[done] {len(els)} PNG(s) in {out_dir}")
        return 0
    except Exception as e:  # noqa: BLE001
        print(_manual_fallback(html_path, out_dir, err=str(e)))
        return 4


if __name__ == "__main__":
    sys.exit(main())
