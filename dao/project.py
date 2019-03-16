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
				"lists" : {
					"0" : "TODO",
					"1" : "Doing",
					"2" : "Done"
				},
				"next_id" : 3,
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

	def create_list(self, new_name):
		self.project["lists"][str(self.project["next_id"])] = new_name
		self.project["next_id"] += 1
		self.save()

	def rename_list(self, list_id, new_name):
		self.project["lists"][list_id] = new_name
		self.save()

	def delete_list(self, list_id):
		del self.project["lists"][list_id]
		self.project["cards"] = [c for c in self.project["cards"] if c["list_id"] != list_id]
		self.save()

	def reorder_lists(self):
		pass

	def get_new_card(self):
		return {
			"id" : 0,
			"list_id" : 0,
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

	def append_card(self, new_card):
		new_card["id"] = self.project["next_id"]
		self.project["next_id"] += 1

		new_card["position"] = 0
		for card in self.project["cards"]:
			if card["list_id"] != new_card["list_id"]:
				continue

			new_card["position"] += 1

		self.project["cards"].append(new_card)
		self.save()
		return

	def prepend_card(self, new_card):
		new_card["id"] = self.project["next_id"]
		self.project["next_id"] += 1

		new_card["position"] = 0
		for card in self.project["cards"]:
			if card["list_id"] != new_card["list_id"]:
				continue

			# note that the difference with append() is that here we change
			# the position of the existing cards, not the one of the new card
			card["position"] += 1

		self.project["cards"].append(new_card)
		self.project["cards"] = sorted(self.project["cards"], key=lambda x: list(x.values())[2])
		self.save()
		return
	
	def save_card(self, new_card):
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

	def reorder_cards(self, list_id, card_ids):
		n = 0
		list_id = int(list_id)
		for card_id in card_ids:
			card = self.load_card(card_id)
			card["list_id"] = list_id
			card["position"] = n
			n += 1

		self.project["cards"] = sorted(self.project["cards"], key=lambda x: list(x.values())[2])
		self.save()
