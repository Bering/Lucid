import os
import config
import response
from controllers.project import ProjectController
from controllers.cards import CardsController

def get_response(method, path, form):

	# serve static files
	filepath = os.path.join(config.path, "public") + path
	if os.path.isfile(filepath):
		return response.ResponseFile(filepath)
	
	else:
		parts = path[1:].split("/")

		if path == "/" or path == "/name":
			# GET / = project's main page
			# POST /name = save new project name
			c = ProjectController(form)
			return c.handle_request(method, parts)

		# POST /<card_id> = save card's info
		# POST /<card_id>/drag_drop = move and reorder cards
		c = CardsController(form)
		return c.handle_request(method, parts)
