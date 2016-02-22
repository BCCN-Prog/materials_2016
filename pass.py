import pickle
from getpass import getpass

def read_pswdb(pswdb_file):
    pswdb = pickle.load(pswdb_file)
    return pswdb

def write_pswdb(pswdb, pswdb_file):
    pickle.dump(pswdb, pswdb_file)

def get_credentials():
    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    return (username, password)

def authorize(username, password, pswdb):
    if username in pswdb:
        if password == pswdb[username]:
            return True
    return False


pswdb_file = open('pswdb', 'rb+')
username, password = get_credentials()
pswdb = read_pswdb(pswdb_file)
if authorize(username, password, pswdb):
    print('Authorization succeeded!')
else:
    print('Wrong username or password')

#pswdb.write(username+' '+password+'\n')
#pswdb.close()
#pswdb[username] = password
