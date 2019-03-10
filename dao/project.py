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
					"description" : "Asteroids clone made in Python 3 using the PyGame library",
					"lists" : [],
					"cards" : {}
				},
				"LUCID" : {
					"username" : "bering",
					"name" : "LUCID",
					"description" : "Ultra-light Python web server hosting a web interface to manage your Kanban-style lists and cards.",
					"lists" : [ "TODO", "Doing", "Done" ],
					"cards" : {
						"0" : { # list index 0
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
								"list_index" : 0,
								"position" : 2,
								"title" : "SQLite",
								"description" : "",
								"labels" : []
							},
							"3" : {
								"id" : 3,
								"list_index" : 0,
								"position" : 3,
								"title" : "Users Interface",
								"description" : """
- [x] user list
- [ ] user add
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
- [ ] card title
- [ ] card description
- [ ] card markdown
- [ ] card labels
- [ ] card checklists
								""",
								"labels" : []
							}
						},
						"1" : { # list index 1
							"1" : { # card id 1
								"id" : 1,
								"list_index" : 0,
								"position" : 1,
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
							}
						},
						"2" : {
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
							}
						}
					}
				},
				"Master-of-Stars" : {
					"username" : "bering",
					"name" : "Master-of-Stars",
					"description" : "4x game made in Python 3 with the PyGame library",
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
