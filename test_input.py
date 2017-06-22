# Starting to write python

#name=input('Enter Name')
#print('hello', name)


                

#password program
def main_menu():
    print('Enter "New" for New Account')
    print('Enter "Login" to access program')
    print('Enter "Exit" to exit program')

user_login = {'Josh': 'jigger', 'Jenny':'asstastic'}

user_name = None
user= None
password= None
enter_pass= None
menu_choice= None
pasword1= None
Paswor2= None

###New Account
while menu_choice != 'Exit':
    menu_choice = input('Enter Command: ')
    if menu_choice == 'New':
        user= input('User Name: ')
        password1= input('Create a Password: ')
        password2= input('Retype Pasword:')
        if password1 == password2:
            password=password2
            user_login[user]=password
        else:
            print("Password doesn't Match")
            

### LOGIN Script
    elif menu_choice == 'Login':

        user= input('User Name: ') 
        if user in user_login:
                password= user_login[user]
        else:
            print('No User Login Found. Please Create an Account or Try Again')

        while enter_pass != password:
            enter_pass = input('Enter Password: ')
        
        print ('Good Morning', user)

### Delete Account
    elif menu_choice == 'Remove':
        user=input('User to be Removed: ')
        if user in user_login:
            del user_login[user]
        else:
            print('User not Found')
        
    
   
    
   
    

        


#    if password != 'jigger':
#        pcount= pcount-1
#    if pcount < 1:       
#        print ("You're not", user_name)


          
