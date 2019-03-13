import json
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

		self.dao = ProjectDAO()

		if parts[0] == "drag_drop":
			return self.drag_drop()

		card_id = int(parts[0])
		if card_id == 0:
			card = self.dao.get_new()
		else:
			card = self.dao.load_card(card_id)

		return self.save_zoomed_card(card)

	def save_zoomed_card(self, card):
		if "title" not in self.form_fields or "list_index" not in self.form_fields:
			return response.Response400BadRequest()

		card["list_index"] = int(self.form_fields["list_index"])
		card["title"] = self.form_fields["title"]
		if "description" in self.form_fields:
			card["description"] = self.form_fields["description"]

		self.dao.save_card(card)

		return response.Response301Redirect("/")

	def drag_drop(self):
		if "list_index" not in self.form_fields or "ids" not in self.form_fields:
			return response.Response400BadRequest()

		list_index = self.form_fields["list_index"]
		ids = json.loads(self.form_fields["ids"])

		n = 0
		for card_id in ids:
			card = self.dao.load_card(card_id)
			card["list_index"] = list_index
			card["position"] = n
			n += 1

		self.dao.project["cards"] = sorted(self.dao.project["cards"], key=lambda x: list(x.values())[2])
		self.dao.save()

		return response.Response204NoContent()
