import json
import response
from controllers.base import Controller
from dao.project import ProjectDAO
from dao.cards import CardsDAO

class ProjectController(Controller):
	def __init__(self, form_fields):
		super().__init__(form_fields)

	def handle_request(self, method, parts):
		dao = ProjectDAO()
		project = dao.load()

		return response.ResponseView(
			"project",
			{
				"%project%" : json.dumps(project)
			}
		)
