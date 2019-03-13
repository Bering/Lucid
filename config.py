import os
import json
from appdirs import AppDirs

class Config:
	def __init__(self):
		dirs = AppDirs("LUCID", "RingLogic")
		if not os.path.exists(dirs.user_config_dir):
			os.makedirs(dirs.user_config_dir)

		self.config_file = os.path.join(dirs.user_config_dir, "config.json")
		if not os.path.exists(self.config_file):
			self.save("localhost", 8888)

	def load(self):
		fh = open(self.config_file, "r")
		config = json.loads(fh.read())
		fh.close()
		return config

	def save(self, h, p):
		config = {}
		config["hostname"] = h
		config["port"] = int(p)
		fh = open(self.config_file, "w+")
		fh.write(json.dumps(config, indent=4))
		fh.close()
		return config

# path is not part of config that is dumped to json file
# TODO: Not sure how this will behave when I use PyInstaller
# TODO: Test again to make sure it works when invoked in another project's folder
path = os.path.dirname(os.path.abspath(__file__))
