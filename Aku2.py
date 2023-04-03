from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://results.akuexam.net/ResultsVocat5thSem2021Pub.aspx?RegNo=19303302013&Sem=V"
contents = requests.get(url)  # Getting contents using requests and get methods
html_text = contents.content  # Getting contents of url in variable using content response
soup = BeautifulSoup(html_text, 'html5lib')  # Getting an instance of beautiful soup and parsing values and features

# student details
dsd = pd.DataFrame(columns=['Registration Number', 'Name'])

registration_number = soup.find('span', id='ctl00_ContentPlaceHolder1_DataList1_ctl00_RegistrationNoLabel').text
name = soup.find('span', id='ctl00_ContentPlaceHolder1_DataList1_ctl00_StudentNameLabel').text

dsd = dsd.append({'Registration Number': registration_number, 'Name': name}, ignore_index=True)
# dsd['Name'] = name
# dsd['Registration Number'] = registration_number
# dsd.to_excel('BCA1.xlsx', index=False)

# paper = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView1')
# print(paper.find('caption').text.strip())

# Subject = "Theory"

# Theory
dft = pd.DataFrame(columns=['Subject Code', 'Subject Name', 'ESE', 'IA', 'Total', 'Grade', 'Credit'])

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

        dft = dft.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                          'Credit': cr}, ignore_index=True)

# dft = dft.append({'Subject Code': None, 'Subject Name': None, 'ESE': None, 'IA': None, 'Total': None, 'Grade': None,
#                 'Credit': None},
#                ignore_index=True)


# df.to_excel('BCA.xlsx', index=False)

# Practical
dfp = pd.DataFrame(columns=['Subject Code', 'Subject Name', 'ESE', 'IA', 'Total', 'Grade', 'Credit'])

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

        dfp = dfp.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                          'Credit': cr},
                         ignore_index=True)
        # dft = dft.append({'Practical': Subject}, ignore_index=True)
# df.to_excel('BCA.xlsx', index=False)
# df.to_excel('BCA.xlsx', index=False)


# print(df)
# print(dsd)

csv_file = pd.concat([dsd.reset_index(drop=True), dft.reset_index(drop=True), dfp.reset_index(drop=True)], axis=0)
# csv_file = pd.concat([dsd, dft, dfp],ignore_index=True, join='union')
csv_file.to_excel('BCA.xlsx', index=False)
print(dft.info)
# CGPA
'''
table3 = soup.find('table', id='ctl00_ContentPlaceHolder1_GridView3')
dfc = pd.DataFrame(columns=['Subject Code', 'Subject Name', 'ESE', 'IA', 'Total', 'Grade', 'Credit'])
datas = table3.tbody.find_all('tr')

for data in datas:
    columns = data.find_all('td')
    if columns:
        sc = columns[0].text.strip()
        sn = columns[1].text.strip()
        ese = columns[2].text.strip()
        ia = columns[3].text.strip()
        total = columns[4].text.strip()
        grade = columns[5].text.strip()
        cr = columns[6].text.strip()
        # print(sc, sn, ese, grade, ia)

        dfc = dfc.append({'Subject Code': sc, 'Subject Name': sn, 'ESE': ese, 'IA': ia, 'Total': total, 'Grade': grade,
                        'Credit': cr},
                       ignore_index=True)
# dfc.to_excel('BCA.xlsx')
'''
