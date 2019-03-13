
class CardsDAO():
	
	def load_all(self):
		return {
			"0" : { # card id 0
				"id" : 0,
				"list_index" : 0,
				"position" : 0,
				"title" : "304 Not Modified",
				"description" : "",
				"labels" : []
			},
			"2" : {
				"id" : 2,
				"list_index" : 1,
				"position" : 1,
				"title" : "Data Storage",
				"description" : "SQLite? XML? JSON?",
				"labels" : []
			},
			"3" : {
				"id" : 3,
				"list_index" : 0,
				"position" : 3,
				"title" : "Users Interface",
				"description" : """
- [x] user list
- [x] user add
- [ ] user edit
- [ ] user delete
				""",
				"labels" : []
			},
			"4" : {
				"id" : 4,
				"list_index" : 0,
				"position" : 4,
				"title" : "Projects Interface",
				"description" : """
- [x] project list
- [ ] project add
- [ ] project delete
				""",
				"labels" : []
			},
			"5" : {
				"id" : 5,
				"list_index" : 0,
				"position" : 5,
				"title" : "Card Interface",
				"description" : """
- [x] card title
- [x] card description
- [ ] card markdown
- [ ] card labels
- [ ] card checklists
				""",
				"labels" : []
			},
			"1" : { # card id 1
				"id" : 1,
				"list_index" : 1,
				"position" : 0,
				"title" : "Project interface",
				"description" : """
- [ ] Username?
- [ ] project renaming
- [ ] project switcher
- [x] display lists
- [ ] renaming lists
- [ ] adding lists
- [ ] removing lists
- [x] display cards
- [ ] adding cards near top
- [ ] adding cards near bottom
- [ ] drag and dropping cards between lists
- [ ] drag and dropping card in same list
- [ ] card icons
- [ ] card labels
				""",
				"labels" : []
			},
			"6" : {
				"id" : 6,
				"list_index" : 2,
				"position" : 0,
				"title" : "Web Server",
				"description" : """
- [x] Hello world
- [x] Response classes
- [x] Router class
- [x] Controller classes
- [x] View basics
				""",
				"labels" : []
			},
			"7" : {
				"id" : 7,
				"list_index" : 0,
				"position" : 6,
				"title" : "Start Browser",
				"description" : "Start user's browser after starting the server, just like Jupyter Notebook",
				"labels" : []
			},
			"8" : {
				"id" : 8,
				"list_index" : 0,
				"position" : 7,
				"title" : "Command line interface",
				"description" : "To setup the hostname and port without editing the JSON config",
				"labels" : []
			}
		}

	def exists(self, card_id):
		return card_id in self.load_all()

	def load(self, card_id):
		return self.load_all()[card_id]

	def add(self, form):
		pass

	def update(self, card_id, title, description):
		pass

	def delete(self, card_id):
		pass