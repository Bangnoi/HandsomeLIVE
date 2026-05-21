import subprocess

url = open("youtube.txt").read().strip()

cmd = [
    "yt-dlp",
    "--cookies", "cookies.txt",
    "--user-agent",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36",
    "--extractor-args",
    "youtube:player_client=android",
    "--no-cache-dir",
    "-g",
    url
]

try:
    out = subprocess.check_output(cmd).decode().splitlines()

    m3u8 = ""

    for line in out:
        if "googlevideo" in line or "m3u8" in line:
            m3u8 = line
            break

    if m3u8:
        open("live.m3u8", "w").write(m3u8)
    else:
        open("live.m3u8", "w").write("NO LINK FOUND")

except Exception as e:
    open("live.m3u8", "w").write(str(e))
