import os
import config
import response
from controllers.project import ProjectController
from controllers.cards import CardsController

def get_response(request):

	# serve static files
	filepath = os.path.join(config.path, "public") + request.path
	if os.path.isfile(filepath):
		return response.ResponseFile(request, filepath)
	
	else:
		if request.path_parts[0] in ["", "name", "drag_drop", "list"]:
			# GET / = project's main page
			# POST /name = save new project name
			# POST /drag_drop = drag & drop a card
			# POST /list/<list_index> = rename list
			c = ProjectController()
			return c.handle_request(request)

		# POST /<card_id> = save card's info
		# POST /<card_id>/drag_drop = move and reorder cards
		# DELETE /<card_id>
		c = CardsController()
		return c.handle_request(request)
