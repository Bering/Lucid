import json
import response
from dao.project import ProjectDAO
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
			card = self.dao.get_new_card()
		else:
			card = self.dao.load_card(card_id)

		if method == "delete":
			return self.delete(card)
		else:
			return self.save_zoomed_card(card)

	def save_zoomed_card(self, card):
		if "title" not in self.form_fields or "list_index" not in self.form_fields:
			return response.Response400BadRequest()
		
		card["list_index"] = int(self.form_fields["list_index"])
		card["title"] = self.form_fields["title"]
		if "description" in self.form_fields:
			card["description"] = self.form_fields["description"]

		card["labels"] = []
		if "label1" in self.form_fields:
			card["labels"].append(1)
		if "label2" in self.form_fields:
			card["labels"].append(2)
		if "label3" in self.form_fields:
			card["labels"].append(3)
		if "label4" in self.form_fields:
			card["labels"].append(4)
		if "label5" in self.form_fields:
			card["labels"].append(5)
		if "label6" in self.form_fields:
			card["labels"].append(6)

		self.dao.save_card(card)
		return response.Response301Redirect("/")

	def drag_drop(self):
		if "list_index" not in self.form_fields or "ids" not in self.form_fields:
			return response.Response400BadRequest()

		list_index = self.form_fields["list_index"]
		ids = json.loads(self.form_fields["ids"])

		self.dao.reorder_cards(list_index, ids)
		return response.Response204NoContent()

	def delete(self, card):
		self.dao.delete_card(card)
		return response.Response204NoContent()
