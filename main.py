from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

songlist = []
url = 'http://www.azlyrics.com/e/edsheeran.html'
data = urlopen(url).read()
page = BeautifulSoup(data,'html.parser')

for link in page.findAll('a'):
    links = str(link.get('href'))
    names = re.findall(r'^(../lyrics/.+)',links)
    for name in [name for name in names if name]:
        songurl = 'http://www.azlyrics.com/lyrics/edsheeran/' + (name.split('/')[3])
        songlist.append(songurl)
        
for songurl in songlist:
    data = urlopen(songurl).read()
    page = BeautifulSoup(data,'html.parser')
    print(page.get_text())
