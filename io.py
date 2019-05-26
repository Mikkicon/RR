import sys
import glob
from PIL import Image
import numpy as np


def getChannels(image):
    r, g, b = image.split()
    return np.mean(list(r.getdata())), np.mean(list(g.getdata())), np.mean(list(b.getdata()))


def absAndSub(a, b):
    return abs(a-b)


def comparator(image1, image2, file1, file2):
    rI, gI, bI = getChannels(image1)
    rJ, gJ, bJ = getChannels(image2)
    absR = absAndSub(rI, rJ)
    absG = absAndSub(gI, gJ)
    absB = absAndSub(bI, bJ)
    if (absR + absG + absB)/3 < 2:
        print(file1, file2)


def __init__():
    if '--help' in sys.argv or '-h' in sys.argv:
        print('\n\nusage: solution.py [-h] --path PATH\n\n')
        sys.exit()
    if '--path' not in sys.argv:
        print('\n\nusage: solution.py [-h] --path PATH')
        print('soution.py: ERROR: the following arguments are required: --path\n\n')
        sys.exit()
    pathArg = sys.argv[sys.argv.index('--path')+1]
    path = str(pathArg + '/*.jpg')
    preFiles = glob.glob(path)
    files = list(map(lambda x: x[len(pathArg)+1:], preFiles))
    images = [Image.open(x) for x in preFiles]
    for i in range(0, len(images)-1):
        for j in range(i+1, len(images)):
            comparator(images[i], images[j], files[i], files[j])


if __name__ == "__main__":
    __init__()
