import yt_dlp

url = open("youtube.txt").read().strip()

ydl_opts = {
    'quiet': True,
    'cookiefile': 'cookies.txt',
    'extractor_args': {
        'youtube': {
            'player_client': ['android']
        }
    },
    'format': 'b'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        stream_url = info.get("url")

        if not stream_url:
            formats = info.get("formats", [])
            for f in formats:
                if f.get("url"):
                    stream_url = f["url"]
                    break

        with open("live.m3u8", "w") as f:
            f.write(stream_url or "#NO_URL")

        print(stream_url)

except Exception as e:

    with open("live.m3u8", "w") as f:
        f.write(str(e))

    print(e)
