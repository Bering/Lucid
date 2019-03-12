import response
from dao.project import ProjectDAO
from dao.cards import CardsDAO
from controllers.base import Controller

class CardsController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, parts):
		card_id = parts[0]
		dao = CardsDAO()
		if not dao.exists(card_id):
			return response.Response404NotFound()

		title = self.form_fields.getfirst("title", "")
		description = self.form_fields.getfirst("description", "")
		dao.update(card_id, title, description)

		return response.Response301Redirect("/")
