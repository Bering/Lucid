import os
from response_301 import Response301Redirect
from response_404 import Response404NotFound
from response_file import ResponseFile

def get_response(path):
	filepath = "public" + path
	if os.path.isfile(filepath):
		# TODO: Check date and return 304 Not Modified?
		return ResponseFile(filepath)
	else:
		user = None
		project = None
		card = None
		parts = path[1:].split("/")

		if parts[0] == "":
			return Response301Redirect("/index.html")

		user = parts[0]
		if len(parts) >= 2:
			project = parts[1]
			if len(parts) >= 3:
				card = parts[2]

		print("User:", user)
		print("Project:", project)
		print("Card:", card)

		return Response404NotFound()
