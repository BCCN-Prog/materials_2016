from getpass import getpass

username = input('Enter your username: ')
password = getpass('Enter your password: ')

pswdb = open('pswdb', 'wb')
#pswdb.write(username+' '+password+'\n')
#pswdb.close()
pswdb[username] = password
pickle.dump(pswdb, pswdb_file)
