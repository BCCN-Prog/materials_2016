import pickle
from getpass import getpass

def read_pswdb(pswdb_file):
    try:
        pswdb = pickle.load(pswdb_file)
    except EOFError:
        pswdb = {}
    return pswdb

def write_pswdb(pswdb, pswdb_file):
    pickle.dump(pswdb, pswdb_file)

def get_credentials():
    username = input('Enter your username: ')
    password = getpass('Enter your password: ')
    return (username, password)

def authorize(username, password, pswdb):
    print(username, password)
    if username in pswdb:
        if password == pswdb[username]:
            return True
    print(pswdb)
    return False

def create_new_user(username, password, paswdb, pswdb_file):
    pswdb[username] = password
    write_pswdb(pswdb, pswdb_file)

pswdb_file = open('pswdb', 'rb+')



username, password = get_credentials()
pswdb = read_pswdb(pswdb_file)
if authorize(username, password, pswdb):
    print('Authorization succeeded!')
else:
    create_new_user(username, password, pswdb, pswdb_file)
    print('Wrong username or password')
