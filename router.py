import os
import response
from controllers.config import ConfigController
from controllers.users import UsersController
from controllers.projects import ProjectsController
from controllers.cards import CardsController

def get_response(path):
	filepath = "public" + path
	if os.path.isfile(filepath):
		# TODO: Check date and return 304 Not Modified?
		return response.ResponseFile(filepath)
	else:
		user = None
		project = None
		card = None
		parts = path[1:].split("/")

		command = parts[0]
		if command == "config":
			c = ConfigController()
			return c.do_GET()
		if command == "users":
			c = UsersController()
			return c.do_GET(parts)
		if len(parts) == 1:
			return response.Response404NotFound()

		user = parts[0]
		project = parts[1]
		if len(parts) == 2:
			c = ProjectsController()
			return c.do_GET(user, project)

		card = parts[2]
		if len(parts) >= 3:
			c = CardsController()
			return c.do_GET(user, project, card)

		return response.Response400BadRequest()
