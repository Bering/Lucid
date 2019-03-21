from __future__ import absolute_import
import json
from bottle import abort, request, HTTPResponse
from dao.project import ProjectDAO

class CardController():
	def __init__(self):
		self.dao = ProjectDAO()

	def read_form_fields(self, card):
		if "id" not in request.forms:
			raise KeyError("Missing id in request")
		if "title" not in request.forms:
			raise KeyError("Missing title in request")
		if "list_id" not in request.forms:
			raise KeyError("Missing list_id in request")

		card["id"] = request.forms.id
		card["list_id"] = request.forms.list_id
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

		self.dao.append_card(card)
		return HTTPResponse(status=201)

	def prepend(self):
		card = self.dao.get_new_card()
		card = self.read_form_fields(card)

		self.dao.prepend_card(card)
		return HTTPResponse(status=201)

	def save(self, card_id):
		card = self.dao.load_card(card_id)
		card = self.read_form_fields(card)

		self.dao.save_card(card)
		return HTTPResponse(status=204)

	def delete(self, card_id):
		card = self.dao.load_card(card_id)
		self.dao.delete_card(card)
		return HTTPResponse(status=204)

	def drag_drop(self):
		if "list_id" not in request.forms\
		or "card_ids" not in request.forms:
			abort(400)

		list_id = request.forms.list_id
		card_ids = json.loads(request.forms.card_ids)

		self.dao.reorder_cards(list_id, card_ids)
		return HTTPResponse(status=204)
