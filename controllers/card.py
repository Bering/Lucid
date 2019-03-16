import response
from dao.project import ProjectDAO
from controllers.base import Controller

class CardController(Controller):
	def handle_request(self, request):
		self.request = request
		self.dao = ProjectDAO()

		card_id = int(request.path_parts[1])
		if card_id == 0:
			card = self.dao.get_new_card()
		else:
			card = self.dao.load_card(card_id)

		if request.method == "post":
			return self.save_zoomed_card(card)
		elif request.method == "delete":
			return self.delete(card)
		else:
			return response.Response400BadRequest()

	def save_zoomed_card(self, card):
		if "title" not in self.request.form_fields\
		or "list_id" not in self.request.form_fields:
			return response.Response400BadRequest()
		
		card["list_id"] = int(self.request.form_fields["list_id"])
		card["title"] = self.request.form_fields["title"]
		if "description" in self.request.form_fields:
			card["description"] = self.request.form_fields["description"]

		card["labels"] = []
		if "label1" in self.request.form_fields:
			card["labels"].append(1)
		if "label2" in self.request.form_fields:
			card["labels"].append(2)
		if "label3" in self.request.form_fields:
			card["labels"].append(3)
		if "label4" in self.request.form_fields:
			card["labels"].append(4)
		if "label5" in self.request.form_fields:
			card["labels"].append(5)
		if "label6" in self.request.form_fields:
			card["labels"].append(6)

		self.dao.save_card(card)
		return response.Response301Redirect("/")

	def delete(self, card):
		self.dao.delete_card(card)
		return response.Response204NoContent()
