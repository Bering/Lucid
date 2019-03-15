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
			else:
				return response.Response400BadRequest()
		else:
			return response.Response400BadRequest()

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
