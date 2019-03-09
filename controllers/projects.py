import json
import response
from dao.user import UserDAO
from dao.project import ProjectDAO
from controllers.base import Controller

class ProjectsController(Controller):
	def __init__(self):
		pass

	def do_GET(self, parts):

		dao = UserDAO()
		username = parts[0]
		if not dao.exists(username):
			return response.Response404NotFound()

		if len(parts) == 1:
			# /<username> = list of projects
			return self.index(username)

		dao = ProjectDAO()
		project_name = parts[1]
		if not dao.exists(username, project_name):
			return response.Response404NotFound()

		# /username/project_name = project page
		return self.get(username, project_name)

	def index(self, username):
		dao = ProjectDAO()
		projects = dao.load_all(username)
		return response.ResponseView(
			"projects", 
			{
				"%username%" : username,
				"%projects%" : json.dumps(projects)
			}
		)

	def get(self, username, project_name):
		dao = UserDAO()
		user = dao.load(username)
		dao = ProjectDAO()
		project = dao.load(username, project_name)
		return response.ResponseView(
			"project",
			{
				"%user%" : json.dumps(user),
				"%project%" : json.dumps(project)
			}
		)
