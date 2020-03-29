import requests as rq
import pandas as pd

class executadas:
    def __init__ (self, efile, esite, elist):
        self.list = elist # list of tables fetched from the website
        self.site = esite # df to work with website contents
        self.file = efile # df to work with data already saved on a csv file

# Read the page's table
url = "https://www.praticagem.org.br/asp/executadas.asp"
contents = rq.get(url).content
contents = contents.replace(b",", b".")
exec.list = pd.read_html(contents)
exec.site = exec.list[-1]

# Transforming the dataframe                                                    # Sorry PEP8
exec.site = exec.site.drop([0, 1])                                              # remove 2 top rows
exec.site = exec.site.drop([7, 9, 11, 12, 13, 14], axis=1)                      # remove other columns
exec.site.columns = exec.site.iloc[0]                                           # first row as headers
exec.site = exec.site.drop([2])                                                 # remove first row
exec.site["Data"] = exec.site["Data"] + " " + exec.site["Hora"]                 # concat date+hour
exec.site = exec.site.drop(["Hora"], axis=1)                                    # remove column hour
exec.site["Data"] = pd.to_datetime(exec.site["Data"], format="%d/%m/%Y %H:%M")  # changed type
exec.site = exec.site.astype({"Calado": "float64"})                             # changed type
exec.site = exec.site.sort_values(by=["Data"])                                  # sorted by datetime
print(exec.site)
#exec.site.to_csv("manoeuvres.csv")

# Read manoeuvres.csv to a dataframe

# Before next step: find out if we can compare a row in a dataframe to a single row dataframe 
# Bf nxt: FOIWC find an specific row in a df whr all it's cntt matches a single row df
# Find the index of the first row equal to the last row of manoeuvres.csv

# Append rest of the .site to the end of .file

# THE END