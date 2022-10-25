import os
import subprocess

def cut_vid(video_input, video_output, start, duration):
    if os.path.exists(video_output):#remove video file if exists one with the same name
        os.remove(video_output)
    subprocess.call(
        "ffmpeg -i " + video_input + " -ss " + start + " -t " + duration + " -c copy -map 0 " + video_output, shell=True)
    #-i: Video input
    #-ss: Starting time
    #-t: Duration
    #-c copy: Copy audio and video codecs
    #-map 0: involves a banch of commands to control stream selection
cut_vid("bbb_trimmed.mp4", "bbb_trimmed2.mp4", "00:00:01", "00:00:20")

