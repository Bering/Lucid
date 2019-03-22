from __future__ import absolute_import
import os
import config
from bottle import get, post, delete, static_file
from controllers.projects import ProjectsController
from controllers.project import ProjectController
from controllers.list import ListController
from controllers.card import CardController

@get("/browse")
def browse_curdir():
	c = ProjectsController()
	return c.browse_curdir()

@get("/browse/<path:path>")
def browse(path):
	c = ProjectsController()
	return c.browse(path)

@get("/select/<path:path>")
def select_project(path):
	c = ProjectsController()
	return c.select(path)

@get("/create/<path:path>")
def create_project(path):
	c = ProjectsController()
	return c.create(path)

@get("/delete/<path:path>")
def delete_project(path):
	c = ProjectsController()
	return c.delete(path)


@get("/")
def main_page():
	c = ProjectController()
	return c.main_page()

@post("/name")
def rename_project():
	c = ProjectController()
	return c.rename_project()

@post("/drag_drop")
def drag_drop():
	c = ProjectController()
	return c.drag_drop()

@get("/theme/<theme_name>")
def switch_theme(theme_name):
	c = ProjectController()
	return c.switch_theme(theme_name)

@get("/shutdown")
def shutdown():
	c = ProjectController()
	return c.shutdown()


@post("/list") # create new list
def create_list():
	c = ListController()
	return c.create()

@post("/list/<list_id>") # rename list
def rename_list(list_id):
	c = ListController()
	return c.rename(list_id)

@delete("/list/<list_id>")
def delete_list(list_id):
	c = ListController()
	return c.delete(list_id)


@post("/card/append") # create new card at bottom of list
def append_card():
	c = CardController()
	return c.append()

@post("/card/prepend") # create new card at top of list
def prepend_card():
	c = CardController()
	return c.prepend()

@post("/card/<card_id>") # save card
def save_card(card_id):
	c = CardController()
	return c.save(card_id)

@delete("/card/<card_id>")
def delete_card(card_id):
	c = CardController()
	return c.delete(card_id)

@post("/card/drag_drop")
def drag_drop_card():
	c = CardController()
	return c.drag_drop()


@get("/<filepath>")
def files(filepath):
	root = os.path.join(config.path, "public")
	return static_file(filepath, root=root)
