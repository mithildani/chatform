import mysql.connector
import datetime

def DataUpdate(profile,experience,gender,company_name,skills):
    mydb=mysql.connector.connect(
        host="us-cdbr-east-05.cleardb.net",
        user="b1e337b88487dd",
        passwd="60cfc22a",
        database='heroku_daa746ade202a92'
    )
    mycursor = mydb.cursor()
    now=datetime.datetime.now()
    # query= 'INSERT INTO chat_bot(profile,experience,gender,company_name) VALUES("{0}","{1}","{2}","{3}");'.format(profile,experience,gender,company_name)
    # query="select * from chat_bot"
    print(skills)
    try:
        mycursor.execute("INSERT INTO chat_bot (profile,experience,gender,company_name,skills,timestamp) VALUES (%s,%s,%s,%s,%s,%s);",(profile,experience,gender,company_name,str(skills),str(now)))
        # mycursor.execute("select * from chat_bot")
    except:
        print(Exception.with_traceback)
    for i in mycursor:  
        print(i)
    mydb.commit()
    mydb.close()

if __name__=="__main__":
    DataUpdate("driver","0","Male","workindia","none")