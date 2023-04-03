from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://results.akuexam.net/ResultsVocat5thSem2021Pub.aspx?RegNo=19303302013&Sem=V"
contents = requests.get(url)  # Getting contents using requests and get methods
html_text = contents.content  # Getting contents of url in variable using content response
soup = BeautifulSoup(html_text, 'html.parser')  # Getting an instance of beautiful soup and parsing values and features
# dft = pd.DataFrame(columns=["Theory", "Practical"])
# dff = pd.DataFrame(columns=['Theory', 'Practical'])
df = pd.DataFrame(columns=['Subject Code', 'Subject Name', 'ESE', 'IA', 'Total', 'Grade', 'Credit'])

# Theory
Subject = "Theory"
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
        # print(sc, sn, ese, grade, ia)

        df = df.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                        'Credit': cr},
                       ignore_index=True)

df = df.append(
    {'Subject Code': 'Practical', 'Subject Name': None, 'ESE': None, 'IA': None, 'Total': None, 'Grade': None,
     'Credit': None},

    ignore_index=True)

df.to_excel("Bca.xlsx", index=False)

# Practical
table2 = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView2')

datas = table2.tbody.find_all('tr')

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
        # print(sc, sn, ese, grade, ia)

        df = df.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                        'Credit': cr},
                       ignore_index=True)

df.to_excel("Bca.xlsx", index=False)

# CGPA
'''
table3 = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView3')

datas = table3.tbody.find_all('tr')

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
        # print(sc, sn, ese, grade, ia)

        df = df.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                        'Credit': cr},
                       ignore_index=True)
# df.to_excel('BCA.xlsx')

'''
