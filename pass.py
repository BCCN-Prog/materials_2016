import pickle
from getpass import getpass

def read_pswdb(pswdb_file):
    try:
        pswdb = pickle.load(pswdb_file)
        pswdb_file.seek(0)
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
    #print(username, password)
    if username in pswdb:
        if pwhash(password) == pswdb[username]:
            return True
    #print(pswdb)
    return False

def pwhash(password):
    hash_ = 0
    for idx, char in enumerate(password):
        hash_ += (idx+1)*ord(char)
    return hash_

def create_new_user(username, password, paswdb, pswdb_file):
    if username in pswdb:
        raise Exception('Unsername already exists [%s]' %username)
    else:
        pswdb[username] = pwhash(password)
        write_pswdb(pswdb, pswdb_file)

try:
    pswdb_file = open('pswdb', 'rb+')
except FileNotFoundError:
    pswdb_file = open('pswdb', 'wb+')

username, password = get_credentials()
pswdb = read_pswdb(pswdb_file)

if authorize(username, password, pswdb):
    print('Authorization succeeded!')
else:
    print('Wrong username or password')
    ans = input('Create new user [y/n]? ')
    if ans == 'y':
        create_new_user(username, password, pswdb, pswdb_file)
    else:
        print('Exit!')

print(pswdb)
