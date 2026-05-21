
import subprocess

url = open("youtube.txt").read().strip()

cmd = [
    "yt-dlp",
    "-g",
    url
]

try:
    out = subprocess.check_output(cmd).decode().splitlines()

    m3u8 = ""
    for line in out:
        if "m3u8" in line:
            m3u8 = line
            break

    open("live.m3u8", "w").write(m3u8)

except Exception as e:
    open("live.m3u8", "w").write(str(e))
