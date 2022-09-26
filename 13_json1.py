import json

data = '''{
    "name"  : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 234 567 890"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide',info["email"]["hide"])