import os
import response
from controllers.config import ConfigController
from controllers.users import UsersController
from controllers.projects import ProjectsController
from controllers.cards import CardsController

def get_response(path):
	filepath = "public" + path
	if os.path.isfile(filepath):
		return response.ResponseFile(filepath)
	else:
		user = None
		project = None
		card = None
		parts = path[1:].split("/")

		if parts[0] == "":
			return response.Response301Redirect("/users")

		command = parts[0]
		if command == "config":
			c = ConfigController()
			return c.do_GET(parts)
		if command == "users":
			c = UsersController()
			return c.do_GET(parts)

		if len(parts) < 3:
			c = ProjectsController()
			return c.do_GET(parts)

		c = CardsController()
		return c.do_GET(parts)
