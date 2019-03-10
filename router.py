import os
import response
from controllers.config import ConfigController
from controllers.users import UsersController
from controllers.projects import ProjectsController
from controllers.cards import CardsController

def get_response(method, path, form):
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
			c = ConfigController(form)
			return c.handle_request(method, parts)
		if command == "users":
			c = UsersController(form)
			return c.handle_request(method, parts)

		if len(parts) < 3:
			c = ProjectsController(form)
			return c.handle_request(method, parts)

		c = CardsController(form)
		return c.handle_request(method, parts)
