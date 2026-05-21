import subprocess

url = open("youtube.txt").read().strip()

result = subprocess.check_output(
    ["yt-dlp", "-g", url],
    text=True
).strip()

with open("live.m3u8", "w") as f:
    f.write(result)

print(result)
