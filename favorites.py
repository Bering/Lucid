import os
import json
from appdirs import AppDirs

class Favorites:
	def __init__(self):
		dirs = AppDirs("LUCID", "RingLogic")
		if not os.path.exists(dirs.user_config_dir):
			os.makedirs(dirs.user_config_dir)

		self.favorites_file = os.path.join(dirs.user_config_dir, "favorites.json")
		if not os.path.exists(self.favorites_file):
			self._favorites = {}
			self.save()

		self.load()

	def load(self):
		fh = open(self.favorites_file, "r")
		self._favorites = json.load(fh)
		fh.close()

	def save(self):
		fh = open(self.favorites_file, "w+")
		json.dump(self._favorites, fh, indent=4)
		fh.close()

	def is_favorite(self):
		current_folder = os.path.dirname(os.path.realpath(__file__))
		return (current_folder in self._favorites)

	def make_options(self):
		current_folder = os.path.dirname(os.path.realpath(__file__))

		options = []
		for path, name in self._favorites.items():
			if path == current_folder:
				continue
			options.append('<option value="' + path + '">' + name + '</option>')

		return options

	def toggle(self, project_name):
		current_folder = os.path.dirname(os.path.realpath(__file__))

		if current_folder in self._favorites:
			del self._favorites[current_folder]
		else:
			self._favorites[current_folder] = project_name

		self.save()
