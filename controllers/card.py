from bottle import request, HTTPResponse
from dao.project import ProjectDAO
from controllers.base import Controller

class CardController(Controller):
	def __init__(self):
		self.dao = ProjectDAO()

	def read_form_fields(self, card):
		if "title" not in request.forms\
		or "list_id" not in request.forms:
			return None

		card["list_id"] = int(request.forms.list_id)
		card["title"] = request.forms.title
		if "description" in request.forms:
			card["description"] = request.forms.description

		card["labels"] = []
		for n in range(6):
			if "label"+str(n+1) in request.forms:
				card["labels"].append(n+1)

		return card

	def append(self):
		card = self.dao.get_new_card()
		card = self.read_form_fields(card)

		if card == None:
			abort(400)

		self.dao.append_card(card)
		return HTTPResponse(status=201)

	def prepend(self):
		card = self.dao.get_new_card()
		card = self.read_form_fields(card)

		if card == None:
			abort(400)

		self.dao.prepend_card(card)
		return HTTPResponse(status=201)

	def save(self, card_id):
		card = self.dao.load_card(card_id)
		card = self.read_form_fields(card)
		
		if card == None:
			abort(400)

		self.dao.save_card(card)
		return HTTPResponse(status=204)

	def delete(self, card_id):
		card = self.dao.load_card(card_id)
		self.dao.delete_card(card)
		return HTTPResponse(status=204)
