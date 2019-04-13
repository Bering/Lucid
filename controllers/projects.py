from __future__ import absolute_import
import os
import json
import urllib
import platform
from favorites import Favorites
from theme import ThemeManager
from bottle import abort, request, template, HTTPResponse, redirect
import ctypes

class ProjectsController():

	def get_drives(self):
		drives = []

		if platform.system() == "Windows":
			bitmask = ctypes.windll.kernel32.GetLogicalDrives()
			for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				if bitmask & 1:
					drives.append(letter)
				bitmask >>= 1

		return drives

	def browse(self, path):
		favorites = Favorites()
		theme_manager = ThemeManager()
		for root, folders, files in os.walk(path):
			return template(
				"browse",
				CSS = theme_manager.apply("default"),
				favorites_options = favorites.make_options(),
				theme_options = theme_manager.make_options(),
				drives=self.get_drives(),
				parent=os.path.abspath(os.path.join(path, os.pardir)),
				folders=folders,
				path=root,
				isAProject=("LUCID.json" in files)
			)

	def browse_curdir(self):
		return self.browse(os.path.abspath("./"))

	def select(self, path):
		if path == "browse":
			redirect("/browse")
		else:
			os.chdir(path)
			redirect("/")

	def create(self, path):
		self.select(path)

	def delete(self, path):
		file = os.path.abspath(os.path.join(path, "LUCID.json"))
		os.remove(file)
		url = "/browse/"
		url += urllib.parse.quote_plus(path)
		url = url.replace("%3A",":")
		url = url.replace("%2F","/")
		url = url.replace("+", "%20")
		redirect(url)
