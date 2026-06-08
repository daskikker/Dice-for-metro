from pathlib import Path

repo_root = Path(r"c:\Users\asas1\Downloads\dice-for-metro\obr-DS-dice-main-main")

replacements = [
    (repo_root / "src" / "background.ts", 'url: "/popover.html"', 'url: "popover.html"'),
    (repo_root / "docs" / "assets" / "background.d231c882.js", 'url:"/popover.html"', 'url:"popover.html"'),
    (repo_root / "docs" / "assets" / "main.4e6983b2.js", '"/assets/', '"/year-zero-engine-dice/assets/'),
    (repo_root / "docs" / "assets" / "PluginThemeProvider.504c3abc.js", '"/assets/', '"/year-zero-engine-dice/assets/')
]

for path, old, new in replacements:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    text = path.read_text(encoding='utf-8')
    if old not in text:
        print(f"Pattern not found in {path.name}: {old}")
        continue
    count = text.count(old)
    text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
    print(f"Updated {path.name}: {count} occurrences replaced.")
