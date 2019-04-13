from __future__ import absolute_import
import sys
import json
from bottle import abort, request, template, HTTPResponse, redirect
from favorites import Favorites
from theme import ThemeManager
from dao.project import ProjectDAO

class ProjectController():
	def __init__(self):
		self.dao = ProjectDAO()

	# GET /
	def main_page(self):
		favorites = Favorites()
		theme_manager = ThemeManager()
		return template(
			"project",
			CSS = theme_manager.apply(self.dao.project["theme"]),
			favorites_options = favorites.make_options(),
			theme_options = theme_manager.make_options(),
			is_favorite = favorites.is_favorite(),
			project_name = self.dao.project["name"],
			project = json.dumps(self.dao.project),
			card_background = theme_manager.theme["card_background"]
		)

	# POST /name
	def rename_project(self):
		if "name" not in request.forms:
			abort(400)

		name = request.forms.name

		self.dao.project_rename(name)
		return HTTPResponse(status=204)

	# POST /drag_drop
	def drag_drop(self):
		if "list_ids" not in request.forms:
			abort(400)

		list_ids = json.loads(request.forms.list_ids)

		self.dao.reorder_lists(list_ids)
		return HTTPResponse(status=204)

	# GET /toggle_favorite
	def toggle_favorite(self):
		favorites = Favorites()
		favorites.toggle(self.dao.project["name"])
		return redirect("/")

	# GET /theme/<theme_name>
	def switch_theme(self, theme_name):
		self.dao.switch_theme(theme_name)
		return redirect("/")

	# GET /shutdown
	def shutdown(self):
		sys.stderr.close()
