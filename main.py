import os
import string
import secrets

banned_usernames = ['porn', 'sex', 'sexy', 'kiss', 'fuck', 'marijuanna', 'weed', 'drugs', 'cocaine', 'meth', 'methamphetamine', 'feet', 'babe', 'makeout']

def display ():
    print ('Password Manager \n')

    print ('[1] Generate New Password')
    print ('[2] Search for Password')
    print ('[3] Save your Existing Password')
    command = input ('Option: ')

    try:
        command = int (command)

    except:
        os.system ('clear')
        print ('Sorry! Option invalid.')

    if command == 1:
        generate ()

    elif command == 2:
        search ()

    else:
        existing ()


def generate ():
    os.system ('clear')
    length = input ('How long do you want your password to be?: ')

    try: 
        length = int (length)

    except:
        os.system ('clear')
        print ('That may be out of my capabilities at the moment.')

    os.system ('clear')
    alphabet = string.ascii_letters + string.digits
    passw = ''.join(secrets.choice(alphabet) for i in range(length))
  
    print ('Your generated password is '+passw)
    print ('Would you like to save it?')
    savetrue = input ('[1] Yes [2] No: ')


    if savetrue == '1':
        print ('1')
        passw = str (passw)
        os.system ('clear')
        username = input ('Username: ')
        print ('Password: '+passw)
        context = input ('Context: ')
        save (username, context, passw)

    elif savetrue == '2':
        print ('2')

    else:
        print ('Option invalid.')

    
    

def search():
    global value
    value = -1  # default value if no match is found
    os.system('clear')
    context = input('Context: ')

    with open('context.txt', 'r') as f:
        contextList = [line.strip() for line in f.readlines()]
        for i in range(1, len(contextList)):
            if contextList[i].strip() == context:
                value = i
                break

    if value != -1:  # check if a match was found
        with open('users.txt', 'r') as h:
            usersList = h.readlines()
            username = usersList[value].strip()

        with open('passwords.txt', 'r') as e:
            passwordsList = e.readlines()
            password = passwordsList[value].strip()

        os.system('clear')
        print("Username: " + username)
        print("Password: " + password)
        print("Context: " + context)
    else:
        os.system('clear')
        print("No matching context found.")



def existing ():
    os.system ('clear')
    username = input ('Username: ')
    if username != banned_usernames:
        context = input ('Context: ')
        password = input ('Password: ')

    else:
        os.system ('clear')
        print ('Dear customer, your desired username is deemed inappropriate. Please replay the programme, and choose a more family-friendly surname. :)')

    save (username, context, password)



def save (username, context, password):
    with open ('passwords.txt', 'a') as f:
        f.write (password+'\n')

    with open ('context.txt', 'a') as x:
        x.write (context+'\n')

    with open ('users.txt', 'a') as y:
        with open ('context.txt', 'a') as x:
            x.write (context+'\n')

    with open ('users.txt', 'a') as y:
        y.write (username+'\n')

    os.system ('clear')
    print ('Done! You can search for your account through your context later!')



display()