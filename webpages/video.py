import json
from websocket import create_connection
import ssl
import json
import time
import wait_response
from wait_response import wait_response_status
import requests
import webbrowser

def fun_call():
    new=2
    url = "file:////Users/venkateshtata/Desktop/final_neuraWave/AgoraVideoCall/index.html"
    webbrowser.open(url,new=new);

ws = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})

_auth="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS4xMTMwMDkuc2V2ZW50aCIsImV4cCI6MTUyODc2ODA1MywiZmlyc3ROYW1lIjoidmVua2F0ZXNoIiwibGFzdE5hbWUiOiJUYXRhIiwibGljZW5zZUlkIjoiMDU3MTRlZmQtZjcwNy00OGMwLWJkNzQtNDU2N2RiYjM0ZTVkIiwibGljZW5zZVNjb3BlIjoyLCJsaWNlbnNlX2FncmVlbWVudCI6eyJhY2NlcHRlZCI6dHJ1ZSwibGljZW5zZV91cmwiOiJodHRwczovL3d3dy5lbW90aXZjbG91ZC5jb20vZGJhcGkvcHJpdmFjeS9kb2MvZXVsYS8ifSwibGljZW5zZV9leHBpcmUiOjE1MzA5ODgxOTksImxpY2Vuc2VfaGFyZExpbWl0IjoxNTMwMzE2Nzk5LCJsaWNlbnNlX3NvZnRMaW1pdCI6MTUyOTcxMTk5OSwibmJmIjoxNTI4NTA4ODUzLCJ1c2VyQ2xvdWRJZCI6MzU3ODQsInVzZXJuYW1lIjoiMTEzMDA5In0.mmiWZzC4eBp4E_w4Qiu6stiGa_uchQMpXL9ZnJrCXZY"
client_secret = "93KE83MORyTci3v4hewngDzerzDdxAkrP1BNqrn84oOhD6tNeF9pLbOWHwlsO29eYq0YmGS0ECyOEGgrWabh6PWDMVkxbYd12ASm1CVUCtwdFyCcX4QX6V1oRWJXx0fp"
client_id = "mACXxmt2Kcir2VQnIkC48QLxPZ9yItYMltv9dt29"

#LOGIN
'''ws.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "login",
    "params": {
      "username": "113009",
      "password": "Srikakulam123",
      "client_id":client_id ,
      "client_secret": client_secret,
    },
    "id": 1
  }))

print(ws.recv())'''
'''
#AUTHORIZE
ws.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": {
      "client_id": client_id,
      "client_secret": client_secret,
      "debit": 10
    },
    "id": 1
  }))
print(ws.recv())

'''
#CREATE SESSION
ws.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "createSession",
    "params": {
      "_auth": _auth,
      "headset":"INSIGHT-5A688F16",
      "status": "open"
    },
    "id": 1
  }))

ws.recv()
# result = ws.recv()
# #print(result)
# asd = json.loads(result)
# session_id = asd['result']['id']
# print(session_id)





#SUBSCRIBE
ws.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "subscribe", 
    "params": {
      "_auth":_auth,
      # "session":session_id,
      "streams":[
        "sys"
      ]
    },
    "id": 1
  }))
ws.recv()


# ws.send(json.dumps(  {
#     "jsonrpc": "2.0", 
#     "method": "training", 
#     "params": {
#       "_auth":_auth,
#       "detection":"mentalCommand",
#       "action":"neutral",
#       "status":"reject"
#     }, 
#     "id": 1
#   }
# ))
# print(ws.recv())


input("PRESS KEY TO START TRAINING 'NEUTRAL COMMAND': ")




#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ws.send(json.dumps(  {
"jsonrpc": "2.0", 
"method": "training", 
"params": {
  "_auth":_auth,
  "detection":"mentalCommand",
  "action":"neutral",
  "status":"start"
}, 
"id": 1
}))

result = ws.recv()
print(result)
result = ws.recv()
time.sleep(5)
print(result)
result = ws.recv()
time.sleep(10)
print(result)


ws.send(json.dumps(  {
  "jsonrpc": "2.0", 
  "method": "training", 
  "params": {
    "_auth":_auth,
    "detection":"mentalCommand",
    "action":"neutral",
    "status":"accept"
}, 
"id": 1
}
))

print(ws.recv())
time.sleep(2)
print(ws.recv())

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


input("PRESS KEY TO START TRAINING 'CALL COMMAND' :")

ws.send(json.dumps(  {
	    "jsonrpc": "2.0", 
	    "method": "training", 
	    "params": {
	      "_auth":_auth,
	      "detection":"mentalCommand",
	      "action":"push",
	      "status":"start"
	    }, 
	    "id": 1
}))




	result = ws.recv()
	print(result)
	result = ws.recv()
	time.sleep(5)
	print(result)
	result = ws.recv()
	time.sleep(10)
	print(result)

	ws.send(json.dumps(  {
	    "jsonrpc": "2.0", 
	    "method": "training", 
	    "params": {
	      "_auth":_auth,
	      "detection":"mentalCommand",
	      "action":"push",
	      "status":"accept"
	    }, 
	    "id": 1
	  }
	))
	print(ws.recv())
	time.sleep(2)
	print(ws.recv())


	




# input("PRESS ANY KEY TO CONTINUE")



# ws.send(json.dumps(  {
#     "jsonrpc": "2.0", 
#     "method": "training", 
#     "params": {
#       "_auth":_auth,
#       "detection":"mentalCommand",
#       "action":"right",
#       "status":"start"
#     }, 
#     "id": 1
#   }))

# url_get = "http://192.168.0.5:5000/action4"
# res = requests.get(url_get)




# result = ws.recv()
# print(result)
# result = ws.recv()
# time.sleep(5)
# print(result)
# roveresult = ws.recv()
# time.sleep(10)
# print(result)

# ws.send(json.dumps(  {
#     "jsonrpc": "2.0", 
#     "method": "training", 
#     "params": {
#       "_auth":_auth,
#       "detection":"mentalCommand",
#       "action":"right",
#       "status":"accept"
#     }, 
#     "id": 1
#   }
# ))
# print(ws.recv())
# time.sleep(2)
# print(ws.recv())



# url_get = "http://192.168.0.5:5000/action0"
# res = requests.get(url_get)


#---------------------------THOUGHT STREAM----------------------------

ws.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "subscribe", 
    "params": {
      "_auth":_auth,
      #"session":session_id,
      "streams":[
        "com"
      ]
    },
    "id": 1
  }))
print(ws.recv())

# Python script for rover control
k = 0
while True:
  
  thought = json.loads(ws.recv())["com"][0]

  if(thought == "push"):
    print("Call Venkatesh")
    k = k + 1
  else:
    print("Neutral")
    k = 0
  
  if k == 16 :
    fun_call()
    break
  


  # if(thought == "push"):
  #   url_get = "http://192.168.0.8:5000/forward"
  #   res = requests.get(url_get)
  # elif(thought == "left"):
  #   url_get = "http://192.168.0.8:5000/pivot_left"
  #   res = requests.get(url_get)
  # elif(thought == "right"):
  #   url_get = "http://192.168.0.8:5000/pivot_right"
  #   res = requests.get(url_get)
  # for _ in range(4):
  #   print(json.loads(ws.recv())["com"][0])



  # if(thought == "push" and flag == 0):
  # 	print(thought)
  # 	url_get = "http://192.168.0.8:5000/forward"
  # 	res = requests.get(url_get)
  # 	time.sleep(3)
  # 	flag = 1
  
  # elif(thought == "left" and flag == 1):
  # 	print(thought)
  # 	url_get = "http://192.168.0.8:5000/pivot_left"
  # 	res = requests.get(url_get)
  # 	time.sleep(3)
  # 	flag = 0

