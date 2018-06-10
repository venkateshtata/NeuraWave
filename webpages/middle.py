from flask import Flask, request, Response, jsonify
import json
from websocket import create_connection
import ssl
import json
import time
import wait_response
from wait_response import wait_response_status
import requests

_auth="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS4xMTMwMDkuc2V2ZW50aCIsImV4cCI6MTUyODc2ODA1MywiZmlyc3ROYW1lIjoidmVua2F0ZXNoIiwibGFzdE5hbWUiOiJUYXRhIiwibGljZW5zZUlkIjoiMDU3MTRlZmQtZjcwNy00OGMwLWJkNzQtNDU2N2RiYjM0ZTVkIiwibGljZW5zZVNjb3BlIjoyLCJsaWNlbnNlX2FncmVlbWVudCI6eyJhY2NlcHRlZCI6dHJ1ZSwibGljZW5zZV91cmwiOiJodHRwczovL3d3dy5lbW90aXZjbG91ZC5jb20vZGJhcGkvcHJpdmFjeS9kb2MvZXVsYS8ifSwibGljZW5zZV9leHBpcmUiOjE1MzA5ODgxOTksImxpY2Vuc2VfaGFyZExpbWl0IjoxNTMwMzE2Nzk5LCJsaWNlbnNlX3NvZnRMaW1pdCI6MTUyOTcxMTk5OSwibmJmIjoxNTI4NTA4ODUzLCJ1c2VyQ2xvdWRJZCI6MzU3ODQsInVzZXJuYW1lIjoiMTEzMDA5In0.mmiWZzC4eBp4E_w4Qiu6stiGa_uchQMpXL9ZnJrCXZY"
client_secret = "93KE83MORyTci3v4hewngDzerzDdxAkrP1BNqrn84oOhD6tNeF9pLbOWHwlsO29eYq0YmGS0ECyOEGgrWabh6PWDMVkxbYd12ASm1CVUCtwdFyCcX4QX6V1oRWJXx0fp"
client_id = "mACXxmt2Kcir2VQnIkC48QLxPZ9yItYMltv9dt29"



url_post = "http://192.168.15.208:7777"

app = Flask(__name__)
a = 10

@app.route('/create', methods=['POST'])
def create():
    if request.method == "POST":
        print("IN POST")
        data = json.loads(request.data)
        try:
            my_list.append(data)
            return Response(json.dumps(a)), 200
        except(Exception,e):
            return Response(
                json.dumps("SORRY !!! Something bad happened in POST.")), 500


@app.route('/list', methods=['GET'])
def list():
    if request.method == "GET":
        try:
            ws = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})
            print("started")
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

            result1 = ws.recv()
            print(result1)
            requests.post(url_post, data=result1)
            result2 = ws.recv()
            time.sleep(5)
            print(result2)
            requests.post(url_post, data=result2)
            result3 = ws.recv()
            time.sleep(10)
            print(result3)
            requests.post(url_post, data=result3)


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

            result4 = ws.recv()
            requests.post(url_post, data=result4)
            time.sleep(2)
            result5 = ws.recv()
            requests.post(url_post, data=result5)

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




            result6 = ws.recv()
            print(result6)
            requests.post(url_post, data=result6)
            result7 = ws.recv()
            time.sleep(5)
            print(result7)
            requests.post(url_post, data=result7)
            result8 = ws.recv()
            time.sleep(10)
            print(result8)
            requests.post(url_post, data=result8)

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
            result9 = ws.recv()
            requests.post(url_post, data=result9)
            time.sleep(2)
            result10 = ws.recv()
            requests.post(url_post, data=result10)

            ws.send(json.dumps(  {
                        "jsonrpc": "2.0", 
                        "method": "training", 
                        "params": {
                            "_auth":_auth,
                            "detection":"mentalCommand",
                            "action":"left",
                            "status":"start"
                        }, 
                        "id": 1
            }))




            result11 = ws.recv()
            print(result11)
            requests.post(url_post, data=result11)
            result12 = ws.recv()
            time.sleep(5)
            print(result12)
            requests.post(url_post, data=result12)
            result13 = ws.recv()
            time.sleep(10)
            print(result13)
            requests.post(url_post, data=result13)

            ws.send(json.dumps(  {
                "jsonrpc": "2.0", 
                "method": "training", 
                "params": {
                  "_auth":_auth,
                  "detection":"mentalCommand",
                  "action":"left",
                  "status":"accept"
                }, 
                "id": 1
              }
            ))
            result14 = ws.recv()
            requests.post(url_post, data=result14)
            time.sleep(2)
            result15 = ws.recv()
            requests.post(url_post, data=result15)
            ws.send(json.dumps({
                "jsonrpc": "2.0",
                "method": "subscribe", 
                "params": {
                    "_auth":_auth,
                    "streams":[
                    "com"
                    ]
                },
                "id": 1
            }))

            flag = 0
            while True:
                thought = json.loads(ws.recv())["com"][0]
                if(thought == "push" and flag == 0):
                    requests.post(url_post, data=thought)
                    print(thought)
                    url_get = "http://192.168.0.8:5000/forward"
                    requests.get(url_get)
                    time.sleep(3)
                    flag = 1
                elif(thought == "left" and flag == 1):
                    requests.post(url_post, data=thought)
                    print(thought)
                    url_get = "http://192.168.0.8:5000/pivot_left"
                    requests.get(url_get)
                    time.sleep(3)
                    flag = 0

            return Response(json.dumps("DONE")), 201
        except Exception as e:
            print(e)
            return Response(json.dumps("SORRY !!! Something bad happened in GET.")), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)