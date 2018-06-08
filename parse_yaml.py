import yaml
import argparse
import os
import sys

class ParseYaml(object):
	"""
	Script to read yaml file and create bash variable assignments as such:
	node1_node2_..._noden=leaf
	Which are written to stdout
	"""

	def __init__(self, file, sep, cap, set):
		self.file = file
		self.sep = sep
		self.cap = cap
		self.set = set
		self.data = self.parse_yaml(self.file)
		self.res = self.top_level()

	def walk_dict(self, indict, pre=None):
		for key, value in indict.items():
			print key, value
			if isinstance(value, dict):
				pre = "{}_{}".format(pre, key) if pre is not None else key
				self.walk_dict(value, pre=pre)
			else:
				bash_var = "{}_{}".format(pre, key) if pre is not None else key
				bash_assignment = "{}={}".format(bash_var, value)
				return(bash_assignment)

	def top_level(self):
		res = []
		for key, value in self.data.items():
			if key is None:
				continue
			res += self.walk_dict({key: value})
		return res

	def parse_yaml(self, file):
		if not os.path.isfile(file):
			raise IOError('File {} not found'.format(file))
		with open(file, 'r') as yml:
			data = yaml.load(yml)
		return(data)

	def get(self, key, default):
		return self.data.get(key, default)

if __name__ == '__main__':
	ParseYaml('')
