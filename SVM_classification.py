
from LIBSVM.python.svmutil import *
import io, json

import smtplib
from email.mime.text import MIMEText


endtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
"""
trainingFeatures = []
trainingLabels = []

for i in xrange(1, 11):
    with open('feature_data/output_split' + str(i) + '.json') as data_file:    
        data = json.load(data_file)
        for item in data:
            trainingFeatures.append(item["histogram"])
            trainingLabels.append(item["rating"])
"""

trainingFeatures = []
trainingLabels = []


with open('feature_data/output_split1.json') as data_file:    
    data = json.load(data_file)
    i = 0;
    for item in data:
        i+=1
        print(i)
        trainingFeatures.append(item["histogram"])
        trainingLabels.append(item["rating"])



model = svm_train(trainingLabels, trainingFeatures, '-c 4')

testingFeatures = []
testingLabels = []
with open('feature_data/output_split2.json') as data_file:    
    data = json.load(data_file)
    for item in data:
        testingFeatures.append(item["histogram"])
        testingLabels.append(item["rating"])


p_labs, p_acc, p_vals = svm_predict(testingLabels, testingFeatures, model)

print(p_acc)
predictResult = []
for i in xrange(0, len(p_labs)-1):
    predictResult.append({'label': p_labs[i], 'value': p_vals[i]})
                

with io.open('predict_result.json', 'w', encoding='utf-8') as outfile:
    outfile.write(unicode(json.dumps(predictResult, ensure_ascii=False)))

sendMail()

def sendMail():

    # Define email addresses to use
    addr_to   = 'caikehe@gmail.com'
    addr_from = 'walleve@mail.com'
 
    # Define SMTP email server details
    smtp_server = 'smtp.mail.com'
    smtp_user   = 'walleve@mail.com'
    smtp_pass   = 'Test123456'
        
    endtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    mailmessage = 'This is a notification email to show that the task is completed\n' + "Start time: " + starttime + " End time: " + endtime + "\n"
    print(mailmessage)
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

