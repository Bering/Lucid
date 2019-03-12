import response
from dao.project import ProjectDAO
from dao.cards import CardsDAO
from controllers.base import Controller

class CardsController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, method, parts):
		if method == "get":
			return response.Response400BadRequest()

		dao = ProjectDAO()

		card_id = int(parts[0])
		if card_id == 0:
			card = dao.get_new()
		else:
			card = dao.load_card(card_id)

		if not card:
				return response.Response404NotFound()

		if "title" not in self.form_fields or "list_index" not in self.form_fields:
			return response.Response400BadRequest()

		card["list_index"] = int(self.form_fields["list_index"])
		card["title"] = self.form_fields["title"]
		if "description" in self.form_fields:
			card["description"] = self.form_fields["description"]

		dao.save_card(card)

		return response.Response301Redirect("/")
