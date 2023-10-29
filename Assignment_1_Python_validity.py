#!/usr/bin/env python
# coding: utf-8

# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password: 
# 1. At least 1 letter between [a-z] 
# 2. At least 1 number between [0-9] 
# 3. At least 1 letter between [A-Z] 
# 4. At least 1 character from [$#@_&%] 
# 5. Minimum length of transaction password: 6 
# 6. Maximum length of transaction password: 12

# In[1]:


#This pythom program defines a function called valid_password to check if passwords given by users of a website meets the underlisted criteria:
# At least 1 letter between [a-z] 
# At least 1 number between [0-9] 
# At least 1 letter between [A-Z] 
# At least 1 character from [$#@_&%] 
# Minimum length of transaction password: 6 
# Maximum length of transaction password: 12

#This program will utilise a Python module called regular expression

import re

def valid_password(password):
    '''defined a function called valid_password'''
    if 6 <= len(password) <= 12:
        '''checks that the password length is between 6 and 12'''
        if re.search('[a-z]', password):
            '''checks if password contains at least one lowercase letter'''
            if re.search('[A-Z]', password):
                '''checks if the password contains at least one uppercase letter'''
                if re.search('[0-9]', password):
                    '''checks if the passowrd contains at least one number'''
                    if re.search('[$#@_&%]', password):
                        '''checks if the password contains at least one special character'''
                        return True
                        '''returns true if the password meets the above criteria'''
    return False
    '''returns false if password does not meet the above criteria'''
    
    
    
# When a user inputs a password
password = input('Enter a password:')

if valid_password(password):
    '''if the passowrd meets the above criteria, the if statement will run'''
    print ('Password is valid! Welldone')
else:
    '''if the password does not meet the above criteria, the else statement will run'''
    print('Password is not valid, sorry try again!')
                    
                
        


# In[ ]:




