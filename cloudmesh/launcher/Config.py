import textwrap
import oyaml as yaml
from cloudmesh.common.console import Console
from cloudmesh.common.util import readfile
import sys
from pprint import pprint

# noinspection PyUnusedLocal
class Config():
    """

    config = Config()
    print(config)
    pprint(config.__dict__)
    pprint(config.data)
    pprint(config["info"])
    pprint(config["info.version"])
    config["info.version"] = "0.2"
    pprint(config["info.version"])

    """

    spec = textwrap.dedent("""
    info:
      name: sample
      version: '0.1'
      filename: None
      kind: launcher
      service: local
    launcher:
      darwin:
        prerequisite:
        - pwd
        install:
        - pwd
        configure:
        - pwd
        run:
        - pwd
      ubuntu:
        prerequisite:
        - pwd
        install:
        - pwd
        configure:
        - pwd
        run:
        - pwd
    """)

    def __str__(self):
        return yaml.safe_dump(self.data, default_flow_style=False)

    def __init__(self, filename=None, spec=None, **kwargs):

        self.filename = filename or "None"
        self.spec = spec or self.spec
        self.spec= textwrap.dedent(self.spec)
        self.data = yaml.load(self.spec, Loader=yaml.SafeLoader)

    def read(self, filename=None):
        with open(filename, 'r') as spec:
            self.data = yaml.load(spec, Loader=yaml.SafeLoader)

    def write(self, filename=None):
        with open(filename, 'w') as file:
            yaml.dump(self.data, file)

    def __setitem__(self, key, value):
        self.set(key, value)

    def set(self, key, value):
        """
        A helper function for setting the default cloud in the config without
        a chain of `set()` calls.

        :param key: A string representing the value's path in the config.
        :param value: value to be set.
        """

        if value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
        try:
            if "." in key:
                keys = key.split(".")
                #
                # create parents
                #
                parents = keys[:-1]
                location = self.data
                for parent in parents:
                    if parent not in location:
                        location[parent] = {}
                    location = location[parent]
                #
                # create entry
                #
                location[keys[len(keys) - 1]] = value
            else:
                self.data[key] = value

        except KeyError:
            Console.error("The key '{key}' could not be found'".format(**locals()))
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

    def __setitem__(self, key, value):
        self.set(key, value)

    def set(self, key, value):
        """
        A helper function for setting the default cloud in the config without
        a chain of `set()` calls.

        Usage:
            mongo_conn = conf.set('db.mongo.MONGO_CONNECTION_STRING',
                         "https://localhost:3232")

        :param key: A string representing the value's path in the config.
        :param value: value to be set.
        """

        if value.lower() in ['true', 'false']:
            value = value.lower() == 'true'
        try:
            if "." in key:
                keys = key.split(".")
                #
                # create parents
                #
                parents = keys[:-1]
                location = self.data
                for parent in parents:
                    if parent not in location:
                        location[parent] = {}
                    location = location[parent]
                #
                # create entry
                #
                location[keys[len(keys) - 1]] = value
            else:
                self.data[key] = value

        except KeyError:
            Console.error(
                "The key '{key}' could not be found".format(**locals()))
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

    def save(self, filename):
        with open(filename, "w") as stream:
            yaml.safe_dump(filename, self.data, default_flow_style=False)

    def __getitem__(self, item):
        """
        gets an item form the dict. The key is . separated
        use it as follows get("a.b.c")
        :param item:
        :type item:
        :return:
        """
        try:
            if "." in item:
                keys = item.split(".")
            else:
                return self.data[item]
            element = self.data[keys[0]]
            for key in keys[1:]:
                element = element[key]
        except KeyError:
            Console.warning(
                "The key '{item}' could not be found".format(**locals()))
            raise KeyError(item)
            # sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)
        # if element.lower() in ['true', 'false']:
        #    element = element.lower() == 'true'
        return element

    def __delitem__(self, item):
        """
        #
        # BUG THIS DOES NOT WORK
        #
        gets an item form the dict. The key is . separated
        use it as follows get("a.b.c")
        :param item:
        :type item:
        :return:
        """
        try:
            if "." in item:
                keys = item.split(".")
            else:
                return self.data[item]
            element = self.data
            print(keys)
            for key in keys:
                element = element[key]
            del element
        except KeyError:
            Console.error("The key '{item}' could not be found".format(**locals()))
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)


