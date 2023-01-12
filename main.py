import bottle
import os.path
import data
import json
import process

@bottle.route("/")
def serve_html():
    return bottle.static_file("index.html", root=".")
    
@bottle.route("/script")
def serve_js():
    return bottle.static_file("script.js", root=".")
    
@bottle.route("/getData")
def serve_data():
    ls = data.load_data("saved_data.csv")   
    return json.dumps(ls)

@bottle.post("/getDataCustom")
def serve_custom():
    jsonContent = bottle.request.body.read().decode()
    hour = json.loads(jsonContent)
    ls = data.load_data("saved_data.csv")  
    dict = {"hour": hour, "ls": ls}
    return json.dumps(dict)


def startup():
    csv_file = 'saved_data.csv'
    if not os.path.isfile(csv_file):
        url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
        info = data.json_loader(url)
        data.fix_data(info,"incident_datetime")
        heads = ['year','month','hour_of_day','incident_type_primary','day_of_week']
        data.save_data(info, heads, csv_file)

startup()
bottle.run(host="0.0.0.0", port=8080)