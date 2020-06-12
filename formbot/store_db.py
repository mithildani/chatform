import mysql.connector

def DataUpdate(profile,experience,gender,company_name):
    mydb=mysql.connector.connect(
        host="us-cdbr-east-05.cleardb.net",
        user="b1e337b88487dd",
        passwd="60cfc22a",
        database='heroku_daa746ade202a92'
    )
    mycursor = mydb.cursor()

    # query= 'INSERT INTO chat_bot(profile,experience,gender,company_name) VALUES("{0}","{1}","{2}","{3}");'.format(profile,experience,gender,company_name)
    # query="select * from chat_bot"
    try:
        mycursor.execute("INSERT INTO chat_bot (profile,experience,gender,company_name) VALUES (%s,%s,%s,%s);",(profile,experience,gender,company_name))
        # mycursor.execute("select * from chat_bot")
    except:
        print(Exception.with_traceback)
    for i in mycursor:
        print(i)
    mydb.commit()
    mydb.close()

if __name__=="__main__":
    DataUpdate("driver","0","Male","workindia")