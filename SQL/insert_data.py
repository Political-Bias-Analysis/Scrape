import psycopg2
import json

def insert_data(info, main_bias, sub_bias, source):

    #establish connection with the database called senior project
    con = psycopg2.connect(
        database= "articles",
        user= "postgres",
        password= "",
        host= "localhost",
        port= "5432"
        )

    #create cursor obj
    cursor_obj = con.cursor()

    #To execute any postgre query, we need to use execute function
    #insert data into biases table
    #cursor_obj.execute("INSERT INTO biases (main_bias, sub_bias) VALUES (%s, %s);", (info["Biases"][0], info["Biases"]))
    #cursor_obj.execute("INSERT INTO biases (main_bias, sub_biases) VALUES (%s, %s);", (main_bias, sub_bias))

    #insert data into articles table
    for i in range(len(info["Articles"])):
        try:
            cursor_obj.execute("INSERT INTO articles (headline, author, source, published_date, article_content, main_bias, query_bias, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);", (info["Articles"][i]["headline"], info["Articles"][i]["author"], info["Articles"][i]["source"],info["Articles"][i]["published_date"]["month"] + "/" + str(info["Articles"][i]["published_date"]["day"]) + "/" + str(info["Articles"][i]["published_date"]["year"]), info["Articles"][i]["article_content"], main_bias, info["Articles"][i]["bias"], info["Articles"][i]["url"]))
        except:
            continue
    #Insert data into   
    #cursor_obj.execute("INSERT INTO media_source (source_name) VALUES (%s);", (str(source),))
 
    con.commit()


if __name__ == "__main__":
    YEAR, SOURCE = 2020, "FOX"
    main_bias = "socioeconomic"
    sub_bias = ["socioeconomic","poverty line","working class","middle class","medicare"]
    path = f"/Users/tramla/Desktop/UCI Courses/Senior-Project/Data/data/articles/{SOURCE}/{main_bias}_{YEAR}.json"
    with open(path, 'r') as f:
        dictionary = json.load(f)

    insert_data(dictionary, main_bias, sub_bias, SOURCE)