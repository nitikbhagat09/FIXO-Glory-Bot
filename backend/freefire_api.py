import os
# saari gandi characters ko saaf karega
bad_chars = {
    "—": "-", "–": "-", "‘": "'", "’": "'", "“": '"', "”": '"',
    "එක": "", "…": "..."
}

for root, dirs, files in os.walk("backend"):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for bad, good in bad_chars.items():
                content = content.replace(bad, good)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

print("All files cleaned!")
