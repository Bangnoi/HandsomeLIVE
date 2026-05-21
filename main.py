import subprocess

url = open("youtube.txt").read().strip()

try:
    result = subprocess.check_output(
        [
            "streamlink",
            "--stream-url",
            url,
            "best"
        ],
        text=True
    ).strip()

    with open("live.m3u8", "w") as f:
        f.write(result)

    print(result)

except Exception as e:

    with open("live.m3u8", "w") as f:
        f.write(str(e))

    print(e)
