class ProjectDAO:
	def __init__(self):
		pass

	def load_all(self, username):
		if username != "bering":
			return {}
		else:
			return {
				"Asteroids" : {
					"username" : "bering",
					"name" : "Asteroids",
					"lists" : [],
					"cards" : {}
				},
				"LUCID" : {
					"username" : "bering",
					"name" : "LUCID",
					"lists" : [ "TODO", "Doing", "Done" ],
					"cards" : {
						"0" : {
							"id" : 0,
							"title" : "304 Not Modified",
							"description" : "",
							"labels" : []
						},
						"1" : {
							"id" : 1,
							"title" : "Project interface",
							"description" : """- [x] project list
- [ ] Username
- [ ] project renaming
- [ ] project switcher
- [ ] display lists
- [ ] renaming lists
- [ ] adding lists
- [ ] removing lists
- [ ] adding cards
- [ ] card title
- [ ] card description
- [ ] drag and dropping cards between lists
- [ ] drag and dropping card in same list
- [ ] project add
- [ ] project delete
- [ ] user add
- [ ] user edit
- [ ] user delete
- [ ] card labels
- [ ] card markdown
- [ ] card checklists
""",
							"labels" : []
						},
						"2" : {
							"id" : 2,
							"title" : "SQLite",
							"description" : "",
							"labels" : []
						},
					}
				},
				"Master-of-Stars" : {
					"username" : "bering",
					"name" : "Master-of-Stars",
					"lists" : [ "TODO", "Doing", "Done" ],
					"cards" : {}
				},
			}

	def exists(self, username, project_name):
		return project_name in self.load_all(username)

	def load(self, username, project_name):
		return self.load_all(username)[project_name]

	def add(self, username, project_name):
		pass

	def update(self, username, project_name):
		pass

	def delete(self, username, project_name):
		pass
