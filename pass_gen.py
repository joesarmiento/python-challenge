from cipher import Cipher 
cipher = Cipher(2)
Pass = input('enter a password: ')
new_pass = cipher.encode(Pass)
print (new_pass)


