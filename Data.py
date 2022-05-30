import requests
import re
import json
import numpy

runsArray = []

def getruns(gameID):
    
    offset = 0
    level = ""
    category = ""
    subcat = ""
    rid = ""
    runner = ""
    time = 0
    count = 0
    
    while True:
        url = "https://www.speedrun.com/api/v1/runs?max=200&offset=" + str(offset) + "&status=verified&game=" + gameID
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            for runs in data:
                if(runs['level'] == None):
                    category = runs['category']
                    try:
                        vals = runs['values'].values()
                        subcat = ''.join(str(e) for e in vals)
                    except KeyError:
                        subcat = ""
                    try:
                        rid = runs['players'][0]['id']
                        runner = requests.get(runs['players'][0]['uri']).json()['data']['names']['international']
                    except KeyError:
                        runner = runs['players'][0]['name']
                    time = runs['times']['primary_t']
                    
                    runsArray.append({"runID": runs['id'], "category": category, "subcat": subcat, "runner": runner, "time": time})
                    count+=1
                    print(count)
        
        if (response.json()['pagination']['size'] < 200):
            break
        else:
            offset+=200

getruns('yd4y2wde')
getruns('j1ll33j1')
getruns('o6gl4yxd')
getruns('76rxokq6')
getruns('m1mq4xd2')
getruns('m1zqnx10')
getruns('3dx2v0y1')
getruns('v1pg4418')
getruns('yd4r0g1e')
getruns('46wje7dr')
getruns('v1ppz718')
getruns('kdkzoz2d')
getruns('268k8y6p')
getruns('v1po7vz6')
getruns('76rykq18')
getruns('4d777rd7')
getruns('268qr96p')
getruns('lde8ljd3')
getruns('j1nl5edp')
getruns('j1l704dg')
getruns('369vv31l')

with open('test.npy', 'wb') as f:
    numpy.save(f, runsArray)