#python program to write HTML table into Excel Sheet 

# import pandas
import pandas as pd


# the webpage URL whose table you want to extract
url = "Enter url here"

# assign the table data to a Pandasa dataframe
table = pd.read_html(url)[3]

#store the dataframe in excel file
table.to_excel("data.xlsx")
