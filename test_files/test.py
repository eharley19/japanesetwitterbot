from bs4 import BeautifulSoup

print("Reading file...")
with open('JMdict_e.xml', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")

    print("Searching for derogatory terms...")
    for entry in soup.findAll('entry'):
        for misc in entry.findAll('misc'):
            if misc.text == '&derog;':
                print(entry.find_next('reb').text)
                print(entry.find_next('gloss').text)
print("Done search.")
