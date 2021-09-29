import re
import requests
from bs4 import BeautifulSoup
import pyperclip as pc
phone_match=[]
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol  
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)
url=input('Enter the url you want us to find email and phone number from: ')
r=requests.get(url)
content=r.content
soup=BeautifulSoup(content,'html.parser')
with open('net_content.txt','w') as net_file:
    net_file.write(str(soup))
with open('net_content.txt','r') as net_file:
    content=net_file.read()
    phone_numbers=phone_regex.findall(content)
    for line in phone_numbers:
        list(line).remove('')
        phone_match.append(''.join(line))
    for phone in phone_match: 
        print(f'Phone Number Matches:{phone}')
    for mail in email_regex.findall(content):
        print(f'Email Matches:{mail}')

    

    
