import response
from dao.project import ProjectDAO
from controllers.base import Controller

class ListController(Controller):
	def handle_request(self, request):
		self.request = request
		self.dao = ProjectDAO()

		if len(request.path_parts) == 1:
			if request.method == "post":
				return self.create()
			else:
				return response.Response400BadRequest()

		list_index = int(request.path_parts[1])

		if request.method == "post":
			return self.rename(list_index)
		elif request.method == "delete":
			return self.delete(list_index)
		else:
			return response.Response400BadRequest()

	# POST /list
	def create(self):
		if "name" not in self.request.form_fields:
			return response.Response400BadRequest()

		name = self.request.form_fields["name"]

		self.dao.create_list(name)
		return response.Response201Created("/")

	# POST /list/<list_index>
	def rename(self, list_index):
		if "name" not in self.request.form_fields:
			return response.Response400BadRequest()

		name = self.request.form_fields["name"]

		self.dao.rename_list(list_index, name)
		return response.Response204NoContent()

	# DELETE /list/<list_index>
	def delete(self, list_index):
		self.dao.delete_list(list_index)
		return response.Response204NoContent()
