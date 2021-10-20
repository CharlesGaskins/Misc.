import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os
from itertools import repeat, chain


job_links =[]
key_words = []
key_words_description = []
clean_description = []
provider_info = []
clean_p = []
master_df_list = []


##GETTING EACH JOB LISTING PAGE
url = requests.get('https://www.eslbase.com/jobs/china/')
urlcontent = url.content
soup = BeautifulSoup(urlcontent, "html.parser")
for link in soup.findAll('a', attrs={'class': "job-title"}):
    job_links.append(link['href'])

=
    # q = []
    # #OPENING EACH JOB LISTING AND SAVING THE JOB SPECFICS
while len(job_links) > 0:
    for j_link in job_links:
        jobresponse=requests.get(j_link)
        jobcontent = jobresponse.content
        job_soup = BeautifulSoup(jobcontent, "html.parser")
        # print(job_soup)
        for job_sections in job_soup.find_all('h2', attrs={'class': 'ad-top'}):
            key_words.append(job_sections.get_text())
        # print(key_words)
        for job_descriptions in job_soup.find_all('div', attrs={'class': 'wpjb-text'}):
            key_words_description.append(job_descriptions.get_text())
        for item in key_words_description:
            clean_description.append(item.replace('\n','').replace('\r','').replace('\r+',''))
        for provider in job_soup.find_all('h2', attrs={'class': 'wpjb-top-header-title jobsub'}):
            provider_info.append(provider.get_text().replace('\n','').replace('\r','').replace('\r+','').strip())
        # print(providers)
        for posted_date in job_soup.find_all('div', attrs={'style': "font-size:12px;margin-bottom:0"}):
            provider_info.append(posted_date.get_text().replace('\n','').replace('\r','').replace('\r+','').strip())
        for website_info in job_soup.find_all("div", attrs={'class': 'wpjb-top-header-subtitle'}):
            for href in website_info.find_all('a'):
                provider_info.append(href.attrs['href'])
        # for email_info in job_soup.find_all("div", attrs={'class': 'wpjb-top-header-subtitle'}):
        #     for email in email_info.find_all('i'):
                # print(email.attrs['class'].get_text())





            # provider_info.append(posted_date.get_text().replace('\n','').replace('\r','').replace('\r+','').strip())
        # provider_info.clear()

        #     provider_info.append(p_info.get_text().replace('\n','').replace('\r','').replace('\r+','').strip())
        # print(provider_info)

        # # for index in range(len(key_words)):
        #     print(key_words[index])
        #     print(clean_description[index])
        #     print('-------------------------')

        info = {"Provider":provider_info,"Section":key_words, "Description":clean_description}
        df = pd.DataFrame.from_dict(info, orient='index')
#
# #
        df = df.transpose()
#         # df.loc[[len(df)], 'Section'] = ' '
        # df.loc[[len(df)], 'Description'] = ' '
        master_df_list.append(df)
#         print(df)
# #
        job_links.pop(0)
        key_words.clear()
        key_words_description.clear()
        clean_description.clear()
        provider_info.clear()
#
todays_df = pd.concat(master_df_list)

# print(todays_df)
todays_df.to_csv(r'C:\Users\Charles\Desktop\China_' + str(date.today()) + '.csv', index = True)
#
#
#
#

