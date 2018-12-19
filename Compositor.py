
from moviepy.editor import *

from Inputs import getVideos
from Converter import convert

import subprocess
import glob
import os

OUTPUTPATH = os.path.join(os.path.expanduser('~'), 'Videos/output')

def getVideoClip(video):
    screencap = VideoFileClip(video)
    resizedclip = screencap.resize(width=1920)
    return resizedclip

def getTitles(video,fps=24):
    titles = convert(video, call=False, ext='png')
    titleGlob = sorted(glob.glob(titles))
    print "titleGlob:", titleGlob
    TitleClip = ImageSequenceClip(titleGlob, fps=fps)
    return TitleClip

def writeAudio(video, output):
    args = ['ffmpeg', "-i", video, "-vn", "-acodec", "libmp3lame", output]
    subprocess.call(args)


def compositeTitles(videoClips, output):
    final = CompositeVideoClip(videoClips, size=(1920, 1080))
    final.write_videofile(output,
                          fps=screencap.fps,
                          codec='libx264',
                          audio=False)


def getDestination(video, ext="_video.mp4"):

    filename = os.path.basename(video).split("-")[0]
    destfilename = filename + ext

    if not os.path.isdir(OUTPUTPATH):
        os.makedirs(OUTPUTPATH)

    dest = os.path.join(OUTPUTPATH, destfilename)
    return dest

def writeFinal(video, audio, output):
    finalcmd = ['ffmpeg', "-i", video, "-i", audio, "-c:v", "copy", "-c:a", "libmp3lame", output]
    subprocess.call(finalcmd)
    os.remove(audio)
    return output





if __name__ == '__main__':
    for video in sorted(getVideos()):


        screencap = getVideoClip(video)

        titles = getTitles(video, fps=screencap.fps)

        finalVideo = getDestination(video, ext="_video.mp4")
        compositeTitles([screencap, titles], output=finalVideo)

        audio_file = "audio_output.mp3"
        writeAudio(video, output=audio_file)

        final = getDestination(video, ext="_final.mp4")
        writeFinal(finalVideo, audio_file, final)

        #upload to vimeo
        #upload to youtube






