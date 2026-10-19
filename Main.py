import time,requests 
z = 0
while True :
   z+=1
   a = requests.get("https://api.telegram.org/bot8953744107:AAHfUaoG2aJZ3WpJzpD_rbGJIDist8pxqbc/sendMessage?chat_id=-1004324675339&parse_mode=Markdown&text=TEST_"+str(z))
   time.sleep(600)
