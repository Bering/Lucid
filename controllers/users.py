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

	def save(self):
		if "username" not in self.form_fields:
			return response.Response400BadRequest()

		username = self.form_fields["username"]
		
		if "email" not in self.form_fields:
			email = ""
		else:
			email = self.form_fields["email"]
		
		dao = UserDAO()
		if not dao.exists(username):
			user = dao.get_new()
		else:
			user = dao.load(username)

		user["username"] = username
		user["email"] = email
		dao.save(user)

		return response.Response301Redirect("/users")
