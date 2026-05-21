import yt_dlp

url = open("youtube.txt").read().strip()

ydl_opts = {
    'quiet': True,
    'cookiefile': 'cookies.txt',
    'format': 'best'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        stream_url = info.get("url", "")

        with open("live.m3u8", "w") as f:
            f.write(stream_url)

        print(stream_url)

except Exception as e:

    with open("live.m3u8", "w") as f:
        f.write(str(e))

    print(e)
