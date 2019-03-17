import json
from bottle import abort, request, template, HTTPResponse
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
		if "list_ids" not in request.forms:
			abort(400)

		list_ids = json.loads(request.forms.list_ids)

		self.dao.reorder_lists(list_ids)
		return HTTPResponse(status=204)
