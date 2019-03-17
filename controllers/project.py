import json
from bottle import request, template, HTTPResponse
from controllers.base import Controller
from dao.project import ProjectDAO

class ProjectController(Controller):
	def __init__(self):
		self.dao = ProjectDAO()

	def main_page(self):
		return template(
			"project",
			project_name = self.dao.project["name"],
			project = json.dumps(self.dao.project)
		)

	# POST /name
	def rename_project(self):
		if "name" not in request.forms:
			abort(400)

		name = request.forms.name

		self.dao.project_rename(name)
		return HTTPResponse(status=204)

	# POST /drag_drop
	def drag_drop(self):
		if "list_id" not in request.forms\
		or "card_ids" not in request.forms:
			abort(400)

		list_id = request.forms.list_id
		card_ids = json.loads(request.forms.card_ids)

		self.dao.reorder_cards(list_id, card_ids)
		return HTTPResponse(status=204)
