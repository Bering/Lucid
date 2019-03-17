from bottle import request, HTTPResponse
from dao.project import ProjectDAO
from controllers.base import Controller

class ListController(Controller):
	def __init__(self):
		self.dao = ProjectDAO()

	# POST /list
	def create(self):
		if "name" not in request.forms:
			abort(400)

		name = request.forms.name

		self.dao.create_list(name)
		return HTTPResponse(status=201)

	# POST /list/<list_id>
	def rename(self, list_id):
		if "name" not in request.forms:
			abort(400)

		name = request.forms.name

		self.dao.rename_list(list_id, name)
		return HTTPResponse(status=204)

	# DELETE /list/<list_id>
	def delete(self, list_id):
		self.dao.delete_list(list_id)
		return HTTPResponse(status=204)
