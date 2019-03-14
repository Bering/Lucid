import json
import response
from controllers.base import Controller
from dao.project import ProjectDAO

class ProjectController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, method, parts):
		dao = ProjectDAO()

		if method == "get":
			return response.ResponseView(
				"project",
				{
					"%project_name%" : dao.project["name"],
					"%project%" : json.dumps(dao.project)
				}
			)
		else:
			if parts[0] == "name":
				if "name" not in self.form_fields:
					return response.Response400BadRequest()

				name = self.form_fields["name"]
				dao.project["name"] = name
				dao.save()
				return response.Response204NoContent()

			# for lists later on
			else:
				return response.Response404NotFound()