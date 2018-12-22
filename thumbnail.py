import os
import PIL


def takeScreenShot():
    """captures a screenshot to composite into a thumbnail image."""

    screencapLocation = "/tmp/screencap.png"
    cmd = "-import window root {}".format(screencapLocation)
    os.system(cmd)


def renderThumbnail():
    """render thumbnail"""

def writeDescription():
    """composite"""