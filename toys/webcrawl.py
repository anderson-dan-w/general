from httplib import HTTPConnection
import re

host = "www.pythonchallenge.com"
url_base = "pc/def/linkedlist.php?nothing="

h = HTTPConnection(host)
index = "90052"
for i in range(400):
    h.request("GET", url_base+index)
    text = h.getresponse().read()
    print(text)
    match = re.search('is (\d+)$', text)
    if match:
        index = match.group(1)
    else:
        print("No next index found - quitting")
        break
