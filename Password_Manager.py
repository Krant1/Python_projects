import re
class PasswordManager(object):
    def __init__(self):
        self.password_dict={}
    def view(self):
        try:
            f=open('Password.txt','r')
            for lines in f.readlines():
                print(lines)
        finally:
            f.close()

    def add(self):
        while True:
            self.pattern=re.compile(r'([A-Za-z0-9$%#@]{7,}[0-9])')
            self.name_of_site=input('Enter the name of the site: ')
            self.password_of_site=str(input('Enter the password: '))
            if self.pattern.search(self.password_of_site)==None:
                print('''The password doesn\'t satisfy either of the criterion:
                1. Must have an uppercase character
                2. Must have a number
                3. Must have a special character 
                4. Must be more than 8 characters long''')
            self.password_dict.update({self.name_of_site:self.password_of_site})
            self.continue_question=input('Press "Enter" to continue or "q" to quit ')
            if self.continue_question=='q':
                break
            else:
                continue
        try:
            f=open('Password.txt','a')
            f.write(str(self.password_dict))
        finally:
            f.close()

    def modify(self):
        self.site_name=input('Enter the site\'s name whose password you want to modify: ')
        if self.site_name in self.password_dict.keys():
            self.verify_old_password=input('Enter the old password: ')
            if self.verify_old_password==self.password_dict.get(self.site_name):
                self.site_password=input('Enter the new password: ')
                self.password_dict.update({self.site_name:self.site_password})
        else: print('The entered site does not exits, please try again')
        try:
            f=open('Password.txt','w+')
            f.write(self.password_dict)
        finally:
            f.close()
            

class User:
    def __init__(self,master_password):
        self.name=input('Enter your name: ')
        self.age=input('Enter your age: ')
        self.master_password=master_password
        self.password_manager=PasswordManager()

    def process(self):
        self.ask_master_password=input('Please enter master password: ')
        if self.ask_master_password==self.master_password:
            print('The password you entered is correct')
            while True:
                print('''
                Choose any one of the following operations:
                A) View: View the list of passwords
                B) Add: Add a new password
                C) Modify: Modifies an existing password
                D) Quit
                ''')
                self.choose_option=input('Which option do you choose? ')
                if self.choose_option.upper()=='A':
                    self.password_manager.view()
                elif self.choose_option.upper()=='B':
                    self.password_manager.add()
                elif self.choose_option.upper()=='C':
                    self.password_manager.modify()
                elif self.choose_option.upper()=='D':
                    break
                else:
                    print('Invalid option,please enter again')
                    continue
        else:
            print('Invalid master password,please try again')
                

user_1=User('sierra')
user_1.process()
