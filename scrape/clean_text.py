import json

PATH = '../data/articles/FOX/immigration_2016.json'

def clean_text(text):
    unicode = {
        '\u2019': "'",
        '\u2013': "-",
        '\u201c': '"',
        '\u201d': '"',
        '\u00a0': "",
        "\u00f1": ""
    }

    for key, value in unicode.items():
        text = text.replace(key, value)
    
    return text 


def read():
    with open(PATH, "r") as f:
        content = json.loads(f.read())
        for item in content["Articles"]:
            item["article_content"] = clean_text(item["article_content"])

        write(content)

def write(content):
    with open(PATH, "w") as f:
        f.write(json.dumps(content, indent=4))


if __name__ == "__main__":
    read()

    
