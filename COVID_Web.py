
from bs4 import BeautifulSoup
import requests


class Scrapper:
    def __init__(self):
        self.content = None
        self.soup = None
        self.samples = None
        self.lastSample = None
        self.numbers = None

    def download(self):
        result = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Northern_Ireland")
        if result.status_code == 200:
            self.content = result.content
        else:
            raise Exception("Download: Could not fetch data.")

    def findSoupSamples(self):
        self.soup = BeautifulSoup(self.content, "html.parser")
        my_table = self.soup.find_all('table', {'class' : 'infobox'})
        #print(self.samples)

        table = my_table[0].find_all(['td'])
        splittedTable = table[5].text
        
        

        
        with open('COVID_19.txt', 'r') as f:
            lines = f.read().splitlines()
            finalLine = lines[-1]
            
        
        if (finalLine == splittedTable + " ~ " ):
            print(finalLine + " :Same as current")
            
        else:
            print("New Cases: " + splittedTable)
            f = open("COVID_19.txt", "a")
            f.write(splittedTable + " ~ ")
            f.close()




    def run(self):
        try:
            self.download()
        except:
            print("No internet")
            time.sleep(500) 
            run(self)
    self.findSoupSamples()
