import psycopg2
import json

def insert_data(info):

    #establish connection with the database called senior project
    con = psycopg2.connect(
        database= "senior_project",
        user= "postgres",
        password= "1668",
        host= "localhost",
        port= "5433"
        )

    #create cursor obj
    cursor_obj = con.cursor()

    #To execute any postgre query, we need to use execute function
    #insert data into biases table
    #cursor_obj.execute("INSERT INTO biases (main_bias, sub_bias) VALUES (%s, %s);", (info["Biases"][0], info["Biases"]))
    #cursor_obj.execute("INSERT INTO biases (main_bias, sub_bias) VALUES (%s, %s);", (main_bias, sub_bias))

    #insert data into articles table
    for i in range(len(info["Articles"])):
        if info["Articles"][i]["published_date"]["month"] != "" or info["Articles"][i]["published_date"]["year"] != 0 or info["Articles"][i]["published_date"]["year"] != 0:

            cursor_obj.execute("INSERT INTO articles (headline, author, source, published_date, article_content, bias, url) VALUES(%s, %s, %s, %s, %s, %s, %s);", (info["Articles"][i]["headline"], info["Articles"][i]["author"], info["Articles"][i]["source"],info["Articles"][i]["published_date"]["month"] + "/" + str(info["Articles"][i]["published_date"]["day"]) + "/" + str(info["Articles"][i]["published_date"]["year"]), info["Articles"][i]["article_content"], info["Biases"], info["Articles"][i]["url"]))

    #Insert data into   
    #cursor_obj.execute("INSERT INTO media_source (source_name) VALUES (%s);", (str(info["Articles"][0]["source"]),))
 
    con.commit()


if __name__ == "__main__":
    path = "/Users/lucylu/Desktop/Senior-Project/data/articles/FOX/immigration_2020.json"
    with open(path, 'r') as f:
        dictionary = json.load(f)
    main_bias = "immigration"
    sub_bias = ["immigration","undocumented","refugees","nationalism","border", "Dreamers", "asylum seekers","xenophobia"]
    insert_data(dictionary)