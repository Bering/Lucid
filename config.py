import os
import json
from appdirs import AppDirs

class ConfigManager:
	def __init__(self):
		dirs = AppDirs("LUCID", "RingLogic")
		if not os.path.exists(dirs.user_config_dir):
			os.makedirs(dirs.user_config_dir)

		self.config_file = os.path.join(dirs.user_config_dir, "config.json")
		if not os.path.exists(self.config_file):
			self.save("localhost", 8888)

	def load(self):
		fh = open(self.config_file, "r")
		config = json.load(fh)
		fh.close()
		return config["hostname"], config["port"]

	def save(self, h, p):
		config = {}
		config["hostname"] = h
		config["port"] = int(p)
		fh = open(self.config_file, "w+")
		json.dump(config, fh, indent=4)
		fh.close()

# path is not part of config that is dumped to json file
path = os.path.dirname(os.path.abspath(__file__))
