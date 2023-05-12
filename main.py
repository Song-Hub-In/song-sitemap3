from bs4 import BeautifulSoup
from requests import get
from json import dumps
import os

sitemap = 1


paths = ["sitemap", "json", "mid"]
for path in paths:
    # Check whether the specified path exists or not
    if not os.path.exists(path):
        os.makedirs(path)
        print("The "+path+" directory is created!")


# This Will Return The SongId As List
# The SiteMap Contains The Song URL
# With The Help Of Request Liberay We Get The Song URL From that We use split Function and Extract thr id
if len(os.listdir("sitemap/")) < 10:
    x = get("https://www.hungama.com/sitemap/song/song-sitemap"+str(sitemap)+".xml",allow_redirects=False)
    soup = BeautifulSoup(x.text, "xml")
    Song_ID = [str(str(j).split("/")[5]) for j in soup.find_all('loc')]

    for i in range(int(len(Song_ID)/200)+1):
        # Writing to sample.json
        with open('sitemap/'+str(i)+'.txt', "w") as outfile:
            for id in Song_ID[200*i:200*(i+1)]:
                outfile.write(id+"\n")

else:
    print("Already Exists")