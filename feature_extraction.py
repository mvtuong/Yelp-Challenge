
import re
import io, json
from pprint import pprint

def words(text):
    """An iterator over tokens (words) in text. Replace this with a
    stemmer or other smarter logic.
    """

    for word in text.split():
        # normalize words by lowercasing and dropping non-alpha
        # characters
        normed = re.sub('[^a-z]', '', word.lower())

        if normed:
            yield normed
            #print normed

def undefinedfunction(keyword1, keyword2, result):
    if keyword1 == 'strongsubj' and keyword2 == 'positive':
        result[0]+=1
    elif keyword1 == 'weaksubj' and keyword2 == 'positive':
        result[1]+=1
    elif keyword1 == 'strongsubj' and keyword2 == 'neutral':
        result[2]+=1
    elif keyword1 == 'weaksubj' and keyword2 == 'neutral':
        result[3]+=1
    elif keyword1 == 'strongsubj' and keyword2 == 'negative':
        result[4]+=1
    elif keyword1 == 'weaksubj' and keyword2 == 'negative':
        result[5]+=1

class Histogram():
    def run(self, filename, dictionary):
        
        with open(dictionary) as dicobject:
            dicdata = dicobject.readlines()
            #for line in dicdata:
            #    print(re.split('\s+|\=+', line))
        with open(filename) as fileobject:
            listOfHistogramAndRating = []
            for line in fileobject:
                data = json.loads(line)
                result = [0, 0, 0, 0, 0, 0]
                for word in words(data["text"]):
                    for line in dicdata:
                        dicline = re.split('\s+|\=+', line)
                        if word == dicline[5]:
                            #print(dicline[5] + " " + dicline[1] + " " + dicline[11])
                            undefinedfunction(dicline[1], dicline[11], result)
                
                #print(" Rating: ")
                #print(data["stars"])
                #print("Histogram: ")
                #print(result) 
                
                listOfHistogramAndRating.append({'rating': data["stars"], 'histogram': result})
                print(listOfHistogramAndRating)
            
            with io.open('output.json', 'w', encoding='utf-8') as outfile:
                outfile.write(unicode(json.dumps(listOfHistogramAndRating, ensure_ascii=False)))
                
                print "End of a review-------------------------------------------------------------"""
        
            #with open('output.json') as data_file:    
            #    data = json.load(data_file)
            #    for line in data:
            #        print(line["rating"])

if __name__ == "__main__":
    Histogram().run("input.json", "subjclueslen1-HLTEMNLP05.tff")
