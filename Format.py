import os

from pytube import YouTube


def video(url):
    yt = YouTube(url).streams.filter(progressive=True,
                                     file_extension='mp4').order_by('resolution').desc().first()
    yt.download('Video')


def musica(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    out_file = stream.download("Musica")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


try:
    os.makedirs("./Musica")
    os.makedirs("./Video")
except OSError:
    print('Ja Existe Pasta...')


# video('URL')
# musica('URL
