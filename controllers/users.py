import json
import response
from dao.user import UserDAO
from models.user import UsersModel
from controllers.base import Controller

class UsersController(Controller):
	def __init__(self):
		pass

	def do_GET(self, parts):
		if len(parts) == 1:
			# /users = index of all users
			return self.index()
		else:
			# /users/<username> = <username>'s settings
			return self.get(parts[1])

	def index(self):
		return response.ResponseView("users")

	def get(self, username):
		dao = UserDAO()
		if not dao.exists(username):
			return response.Response404NotFound()

		user = dao.load(username)
		return response.ResponseView(
			"user",
			{
				"%username%" : user["username"],
				"%email%" : user["email"]
			}
		)

	def do_POST(self):
		pass
