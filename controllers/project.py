import json
import response
from controllers.base import Controller
from dao.project import ProjectDAO

class ProjectController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, method, parts):
		self.dao = ProjectDAO()

		if method == "get":
			return self.main_view()
		elif method == "post":
			if parts[0] == "name":
				return self.project_rename()
			elif parts[0] == "list":
				return self.list_rename(parts)
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
			if "name" not in self.form_fields:
				return response.Response400BadRequest()

			name = self.form_fields["name"]

			self.dao.project_rename(name)
			return response.Response204NoContent()

	# POST /list/<list_index>
	def list_rename(self, parts):
			if "name" not in self.form_fields:
				return response.Response400BadRequest()

			if len(parts) != 2:
				return response.Response400BadRequest()

			list_index = int(parts[1])
			name = self.form_fields["name"]

			self.dao.list_rename(list_index, name)
			return response.Response204NoContent()

	def not_found(self):
			return response.Response404NotFound()