from videocr import get_subtitles

if __name__ == '__main__':  # This check is mandatory for Windows.
    print(get_subtitles('video.mp4', lang='spa', sim_threshold=70, conf_threshold=65))
