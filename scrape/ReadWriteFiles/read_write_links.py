import json
import pathlib

## TRAM'S PATH
PATH = "/Users/tramla/Desktop/UCI Courses/Senior-Project/Data/data"

def write_all_links(media_name, links):
    with open( PATH + f"/links/{media_name}/all_links.json", "w") as f:
        in_json = json.dumps(list(links), indent=4)
        f.write(in_json)


def get_all_links(media_name):

    with open( PATH + f"/links/{media_name}/all_links.json") as f:
        return set(json.loads(f.read()))


def get_links_by_year(year, main_bias, media_name):

    with open(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json", 'r') as f:
        cur = json.loads(f.read())
        return cur

def prepare_format(links, main_bias, year):
    return {"Biases": [main_bias], "Links": links, "Year": year}


def write_links_by_year(dict_links, main_bias, media_name):

    for year, links in dict_links.items():
        with open(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json", "w") as f:
            in_json = json.dumps(prepare_format(links, main_bias, year), indent=4)
            f.write(in_json)
            
            
def write_more_links_by_year(dict_links, main_bias, new_bias, media_name):

    for year, links in dict_links.items():
        cur = None
        if pathlib.Path(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json").exists():
            with open(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json", 'r') as f:
                cur = json.loads(f.read())

            cur["Biases"].append(new_bias)
            cur["Links"] += links

            with open(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json", "w") as f:
                f.write(json.dumps(cur, indent=4))
        else:
            with open(PATH + f"/links/{media_name}/{main_bias}_{str(year)}.json", "w") as f:
                item = prepare_format(links, main_bias, year)
                item["Biases"].append(new_bias)
                in_json = json.dumps(item, indent=4)
                f.write(in_json)