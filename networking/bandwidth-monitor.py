'''
Bandwidth Monitor
A small utility program that tracks how much data you have uploaded and downloaded from the net during the course of your current online session.
See if you can find out what periods of the day you use more and less and generate a report or graph that shows it.
'''
import psutil
import time


t0 = time.time()
upload = psutil.net_io_counters(pernic=True)["network name"][0]
download = psutil.net_io_counters(pernic=True)["network name"][1]

print("Total Upload: {:0.2f} kB \n" .format(upload/1024) + "Total Download: {:0.2f} kB" .format(download/1024))

while True:
    latest_upload = upload
    latest_download = download
    upload = psutil.net_io_counters(pernic=True)["network name"][0]
    download = psutil.net_io_counters(pernic=True)["network name"][1]
    t1 = time.time()

    upload_ps = (upload - latest_upload) / (t1 - t0) / 1024.0
    download_ps = (download - latest_download) / (t1 - t0) / 1024.0
    t0 = time.time()
    time.sleep(1)
    print('Upload: {:0.2f} kB/s \n'.format(upload_ps)+'Download: {:0.2f} kB/s'.format(download_ps))
