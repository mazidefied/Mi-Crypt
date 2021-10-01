# Mi-Crypt v0.1

# Author info: 
# Github| @mile403



# import cryptography module for encrypting/decrypting
from cryptography.fernet import Fernet

import sys # import sys library for closing the program

import time # import time library(to add a delay when encrypting/decrypting)

import tqdm # import the tqdm library for progress bar

# tqdm progresa bar functions
def work1():
    time.sleep(1.1)
def work2():
    time.sleep(2)
    print('fetching cipher resources...')
def work3():
    time.sleep(1.)
def work4():
    time.sleep(1.4)
    print('creating ciphertext....')
def work5():
    time.sleep(0.5)
def work6():
    time.sleep(0.6)
    print('loading Mi-Crypttext.....')
def work7():
	time.sleep(0.7)
def work8():
	time.sleep(0.8)
def work9():
	time.sleep(0.9)
def work10():
	time.sleep(1)
def worker():
    work_set = [work1,work2,work3,work4,work5,work6,work7,work8,work9,work10]
    return work_set

def prog_bar(): # main tqdm progress bar function
    a = worker()
    for i in tqdm.tqdm(range(10)):
        b = a[i]()

key = Fernet.generate_key()
f = Fernet(key)
print('Mi-Crypt v0.1')

if __name__ == '__main__':
	    print('\nWrite A Text You Want To enCRYPT: ')
	    user_input = input()
	    time.sleep(1)
	    print('\nCreate a SECRET KEY(Choose Any Number): ') # create a key you will use to decrypt your string
	    s_key = int(input())
	    inp_str = str.encode(user_input) # user input will be taken in as bytes
	    token = f.encrypt(inp_str)
	    time.sleep(1)
	    print('please wait...')
	    prog_bar() # calling tqdm progress bar
	    time.sleep(1)
	    print('TeXt enCRYPTion complete!')
	    time.sleep(1)
	    print(f'\nMi-Crypttext: {token} ')
	    time.sleep(2)
	    print('\nEnter your SECRET KEY to deCRYPT the Mi-Crypttext: ')
	    s_key_dcrpt = input()
	    if s_key_dcrpt == str(s_key):
	    	time.sleep(1)
	    	print('Mi-Crypttext has been decrypted!: \n', f.decrypt(token))
	    else:
	    	time.sleep(1)
	    	sys.exit('INVALID SECRET KEY!')
	    	

	    	
# Thank you for using Mi-Crypt!	    	
# ©2021
