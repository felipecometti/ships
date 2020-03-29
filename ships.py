import requests as rq
import pandas as pd

class executadas:
    def __init__ (self, efile, esite, elist):
        self.list = elist # list of tables fetched from the website
        self.site = esite # dataframe used to work with the website contents
        self.file = efile # dataframe used to work with the data already saved on a csv file

# Read the page's table
url = "https://www.praticagem.org.br/asp/executadas.asp"
contents = rq.get(url).content
executadas.list = pd.read_html(contents)
executadas.site = executadas.list[-1]

# Transforming the dataframe
executadas.site = executadas.site.drop([0, 1]) # remove 2 top rows
executadas.site = executadas.site.drop([7, 9, 11, 12, 13, 14], axis=1) # remove other columns
executadas.site.columns = executadas.site.iloc[0] # first row as headers
executadas.site = executadas.site.drop([2]) # remove first row
print(executadas.site)

# Read manoeuvres.csv to a dataframe

# Before next step: find out if we can compare a row in a dataframe to a single row dataframe 
# Bf nxt: FOIWC find an specific row in a df whr all it's cntt matches a single row df
# Find the index of the first row equal to the last row of manoeuvres.csv

# Append rest of the .site to the end of .file

# THE END