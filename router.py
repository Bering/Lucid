import os
import cgi
import response
from controllers.config import ConfigController
from controllers.users import UsersController
from controllers.projects import ProjectsController
from controllers.cards import CardsController

def get_response(method, path):
	filepath = "public" + path
	if os.path.isfile(filepath):
		return response.ResponseFile(filepath)
	else:
		user = None
		project = None
		card = None
		parts = path[1:].split("/")
		form = cgi.FieldStorage()

		if parts[0] == "":
			return response.Response301Redirect("/users")

		command = parts[0]
		if command == "config":
			c = ConfigController(form)
			return c.do_GET(parts)
		if command == "users":
			c = UsersController(form)
			return c.do_GET(parts)

		if len(parts) < 3:
			c = ProjectsController(form)
			return c.do_GET(parts)

		c = CardsController(form)
		if method == "get":
			return c.do_GET(parts)
		elif method == "post":
			return c.do_POST(parts)
