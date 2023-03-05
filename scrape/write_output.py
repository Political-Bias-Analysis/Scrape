from json import dumps


def write_to_json(path, info):
    with open(path, 'w') as f:
        json_val = dumps(info, indent=4)
        f.write(json_val)