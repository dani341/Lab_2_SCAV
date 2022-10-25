import os
import subprocess

def hist(video_input, video_output):
    if os.path.exists(video_output):
        os.remove(video_output)
    subprocess.call("ffmpeg -i " + video_input + ' -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" ' + video_output, shell=True)
    #-vf histogram: Displays histogram for every component.
    #split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay: Splits in two commands: b, the historgram and a, the
        #video, and then verlais them.
hist("bbb_output.mp4", "bbb_hist.mp4")
