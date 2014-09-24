
import re
import io, json
#from pprint import pprint

import smtplib
from email.mime.text import MIMEText

from time import gmtime, strftime

def words(text):
    """An iterator over tokens (words) in text. Replace this with a
    stemmer or other smarter logic.
    """

    for word in text.split():
        # normalize words by lowercasing and dropping non-alpha characters
        normed = re.sub('[^a-z]', '', word.lower())

        if normed:
            yield normed
            
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
    elif keyword1 == 'weaksubj' and keyword2 == 'both':
        result[1]+=1
        result[5]+=1
    elif keyword1 == 'strongsubj' and keyword2 == 'both':
        result[0]+=1
        result[4]+=1

class Histogram():
    def run(self, filename, dictionary):
        
        starttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        
        with open(dictionary) as dicObject:    
            dicData = json.load(dicObject)

        with open(filename) as fileobject:
            
            for line in fileobject:
                histogramAndRating = []
                if line == '\n':
                    break
                data = json.loads(line)
                result = [0, 0, 0, 0, 0, 0]
                for word in words(data["text"]):
                    for item in dicData:
                        if word == item["word"]:
                            undefinedfunction(item["type"], item["priorpolarity"], result)
                            
                histogramAndRating.append({'rating': data["stars"], 'histogram': result})
                with io.open('output_test.json', 'a', encoding='utf-8') as outfile:
                    outfile.write(unicode(json.dumps(histogramAndRating, ensure_ascii=False)))
                    outfile.close()

            

        print "FINISHED"
        # Define email addresses to use
        addr_to   = 'caikehe@gmail.com'
        addr_from = 'walleve@mail.com'
 
        # Define SMTP email server details
        smtp_server = 'smtp.mail.com'
        smtp_user   = 'walleve@mail.com'
        smtp_pass   = 'pwd'
        
        endtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        mailmessage = 'This is a notification email to show that the task is completed\n' + "Start time: " + starttime + " End time: " + endtime + "\n"
        # Construct email
        msg = MIMEText(mailmessage)
        msg['To'] = addr_to
        msg['From'] = addr_from
        msg['Subject'] = 'Notification Email'
 
        # Send the message via an SMTP server
        s = smtplib.SMTP(smtp_server)
        s.login(smtp_user,smtp_pass)
        s.sendmail(addr_from, addr_to, msg.as_string())
        s.quit()


if __name__ == "__main__":
    Histogram().run("file_review.json", "mydictionary.json")
