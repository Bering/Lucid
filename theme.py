import os
import json
import config

class ThemeManager:
	def __init__(self):
		self.theme_name = None
		self.theme = None

	def apply(self, theme_name):
		theme = self.load_theme(theme_name)
		css = self.load_css()
		css = css.replace("{{html_background}}", theme["html_background"])
		css = css.replace("{{html_foreground}}", theme["html_foreground"])
		css = css.replace("{{list_background}}", theme["list_background"])
		css = css.replace("{{list_border}}", theme["list_border"])
		css = css.replace("{{list_foreground}}", theme["list_foreground"])
		css = css.replace("{{card_background}}", theme["card_background"])
		css = css.replace("{{card_border}}", theme["card_border"])
		css = css.replace("{{card_foreground}}", theme["card_foreground"])
		css = css.replace("{{progressbar_background}}", theme["progressbar_background"])
		css = css.replace("{{progressbar_border}}", theme["progressbar_border"])
		css = css.replace("{{progressbar_progress}}", theme["progressbar_progress"])
		css = css.replace("{{label1}}", theme["label1"])
		css = css.replace("{{label2}}", theme["label2"])
		css = css.replace("{{label3}}", theme["label3"])
		css = css.replace("{{label4}}", theme["label4"])
		css = css.replace("{{label5}}", theme["label5"])
		css = css.replace("{{label6}}", theme["label6"])
		css = css.replace("{{button_background}}", theme["button_background"])
		css = css.replace("{{button_foreground}}", theme["button_foreground"])
		return css

	def load_theme(self, theme_name):
		self.theme_name = theme_name
		theme_file = os.path.join(config.path, "themes", theme_name+".json")
		fh = open(theme_file, "r")
		self.theme = json.load(fh)
		fh.close()
		return self.theme

	def load_css(self):
		css_file = os.path.join(config.path, "public", "site.css")
		fh = open(css_file, "r")
		css = fh.read()
		fh.close()
		return css

	def make_options(self):
		files = os.listdir(os.path.join(config.path, "themes"))

		options = []
		for file in files:
			name, ext = os.path.splitext(file)
			if name == self.theme_name:
				options.append("<option selected>"+name+"</option>")
			else:
				options.append("<option>"+name+"</option>")

		return options
