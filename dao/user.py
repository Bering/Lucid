import os
import json
import unidecode

class UserDAO:
	def __init__(self):
		subfolder = "data"
		if not os.path.exists(subfolder):
			os.makedirs(subfolder)

		self.file = os.path.join(subfolder, "users.json")
		if not os.path.exists(self.file):
			fh = open(self.file, "w+")
			fh.write(json.dumps({}))
			fh.close()

	def get_new(self):
		return {
			"username" : "",
			"email" : ""
		}

	def load_all(self):
		fh = open(self.file, "r")
		result = json.loads(fh.read())
		fh.close()
		return result

		return {
			"bering" : {
				"username" : "bering",
				"email" : "bering@ringlogic.com"
			},
			"phil" : {
				"username" : "phil",
				"email" : "bering@ringlogic.com"
			}
		}

	def exists(self, username):
		return username in self.load_all()

	def load(self, username):
		return self.load_all()[username]

	def save(self, user):
		user["username"] = unidecode.unidecode(user["username"])

		users = self.load_all()
		users[user["username"]] = user

		fh = open(self.file, "w")
		fh.write(json.dumps(users, indent=4))
		fh.close()

	def delete(self, username):
		users = self.load_all()
		del users[username]

		fh = open(self.file, "w")
		fh.write(json.dumps(users))
		fh.close()
