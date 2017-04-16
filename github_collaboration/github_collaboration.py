from github import Github, GithubException
from Crypto.Cipher import AES
from graphviz import Digraph

f = open('password.txt', 'r')
passw = f.readline()
f.close()

encrypter = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
decrypter = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

g = Github("koshinus", decrypter.decrypt(encrypter.encrypt(passw)))
# g = Github("Your login", "Your password")

user_list = ['koshinus', 'kostaNew', 'proAlexander']
user_dict = {}
for user in user_list:
	try:
		for repo in g.get_user(user).get_repos():
			try:
				user_dict[user] += [repo]
			except KeyError:
				user_dict[user] = [repo]
	except GithubException:
		continue

dot = Digraph("Collaboration Graph")
dot.attr('node', shape='box')

for user in user_dict.keys():
	for repo in user_dict[user]:
		dot.node(str(repo.name))
		# print str(repo)
	dot.node(str(user))
	# print str(user)

for user in user_dict.keys():
	for repo in user_dict[user]:
		for user1 in user_dict.keys():
			try:
				if user1 in map(lambda x: str(x._author.value.login),
								list(g.get_user(str(user1)).get_repo(str(repo.name)).get_commits())):
					dot.edge(str(user1), str(repo.name))
			except AttributeError, GithubException:
				continue

dot.render('Collaboration Graph', None, True)

# print map(lambda x: str(x._author.value.login), list(g.get_user("koshinus").get_repo("perl_imkn").get_commits()))
