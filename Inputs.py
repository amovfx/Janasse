import glob
import os

VIDEODIR = os.path.join(os.path.expanduser('~'), "Videos/*mp4")
TITLESDIR = os.path.join(os.path.expanduser('~'), "HoudiniProjects/EigenTitles/render")

def getVideos():
    videos = dict()

    for videopath in glob.glob(VIDEODIR):
        filename = os.path.basename(videopath)
        index = filename.split("_")[0]
        if index not in videos.keys():
            videos[index] = [videopath]
        else:
            videos[index].append(videopath)

    latest = []
    for index in videos.keys():
        mylist = videos[index]
        latest.append(sorted(mylist, key=lambda x: os.stat(x).st_mtime)[-1])
    return latest


def getTitles(video):
    filename = os.path.basename(video)
    videoBaseName = filename.split("_", 1)[0]
    globpath = os.path.join(TITLESDIR, videoBaseName+'*','*.exr')
    return glob.glob(globpath)


print getTitles(getVideos()[1])

