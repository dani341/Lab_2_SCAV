import os
import subprocess

def mono_stereo(video_input, video_output):
    if os.path.exists(video_output):
        os.remove(video_output)
    subprocess.call("ffmpeg -i " + video_input + ' -ac 1 ' + video_output, shell=True)
    #-ac 1: To change it to mono
    #ffmpeg -i input.mp3 -ac 2 output.m4a
mono_stereo("bbb_output.mp4", "bbb_mono.mp4")

def stereo_mono(video_input, video_output):
    if os.path.exists(video_output):
        os.remove(video_output)
    subprocess.call("ffmpeg -i " + video_input + ' -ac 2 ' + video_output, shell=True)
    #-ac2: To change it to stereo
stereo_mono("bbb_mono.mp4", "bbb_stereo.mp4")
