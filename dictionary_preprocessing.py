import re, io, json

with open("subjclueslen1-HLTEMNLP05.tff") as dicobject:
    
    dicdata = dicobject.readlines()
    dicItems = []
    for line in dicdata:
        dicline = re.split('\s+|\=+', line)
        dicItems.append({'word': dicline[5], 'type': dicline[1], 'priorpolarity': dicline[11]})
        
    with io.open('mydictionary.json', 'w', encoding='utf-8') as outfile:
        outfile.write(unicode(json.dumps(dicItems, ensure_ascii=False)))

