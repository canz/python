import random
import yaml

for i in range(5):
    print(random.random())


with open("D:\python\settings.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
#comment
