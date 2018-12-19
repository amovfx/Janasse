"""Converts exrs to tgas"""

import os
import subprocess as sp

from Inputs import getVideos, getTitles


icp = os.path.join(os.getenv('HFS'),'bin', 'icp')

def convert(video, call=True, ext='tga'):
    """Converts exr to tga for moviepy"""
    titles = getTitles(video)
    if call:
        for img in titles:
            dest = os.path.splitext(img)[0] + '.' + ext
            sp.call([icp, img, dest])

    globpath = titles[0].split(".")
    globpath[1] = '*'
    globpath[2] = ext
    globpath = ".".join(globpath)
    print globpath
    return globpath

