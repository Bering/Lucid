import os
import json

class ProjectDAO():
	def __init__(self):
		self.file = "LUCID.json"
		if not os.path.exists(self.file):
			fh = open(self.file, "w+")
			default_config = {
				"name" : "New Project",
				"description" : "",
				"lists" : ["TODO", "Doing", "Done"],
				"cards" : [
					"0" : [],
					"1" : [],
					"2" : []
				}
			}
			fh.write(json.dumps(default_config, indent=4))
			fh.close()

	def load(self):
		fh = open(self.file, "r")
		project_json = fh.read()
		fh.close()
		project = json.loads(project_json)
		return project
