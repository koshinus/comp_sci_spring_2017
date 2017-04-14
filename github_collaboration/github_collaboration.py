from github import Github
from Crypto.Cipher import AES

f = open('password.txt', 'r')
passw = f.readline()
f.close()

encrypter = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
decrypter = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

g = Github("koshinus", decrypter.decrypt(encrypter.encrypt(passw)))
#g = Github("Your login", "Your password")

for repo in g.get_user("koshinus").get_repos():
	print repo.get_commits()