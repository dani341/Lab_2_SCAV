import os
import subprocess

def resize(video_input, scale, video_output):
    if os.path.exists(video_output):
        os.remove(video_output)
    subprocess.call("ffmpeg -i " + video_input + " -vf scale=" + scale + " " + video_output, shell=True)
    # -vf scale=: Scales video in the desired size.
resize("bbb_trimmed.mp4", "1280:720", "bbb_720p.mp4")
resize("bbb_trimmed.mp4", "640:480", "bbb_480p.mp4")
resize("bbb_trimmed.mp4", "360:240", "bbb_360x240.mp4")
resize("bbb_trimmed.mp4", "160:120", "bbb_160x120.mp4")

