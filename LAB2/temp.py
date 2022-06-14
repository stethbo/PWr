import json

file = open('machine_params/params_4.json',)
dict_rules = json.load(file)

print(dict_rules)
