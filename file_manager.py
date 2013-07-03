import os
import os.path, time 
from setting import *

def getAllFiles():
    fl = [];
    for folder, subs, files in os.walk(unicode(FILES_DIRECTORY)):
        for filename in files:
            f = dict();
            fn = filename.encode("utf-8");
            f["name"] = fn;
            fullPath = FILES_DIRECTORY + fn;
            t = os.path.getctime(fullPath);
            f["create_time"] = t;
            f["url"] = URL_PREFIX + fn;
            fl.append(f);
    fl = sorted(fl, key=lambda x:x["create_time"], reverse=True);
    return fl;

if __name__ == '__main__':
    files =  getAllFiles()
    print "before sort"
    for f in files:
        print f;

    files = sorted(files, key=lambda x:x["create_time"], reverse=True);
    print "after sort"
    for f in files:
        print f;
