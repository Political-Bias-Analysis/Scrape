from json import dumps, load

def write_to_json(path, info):
    with open(path, 'w') as f:
        json_val = dumps(info, indent=4)
        f.write(json_val)


def add_to_json(path, info):
    with open(path, 'a+') as file:
        cur = load(file)
        print(cur)
        cur.update(info)
        json_val = dumps(info, indent=4)
        file.write(json_val)

