from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "http://www.mfd.gov.np/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

right_table=soup.find('table', class_='table')

#Generate lists
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    #states=row.findAll('th') #To store second column data
    if len(cells)==4: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        #B.append(states[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))


df=pd.DataFrame(A,columns=['Station'])
df['Max']=B
df['Min']=C
df['Rain']=D
print(df)

df.to_csv('out.csv')

