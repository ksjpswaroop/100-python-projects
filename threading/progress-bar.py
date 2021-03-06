'''
Create A Progress Bar for Downloads
Create a progress bar for applications that can keep track of a download in progress. The progress bar will be on a separate thread and will communicate with the main thread using delegates.
'''
import threading
import sys
import urllib.request
import os

class Download(object):

    def __init__(self, obj):
        self.obj = obj

    def file(self, link):
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        save_to = "add path"
        file_name = link.split("/")[-1]

        with urllib.request.urlopen(urllib.request.Request(link, None, headers)) as url:
            meta = url.info()
            file_size = meta.get("Content-length")
            progress_dl = 0
            block_size = 1024

            with open(os.path.join(save_to, file_name), 'wb') as f:

                while float(file_size) != float(progress_dl):
                    buffer = url.read(block_size)

                    if not buffer:
                        break

                    progress_dl += len(buffer)
                    f.write(buffer)

                    #calling DownloadProgress class
                    arr = [progress_dl, file_size]
                    t1 = threading.Thread(target = self.obj.run, args = [arr,])
                    t1.start()
                    t1.join()


class DownloadProgress(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self, arr):
        progress_dl = arr[0]
        file_size = arr[1]
        p = float(progress_dl) / float(file_size)
        status = r"{0}  [{1:.2%}]".format(progress_dl, p)
        status = status + chr(8)*(len(status)+1)
        sys.stdout.write(status)

url = "add url"

t1 = DownloadProgress()
Download(t1).file(url)
