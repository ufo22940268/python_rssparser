import urllib

class downloader:
    mUrl = ""
    def __init__(self, url):
        self.mUrl = url

    def download(self):
        inStream = urllib.urlopen(self.mUrl)
        outFile = self.getOutFile()
        byte = inStream.read(1024)
        while byte != "":
            print byte
            outFile.write(byte)
            byte = inStream.read()
        outFile.close()
        return outFile

    def getOutFile(self):
        return open(self.parseFileName(), "w")

    def parseFileName(self):
        return self.mUrl[self.mUrl.rfind("/") + 1:]


if __name__ == '__main__':
    downloader("http://cn.engadget.com/rss.xml").download()
