import os
import config
import response
from controllers.project import ProjectController
from controllers.list import ListController
from controllers.card import CardController

def get_response(request):

	filepath = os.path.join(config.path, "public") + request.path

	if request.path_parts[0] in ["", "name", "drag_drop"]:
		# GET / = project's main page
		# POST /name = save new project name
		# POST /drag_drop = drag & drop a card
		c = ProjectController()
		return c.handle_request(request)

	elif request.path_parts[0] in ["list", "lists"]:
		# POST /list = create new list
		# POST /list/<list_index> = rename list
		# DELETE /list/<list_index>
		c = ListController()
		return c.handle_request(request)

	elif request.path_parts[0] == "card":
		# POST /card = create new card
		# POST /card/<card_id> = save card's info
		# DELETE /card/<card_id>
		c = CardController()
		return c.handle_request(request)

	elif os.path.isfile(filepath):
		# serve static files
		return response.ResponseFile(request, filepath)

	else:
		return response.Response400BadRequest()