import os
from response_404 import Response404NotFound
from response_file import ResponseFile

def get_response(path):
	filepath = "public" + path
	if not os.path.isfile(filepath):
		return Response404NotFound()
	else:
		return ResponseFile(filepath)
