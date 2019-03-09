from response import Response

class Response301Redirect(Response):

	def __init__(self, location):
		super().__init__(
			301,
			{ "Location" : location },
			""
		)
