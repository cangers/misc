## Misc

Miscellaneous utilities and helper scripts.

### parse_yaml.py
A tool to allow bash scripts to read yaml files. It pipes the output to stdout to allow shell scripts to evaluate it.

Given a yaml file db.yaml:
```
author: corey
version: 1.0
db:
    type: mysql
    host: localhos
```

The folowing will create bash-friendly variables given the keys of the file.
```bash
$ python parse_yaml.py db.yaml
version=1.0
db_host=localhost
db_type=mysql
author=corey
```

#### Requirements
`parse_yaml.py` requires Python 2 and PyYAML. You can install it to your global Python installation, or for a safer alternative
create a virtual environment and shebang it in the top of the file.

```python
#!/path/to/PyYAML_env/bin/python2.7
import ...
```

#### Usage
`parse_yaml.py` takes several parameters that can be viewed with `--help`.

##### Parameters
```bash
usage: parse_yaml.py [-h] [--sep {,_}] [--cap CAP] [--prefix PREFIX]
                     [--get GET] [--default DEFAULT]
                     file

positional arguments:
  file               YAML file

optional arguments:
  -h, --help         show this help message and exit
  --sep {,_}         Key-value separator
  --cap CAP          Capitalize variable(s)
  --prefix PREFIX    Prefix for variable(s)
  --get GET          Retrieve a value
  --default DEFAULT  Default value if key is not found (for --get)
  ```

##### Examples

