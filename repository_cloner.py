import pandas as pd
import requests 
from datetime import datetime
df = pd.DataFrame(columns=['repository_ID', 'name', 'URL', 'created_date',  'description'])

# get HTTP links for the python repositories

for i in range(4,8):
        results = requests.get(url='https://api.github.com/search/repositories?q=language:python&sort=forks&order=desc&page='+str(i),headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }).json()
        try:
                for repo in results['items']:
                        d_tmp = {'repository_ID': repo['id'],
                                'name': repo['name'],
                                'URL': repo['html_url'],
                                'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                                }
                        # print(len(df))
                        print(d_tmp['URL'])
                        df = df.append(d_tmp, ignore_index=True)
        except:
                print("error occured")
        # print(len(df))
        df = df.append(d_tmp, ignore_index=True)
        print(len(df))


# clone the repositories
print(len(df))
print("-----------------------------------------------------------------")
# print(df[0:10])
# f=open("list2",'w')
# print("Cloning...")

# for i in range(len(df)):
#         f.write(df['URL'][i])
#         f.write('\n')
# Opening a file 
file = open("list2","r") 
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1

print("No. of repositories: ",Counter)



import os
from git.repo.base import Repo
for i in range(Counter):
        print(i)
        try:
                os.mkdir("/home/sachendra/TSE/T2/"+df['name'][i])
                Repo.clone_from(df['URL'][i],"/home/sachendra/TSE/T2/"+df['name'][i])
        except:
                pass
# Repo.clone_from("https://github.com/panthap2/LearningToUpdateNLComments.git", "/home/sachendra/T")
# print(d_tmp)
# print(df['URL'][300:399])

# print(df['name'])