import json
import response
from dao.user import UserDAO
from controllers.base import Controller

class UsersController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, method, parts):
		if method == "get":
			return self.index()
		else:
			return self.save()

	def index(self):
		dao = UserDAO()
		users = dao.load_all()
		return response.ResponseView(
			"users",
			{
				"%users%" : json.dumps(users)
			}
		)

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
