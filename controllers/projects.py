import response
from controllers.base import Controller

class ProjectsController(Controller):
	def __init__(self):
		pass

	def do_GET(self, parts):
		username = parts[0]
		project_name = parts[1]
		return response.Response404NotFound()
