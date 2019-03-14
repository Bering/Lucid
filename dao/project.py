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

	def save(self):
		fh = open(self.file, "w")
		fh.write(json.dumps(self.project, indent=4))
		fh.close()

	def project_rename(self, new_name):
		self.project["name"] = new_name
		self.save()

	def list_rename(self, list_index, new_name):
		self.project["lists"][list_index] = new_name
		self.save()

	def list_add(self, new_name):
		self.project["lists"].append(new_name)
		self.save()

	def list_delete(self, list_index):
		del self.project["lists"][list_index]
		self.save()

	def reorder_lists(self):
		pass

	def get_new_card(self):
		return {
			"id" : 0,
			"list_index" : 0,
			"position" : 0,
			"title" : "",
			"description" : "",
			"labels" : []
		}

	def load_card(self, card_id):
		for card in self.project["cards"]:
			if card["id"] == card_id:
				return card
		return None

	def save_card(self, new_card):
		if new_card["id"] == 0:
			new_card["id"] = self.project["next_id"]
			self.project["next_id"] += 1
			self.project["cards"].append(new_card)
			self.save()
			return
		
		for n, card in enumerate(self.project["cards"]):
			if card["id"] == new_card["id"]:
				self.project["cards"][n] = new_card

		self.save()

	def delete_card(self, card):
		for n in range(len(self.project["cards"])):
			if self.project["cards"][n]["id"] == card["id"]:
				del self.project["cards"][n]
				break

		self.save()

	def reorder_cards(self, list_index, ids):
		n = 0
		list_index = int(list_index)
		for card_id in ids:
			card = self.load_card(card_id)
			card["list_index"] = list_index
			card["position"] = n
			n += 1

		self.project["cards"] = sorted(self.project["cards"], key=lambda x: list(x.values())[2])
		self.save()
