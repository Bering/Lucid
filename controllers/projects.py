from __future__ import absolute_import
import os
import json
import urllib
import platform
from theme import ThemeManager
from bottle import abort, request, template, HTTPResponse, redirect
from ctypes import windll

class ProjectsController():

	def get_drives(self):
	    drives = []
	    bitmask = windll.kernel32.GetLogicalDrives()
	    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	        if bitmask & 1:
	            drives.append(letter)
	        bitmask >>= 1

	    return drives

	def browse(self, path):
		theme_manager = ThemeManager()
		for root, folders, files in os.walk(path):
			return template(
				"browse",
				CSS = theme_manager.apply("default"),
				theme_options = theme_manager.make_theme_options(),
				isRunningOnWindows=(platform.system() == "Windows"),
				drives=self.get_drives(),
				parent=os.path.abspath(os.path.join(path, os.pardir)),
				folders=folders,
				path=root,
				isAProject=("LUCID.json" in files)
			)

	def browse_curdir(self):
		return self.browse(os.path.abspath("./"))

	def select(self, path):
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