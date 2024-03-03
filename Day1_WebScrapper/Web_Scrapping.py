from bs4 import BeautifulSoup

import requests
import time

print("Put some skill you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup = BeautifulSoup(html_text, 'lxml')

    # jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # for job in jobs:
    #     job_position = job.a.text
    #     company = job.h3.text.split()[1]
    #     print(f'{job_position} is available in {company}')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        date_posted = job.find('span', class_='sim-posted').span.text
        # if 'today' in date_posted:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        job_link = job.find('button', class_='waves-effect waves-light btn').text
        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.text','w') as f:
                print('\n')
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'KeySkills: {skills.strip()} \n')
                f.write(f'Post Date:{date_posted.strip()} \n')
                f.write(f'Job Link: {job_link.strip()} \n')
                f.write(f'More Info: {more_info} \n')
            print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print('\n')
        print(f'Waiting {time_wait} minutes.... ')
        time.sleep(time_wait*60)
        print()
