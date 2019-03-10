import response
from dao.user import UserDAO
from dao.project import ProjectDAO
from dao.card import CardDAO
from controllers.base import Controller

class CardsController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def do_POST(self, parts):
		username = parts[0]
		dao = UserDAO()
		if not dao.exists(username):
			return response.Response404NotFound()

		project_name = parts[1]
		dao = ProjectDAO()
		if not dao.exists(username, project_name):
			return response.Response404NotFound()

		card_id = parts[2]
		dao = CardDAO()
		if not dao.exists(card_id):
			return response.Response404NotFound()

		title = self.form_fields.getfirst("title", "")
		description = self.form_fields.getfirst("description", "")
		dao.update(card_id, title, description)

		return response.Response301Redirect("/" + username + "/" + project_name)
