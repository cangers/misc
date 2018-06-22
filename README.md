## Misc

Miscellaneous utilities and helper scripts.

### parse_yaml.py
A tool to allow bash scripts to read yaml files. It pipes the output to stdout to allow shell scripts to evaluate it.

Given a yaml file db.yaml:
```yaml
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
  --sep              Key-value separator
  --cap CAP          Capitalize variable(s)
  --prefix PREFIX    Prefix for variable(s)
  --get GET          Retrieve a value
  --default DEFAULT  Default value if key is not found (for --get)
  ```

##### Examples
The default behavior of parse_yaml.py is to print the bash-ified yaml file to stdout. In order to assign
those variables in your bash scripts, use `eval`
```bash
$ eval $(python parse_yaml.py db.yaml)
$ echo $db_type
mysql
```
If there are two yaml files with the same variables, use a prefix to keep variable assignments unique.

staging.yaml:
```yaml
db:
    type: sqllite
    host: 127.0.0.1
    user: dev
    password: password123
```
prod.yaml:
```yaml
db:
    type: postgres
    host: 10.0.50.100
    user: postgres
    password: password123
```

```bash
$ eval $(python parse_yaml.py prod.yaml --prefix prod --cap)
$ eval $(python parse_yaml.py staging.yaml --prefix stg --cap)
$ echo $PROD_DB_HOST
10.0.50.100
$ echo $STG_DB_HOST
127.0.0.1
```

It's also easy to grab a single value from a file. Access it with the variable that would get assigned
if you'd printed to stdout.
```bash
$ prod_user=$(python parse_yaml.py prod.yaml --get db_user)
$ prod_port=$(python parse_yaml.py prod.yaml --get db_port --default 5432)
$ echo prod_user
postgres
$ echo prod_port
5432
```