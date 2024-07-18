from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil,os
download_path=''
ydl_opts = {
    'outtmpl': os.path.join(download_path, '%(title)s-%(id)s.%(ext)s'),
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=92NO3KRdy_w'])