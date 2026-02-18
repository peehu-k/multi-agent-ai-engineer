

import configparser

from collections import defaultdict


class ConfigurationParser:

    def __init__(self, filepath):

        self.filepath = filepath

        self.data = defaultdict(dict)

        with open(self.filepath, 'r') as configFile:

            parser = configparser.ConfigParser()

            # Read the entire content of the configuration file into a string and split it by section headers.

            cfg_str = '\n'.join([line for line in configFile if not line.startswith('[')]) + '\n'

            parser.read_string(cfg_str)

            # Iterate through all sections except the default one (__name__).

            for sectionName in parser:

                if sectionName != 'DEFAULT':

                    self.data[sectionName] = dict(parser[sectionName])

        return self.data


# Usage example - assuming the configuration file is at './config.ini' and structured as follows:

"""

[Section1]

key1=value1

key2=value2


[Section2]

anotherKey1=anotherValue1

anotherKey2=anotherValue2

"""

config_parser = ConfigurationParser('./config.ini')

configuration = config_parser.get_configuration()

print(dict(configuration))  # The output is now a regular dict instead of defaultdict.

