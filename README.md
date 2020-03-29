# ships
A script to automate the collection of data from my city's harbour pilot's website.

## Motivation

The Port of Tubarao in the city of Vitoria is one of the largest embarkers of iron ore in the world and it's operated by Vale, one of the big3 of iron ore mining, that is a publicly traded company.

But can we know how much iron ore are they shipping per year?

Well, turns out the harbour pilot's have some information available on their website. A table of manoeuvres with date, name of the vessel and the terminal where the manoeuvre is being executed. But they only allow us to see data from the last 30 days.

## Project

Our goal is to automate that task of going to their website, reading the table and adding the new values into an spreadsheet, so we can collect more than one month of data.

### Tools (I think I’ll use)

* Python 3.7
* Requests lib
* Pandas lib