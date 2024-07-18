from pytube import YouTube
yt = YouTube("https://www.youtube.com/shorts/JfbnpYLe3Ms")
mp4_files = yt.streams.filter(file_extension="mp4")
mp4_369p_files = mp4_files.get_by_resolution("360p")
mp4_369p_files.download("videos")