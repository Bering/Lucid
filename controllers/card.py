import response
from dao.project import ProjectDAO
from controllers.base import Controller

class CardController(Controller):
	def handle_request(self, request):
		self.request = request
		self.dao = ProjectDAO()

		if request.method == "post":
			if request.path_parts[1] == "append":
				return self.append()
			elif request.path_parts[1] == "prepend":
				return self.prepend()
			else:
				card_id = int(request.path_parts[1])
				return self.save_zoomed_card(card_id)
		elif request.method == "delete":
			card_id = int(request.path_parts[1])
			return self.delete(card_id)
		else:
			return response.Response400BadRequest()

	def append(self):
		card = self.dao.get_new_card()
		card = self.read_form_fields(card)

		if card == None:
			return response.Response400BadRequest()

		self.dao.append_card(card)
		return response.Response201Created("/")

	def prepend(self):
		card = self.dao.get_new_card()
		card = self.read_form_fields(card)

		if card == None:
			return response.Response400BadRequest()

		self.dao.prepend_card(card)
		return response.Response201Created("/")

	def save_zoomed_card(self, card_id):
		card = self.dao.load_card(card_id)
		card = self.read_form_fields(card)
		
		if card == None:
			return response.Response400BadRequest()

		self.dao.save_card(card)
		return response.Response204NoContent()

	def read_form_fields(self, card):
		if "title" not in self.request.form_fields\
		or "list_id" not in self.request.form_fields:
			return None

		card["list_id"] = int(self.request.form_fields["list_id"])
		card["title"] = self.request.form_fields["title"]
		if "description" in self.request.form_fields:
			card["description"] = self.request.form_fields["description"]

		card["labels"] = []
		for n in range(6):
			if "label"+str(n+1) in self.request.form_fields:
				card["labels"].append(n+1)

		return card

	def delete(self, card_id):
		card = self.dao.load_card(card_id)
		self.dao.delete_card(card)
		return response.Response204NoContent()
