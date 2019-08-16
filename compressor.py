import os
from PIL import Image as i
from datetime import datetime

# settings
path = "PATH TO FOLDER HERE"
setwidth = 500
ignore_files = ['.DS_Store', 'archive']  # For Mac OS X

startTime = datetime.now()

fails = []

for filename in os.listdir(path):
    print ("COMPRESSING to " + str(setwidth) + "px: " + filename)
    filepath = os.path.join(path, filename)
    try:
        if filename not in ignore_files:
            img = i.open(filepath)
            print ("Filesize: " + str(img.size))

            # finds percent shrinkage of width and does same for height
            wpercent = (setwidth / float(img.size[0]))
            height = int((float(img.size[1]) * float(wpercent)))

            img = img.resize((setwidth, height), i.ANTIALIAS)
            img.save(filepath, quality=95)
            img.save(filepath, optimize=True, quality=95)

            print ("New size: " + str(img.size))
    except:
        print ("Could not open: " + str(filepath))
        fails.append (str(filepath))
    else:
        print ("Compression complete.\n")

print("DONE: " + str(datetime.now() - startTime))

print (fails)
