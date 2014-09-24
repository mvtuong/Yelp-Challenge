import json, io

with open('predict_result.json') as predict_file:
    with open('feature_data/output_split2.json') as original_file:
        predict_data = json.load(predict_file)
        original_data = json.load(original_file)
        acc_rate = [0, 0]
        with io.open('evaluation_result.txt', 'a', encoding='utf-8') as output_file:
            for i in xrange(0, 100000-1):
                if predict_data[i]["label"]=='' or original_data[i]["rating"] =='':
                    break
                if int(predict_data[i]["label"]) == int(original_data[i]["rating"]):
                    acc_rate[0]+=1
                    data = "#" + str(i) + ": " + str(original_data[i]["histogram"]) + "   " + str(int(predict_data[i]["label"])) + "-" + str(original_data[i]["rating"]) + " -> r\n"
                    #print(data)
                    output_file.write(unicode(data))
                    
                else:
                    acc_rate[1]+=1
                    data = "#" + str(i) + ": " + str(original_data[i]["histogram"]) + "   " + str(int(predict_data[i]["label"])) + "-" + str(original_data[i]["rating"]) + " -> wrong\n"
                    #print(data)
                    output_file.write(unicode(data))
                    
            finalResult = "#Right: " + str(acc_rate[0]) + " #Wrong: " + str(acc_rate[1]) + '\n'        
            #print(finalResult)
            #print("Accuracy = 37.807% (37807/100000) (classification) (37.807, 2.25009, 0.1385564602059881)")
            output_file.write(unicode(finalResult))
            output_file.write(unicode("Accuracy = 37.807% (37807/100000) (classification) (37.807, 2.25009, 0.1385564602059881)"))
