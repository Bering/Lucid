class UserDAO:
	def __init__(self):
		pass

	def load_all(self):
		# TODO: SQLite
		return {
			"bering" : {
				"username" : "bering",
				"email" : "bering@ringlogic.com"
			}
		}

	def exists(self, username):
		return username in self.load_all()

	def load(self, username):
		return self.load_all()[username]

	def add(self, username):
		pass

	def update(self, username):
		pass

	def delete(self, username):
		pass
