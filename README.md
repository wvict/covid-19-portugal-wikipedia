# Table/graph generator for Portugal's Covid-19 Wikipedia page
This project has the goal of automating the process of searching and editing tables and graphs for the Portugal Covid-19 pandemic wikipedia page.

## Requirements
- Python 3
- Beautiful Soup
- pdfminer
- requests

## How to use
- Clone this repository and `cd` into it.
- Download the required packages with `pip3 install -r requirements.txt`.
- Run the command `python3 setup.py`.
- Go to the folder `output/english` and:
    - copy the content of the file `SummaryTable.txt` to https://en.wikipedia.org/w/index.php?title=2020_coronavirus_pandemic_in_Portugal&action=edit&section=6.
    - copy the content of the file `GraphsCasesByAgeAndGender.txt` to https://en.wikipedia.org/w/index.php?title=2020_coronavirus_pandemic_in_Portugal&action=edit&section=8.
    - copy the content of the file `TimelineGraphs.txt` to https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Portugal?action=edit&section=9.
- If you want to contribute to the portuguese article, you can do the same thing as before, but the text files are not on the folder `output/portuguese` and the link to the Wikipedia article is https://pt.wikipedia.org/wiki/Pandemia_de_COVID-19_em_Portugal.

## Contributions
Thanks to [hagnat](https://github.com/hagnat/) for the inspiration (he did something similar [here](https://github.com/hagnat/covid) but for the Brazilian wikipedia page).

## To do:
- Implement testing.
- Right now, the correctness of the information taken from the PDFs is based upon its formatting. If DGS changes it, some error will be thrown while parsing for the data. That needs to be fixed (it's working for DGS reports starting from April 1 - I tested :).