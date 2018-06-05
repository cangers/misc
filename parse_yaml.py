import yaml
import argparse
import os
import sys

class ParseYaml(object):

    def __init__(self, file, sep, cap, set):
        self.file = file
        self.sep = sep
        self.cap = cap
        self.set = set
        self.data = self.parse_yaml(self.file)

    def walk_dict(self, indict, pre=None):
        for key, value in indict.items():
            if isinstance(value, dict):
                pre = "{}_{}".format(pre, key) if pre is not None else key
                walk_dict(value, pre=pre)
            else:
                bash_var = "{}_{}".format(pre, key) if pre is not None else key
                bash_assignment = "{}={}".format(bash_var, value)
                return(bash_assignment)

    def parse_yaml(self, file):
        if not os.path.isfile(file):
            raise IOError('File {} not found'.format(file))
        with open(file, 'r') as yml:
            data = yaml.load(yml)
        return(data)

    def test(self):
        res = []
        for key, value in self.data.items():
            res += walk_dict({key: value})
            print(res)
        return res

if __name__ == '__main__':
    test()
