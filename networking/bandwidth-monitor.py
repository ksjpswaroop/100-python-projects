'''
Bandwidth Monitor
A small utility program that tracks how much data you have uploaded and downloaded from the net during the course of your current online session.
'''
import psutil

total_upload = psutil.net_io_counters(pernic=True)["network name"][0]
total_download = psutil.net_io_counters(pernic=True)["network name"][1]

print("Upload: {:0.2f} kB \n" .format(total_upload/1024) + "Download: {:0.2f} kB" .format(total_download/1024))
