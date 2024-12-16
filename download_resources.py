
import requests
host = "https://annual.inven2.com/2023/"

urls = [
    "wp-content/uploads/2023/01/eidsvoll_logo.png"
]
 
# create progress bar

import sys

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    if iteration == total: 
        print()

for url in urls:
    r = requests.get(host + url)

    with open("./" + url, "wb") as f:
        f.write(r.content)

    printProgressBar(urls.index(url) + 1, len(urls), prefix = "Progress", suffix = "Complete", length =  100)
        