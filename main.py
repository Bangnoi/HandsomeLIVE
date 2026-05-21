import subprocess

url = open("youtube.txt").read().strip()

try:
    result = subprocess.check_output(
        ["yt-dlp", "-g", url],
        text=True
    ).strip()

    with open("live.m3u8", "w") as f:
        f.write(result)

    print("SUCCESS")

except Exception as e:

    with open("live.m3u8", "w") as f:
        f.write("#ERROR")

    print(e)
