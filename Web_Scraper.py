import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
url='https://www.iplt20.com/points-table/men/2021'
r=requests.get(url)
ipl_content=r.content
soup=BeautifulSoup(ipl_content,'html.parser')
team_name=[]
team_pld=[]
team_stats=[]
team_pts=[]
team_matrix=[]
ipl_points_table=PrettyTable(['Team','Pld','Won','Lost','Tied','N/R','For','Against','Pts'])
for names in soup.find_all('span',class_='standings-table__team-name js-team'):
    team_name.append(names.get_text())
for pld in soup.find_all('td',class_='standings-table__padded'):
    team_pld.append(pld.get_text())
for stats in soup.find_all('td',class_='standings-table__optional'):
    team_stats.append(stats.get_text())
for points in soup.find_all('td',class_='standings-table__highlight js-points'):
    team_pts.append(points.get_text())
count=0
while True:
    team_matrix.append(team_stats[count:count+6])
    count+=6
    if count>42:
        break
for i in range(8):
    team_matrix[i].insert(0,team_pld[i])
    team_matrix[i].insert(0,team_name[i])
    team_matrix[i].append(team_pts[i])
for i in range(8):
    ipl_points_table.add_row(team_matrix[i])
print(ipl_points_table)

    
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

#Using from_html_one in PrettyTable
from prettytable import from_html_one
import requests
url='https://www.iplt20.com/points-table/men/2021'
r=requests.get(url)
print(from_html_one(r.text))

