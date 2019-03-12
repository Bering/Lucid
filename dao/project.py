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
				"next_id" : 0,
				"cards" : []
			}
			fh.write(json.dumps(default_config, indent=4))
			fh.close()

		fh = open(self.file, "r")
		project_json = fh.read()
		fh.close()
		self.project = json.loads(project_json)

	def get_new(self):
		return {
			"id" : 0,
			"list_index" : 0,
			"position" : 0,
			"title" : "",
			"description" : "",
			"labels" : []
		}

	def update(
		self,
		new_name=None,
		new_description=None,
		new_lists=None
	):
		if new_name:
			self.project.name = new_name
		if new_description:
			self.project.description = new_description
		if new_lists:
			self.project.lists = new_lists
		self.save()

	def save(self):
		fh = open(self.file, "w")
		fh.write(json.dumps(self.project, indent=4))
		fh.close()

	def load_card(self, card_id):
		for card in self.project["cards"]:
			if card["id"] == card_id:
				return card
		return None

	def save_card(self, new_card):

		# TODO: update position

		if new_card["id"] == 0:
			self.project["cards"].append(new_card)
			self.save()
			return
		
		for n, card in enumerate(self.project["cards"]):
			if card["id"] == new_card["id"]:
				self.project["cards"][n] = new_card

		self.save()