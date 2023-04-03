import time
from bs4 import BeautifulSoup
import requests
import openpyxl
import html5lib

'''
It takes input for different values which we later pass it on my url to find best results
like the Job we are searching for Location and the Work_Experience
we also filter our data with unfamiliar skills ie the skills which user dont know
'''
try:
    search = input('Enter the search for job: ').title()
    location = input("Enter the location: ").title()
    work_experience = int(input("Enter the Work Experience from 0 to 25+: "))

    print('Put some skills that you are not familiar with:')

    unfamiliar_skills = input('>').title()

    print(f"Filtering unfamiliar skills {unfamiliar_skills}")

    # Here is the url of the website

    url = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit'
                       f'&txtKeywords={search}&txtLocation={location}&cboWorkExp1={work_experience}')

    # if we don't want to use contents we can use .text at the end of url
    html_text = url.content  # taking the contents of the urls which is similar to .text a kind of beautiful soup content

    url.raise_for_status() # Throws an error if something wrong with url

    soup = BeautifulSoup(html_text, 'html5lib')  # Creating an object and passing parameters like our html contents and
    # the features

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  # Getting jobs list using li tag


    def find_jobs():
        """
        this function will help to find the jobs on TimesJob website

        """
        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ",
                                                                                       "")  # To replace all the white
                # spaces
                # with nothing, we can also use .strip() method
                skills = job.find('span', class_='srp-skills').text.replace(" ", '').title()
                more_info = job.header.h2.a['href']
                if unfamiliar_skills not in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f"For the Job {search}\n")
                        f.write(f"Company Name: {company_name.strip()}\n")
                        f.write(f"Skills: {skills.strip()}\n")
                        f.write(f"Job Posted Date: {published_date.strip()}\n")
                        f.write(f"More Info: {more_info}\n")

        return "File Saved!"


    if __name__ == '__main__':
        while True:
            find_jobs()
            print('File saved!')
            time_wait = 10
            print(f"Waiting for time {time_wait} minutes...")
            # print(f"{time.time()} + {time_wait} ")
            time.sleep(time_wait * 60)


except Exception as e:
    print(e)