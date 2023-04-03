import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np

# Reading csv
# df = pd.read_csv('pandas-master/pokemon_data.csv')

# Reading Excel
# df = pd.read_excel('pandas-master/pokemon_data.xlsx')
# print(df)

# print(df.head(3)) # Print only top 3
# print(df.tail(3)) # Print only bottom 3

# print(df.columns)  # Returns or reads number of columns
# print(df['Name'])  # Returns specific columns
# print(df.iloc[0:4])  # Returns Each Rows
# for index, row in df.iterrows():  # Returns Each Rows
#     print(index, row["Name"])

url = "https://results.akuexam.net/ResultsVocat5thSem2021Pub.aspx?RegNo=19303302013&Sem=V"
contents = requests.get(url)  # Getting contents using requests and get methods
html_text = contents.content  # Getting contents of url in variable using content response
soup = BeautifulSoup(html_text, 'html5lib')  # Getting an instance of beautiful soup and parsing values and features
'''
table1 = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView1')

datas = table1.tbody.find_all('tr')


for data in datas:
    colums = data.find_all('td')
    if colums:
        sc = colums[0].text.strip()
        sn = colums[1].text.strip()
        ese = colums[2].text.strip()
        ia = colums[3].text.strip()
        total = colums[4].text.strip()
        grade = colums[5].text.strip()
        cr = colums[6].text.strip()
        # dict_subject[sc] = sn, ese, ia, total

        df = df.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                        'Credit': cr}, ignore_index=True)

# dff.to_excel("B.xlsx", index=False)
'''
# Practical
table2 = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView2')
sc = []
ese = []
ia = []
total = []

df = pd.DataFrame(columns=['Subject code', 'Subject Name', "ESE", 'IA', 'Total', 'Grade', 'Credit'])
datas = table2.tbody.find_all('tr')
for data in datas:
    colums = data.find_all('td')
    if colums:
        sc.append(int(colums[0].text.strip()))
        sn = colums[1].text.strip()
        ese.append(int(colums[2].text.strip()))
        ia.append(int(colums[3].text.strip()))
        total.append(int(colums[4].text.strip()))
        grade = colums[5].text.strip()
        cr = colums[6].text.strip()
        # dict_subject[sc] = sn, ese, ia, total
        # print(sc, sn, ese, grade, ia)
        df = df.append(
                {'3030601': {"IA":23,"ESE":33,"Total":121}, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                 'Credit': cr},
                ignore_index=True)

df.to_excel("bca.xlsx")
