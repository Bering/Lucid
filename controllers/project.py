import json
import response
from controllers.base import Controller
from dao.project import ProjectDAO

class ProjectController(Controller):
	def handle_request(self, request):
		self.request = request
		self.dao = ProjectDAO()

		if request.method == "get":
			return self.main_view()
		elif request.method == "post":
			if request.path_parts[0] == "name":
				return self.project_rename()
			elif request.path_parts[0] == "drag_drop":
				return self.drag_drop()
			elif request.path_parts[0] == "list":
				return self.list_rename()
			else:
				return self.not_found()

	def main_view(self):
		return response.ResponseView(
			"project",
			{
				"%project_name%" : self.dao.project["name"],
				"%project%" : json.dumps(self.dao.project)
			}
		)

	# POST /name
	def project_rename(self):
			if "name" not in self.request.form_fields:
				return response.Response400BadRequest()

			name = self.request.form_fields["name"]

			self.dao.project_rename(name)
			return response.Response204NoContent()

	# POST /drag_drop
	def drag_drop(self):
		if "list_index" not in self.request.form_fields\
		or "ids" not in self.request.form_fields:
			return response.Response400BadRequest()

		list_index = self.request.form_fields["list_index"]
		ids = json.loads(self.request.form_fields["ids"])

		self.dao.reorder_cards(list_index, ids)
		return response.Response204NoContent()

	# POST /list/<list_index>
	def list_rename(self):
			if "name" not in self.request.form_fields\
			or len(self.request.path_parts) != 2:
				return response.Response400BadRequest()

			list_index = int(self.request.path_parts[1])
			name = self.request.form_fields["name"]

			self.dao.list_rename(list_index, name)
			return response.Response204NoContent()

	def not_found(self):
			return response.Response404NotFound()