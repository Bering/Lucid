import os
import json
from appdirs import AppDirs

dirs = AppDirs("LUCID", "RingLogic")
if not os.path.exists(dirs.user_config_dir):
	os.makedirs(dirs.user_config_dir)

config_file = os.path.join(dirs.user_config_dir, "config.json")
if not os.path.exists(config_file):
	fh = open(config_file, "w+")
	config = {
		"hostname" : "localhost",
		"port" : 8888
	}
	fh.write(json.dumps(config, indent=4))
	fh.close()

fh = open(config_file, "r")
config = json.loads(fh.read())
fh.close()

path = os.path.dirname(os.path.abspath(__file__))
hostname = config["hostname"]
port = config["port"]
