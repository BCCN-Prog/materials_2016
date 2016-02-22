import pickle
import os
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

def authorize(username, pass_text, pswdb):
    #print(username, password)
    if username in pswdb:
        salt = pswdb[username][1]
        if pwhash(pass_text, salt) == pswdb[username][0]:
            return True
    #print(pswdb)
    return False

def pwhash(pass_text, salt):
    hash_ = 0
    full_pass_text = pass_text + salt
    for idx, char in enumerate(full_pass_text):
        hash_ += (idx+1)*ord(char)
    return hash_

def create_new_user(username, password, salt, paswdb, pswdb_file):
    if username in pswdb:
        raise Exception('Unsername already exists [%s]' %username)
    else:
        pswdb[username] = (pwhash(password,salt), salt)
        write_pswdb(pswdb, pswdb_file)

def create_individual_salt():
    # make a longer salt
    salt = ''
    for i in range(1,10):
        salt = salt + chr(int.from_bytes(os.urandom(1), 'little'))
    return salt

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
        salt = create_individual_salt()
        create_new_user(username, password, salt, pswdb, pswdb_file)
    else:
        print('Exit!')

print(pswdb)
