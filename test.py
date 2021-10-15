import psutil
iostat = psutil.net_io_counters(pernic=False)
print(iostat[0])  # upload only
print