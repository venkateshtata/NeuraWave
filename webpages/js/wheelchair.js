function wheelchair(){
	var stat = document.getElementById("status");
	var request = require('request');
	url = "wss://emotivcortex.com:54321"
	client_secret = "hssnlmFMOjAo6d3KCCm8Wczy4M0ZOM0ldZjTtyXvPDb3gJpGV7YfRQReecYR5MhYowlNHjUB2LszqFQ9CTYCxHNYPpSFFr3jcl5YepDEJYYTCnED5g1jJCzfzZaRaSBs"
	client_id = "SZYEX5zTzBnzZ6BbLwxLfdcBy8shV5H57wSEHziZ"
	auth = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS4xMTMwMDkuZWlnaHRoIiwiZXhwIjoxNTI4Njk3MDMwLCJmaXJzdE5hbWUiOiJ2ZW5rYXRlc2giLCJsYXN0TmFtZSI6IlRhdGEiLCJsaWNlbnNlSWQiOiIwNTcxNGVmZC1mNzA3LTQ4YzAtYmQ3NC00NTY3ZGJiMzRlNWQiLCJsaWNlbnNlU2NvcGUiOjIsImxpY2Vuc2VfYWdyZWVtZW50Ijp7ImFjY2VwdGVkIjp0cnVlLCJsaWNlbnNlX3VybCI6Imh0dHBzOi8vd3d3LmVtb3RpdmNsb3VkLmNvbS9kYmFwaS9wcml2YWN5L2RvYy9ldWxhLyJ9LCJsaWNlbnNlX2V4cGlyZSI6MTUzMDk4ODE5OSwibGljZW5zZV9oYXJkTGltaXQiOjE1MzAzMTY3OTksImxpY2Vuc2Vfc29mdExpbWl0IjoxNTI5NzExOTk5LCJuYmYiOjE1Mjg0Mzc4MzAsInVzZXJDbG91ZElkIjozNTc4NCwidXNlcm5hbWUiOiIxMTMwMDkifQ.xqtoWQ-qHNJbo8APYzTiLXyQhBAQXlunlLhjDWN3Hz8"

	command = ["neutral", "push", "left"]
	i = 0
	k = 0

	var WebSocket = require('ws')
	w = new WebSocket(url, null, {rejectUnauthorized: false});


	function sleep(milliseconds) {
	  var start = new Date().getTime();
	  for (var i = 0; i < 1e7; i++) {
	    if ((new Date().getTime() - start) > milliseconds){
	      break;
	    }
	  }
	}



	w.onopen = function(){
		console.log("open web socket");
		request.get('http://192.168.43.235:5000/pivot_left');


	//-----LOGIN TO DEVICE------
	/*	w.send(JSON.stringify({
	    "jsonrpc": "2.0",
	    "method": "authorize",
	    "params": {
	      "client_id": client_id,
	      "client_secret": client_secret,
	      "debit": 10
	    },
	    "id": 1
	  }));
	*/
	//-------------------------


	w.send(JSON.stringify({
	    "jsonrpc": "2.0",
	    "method": "createSession",
	    "params": {
	      "_auth": auth,
	      "headset":"INSIGHT-5A688F16",
	      "status": "open"
	    },
	    "id": 1
	  }));


	//-----FOR CLOSING SESSION----
	/*w.send(JSON.stringify({
	  "jsonrpc": "2.0",
	  "method": "updateSession",
	  "params": {
	    "_auth": auth,
	    "status": "close",
	  },
	  "id": 1
	}));
	*/
	//----------------------------


	w.send(JSON.stringify({
	    "jsonrpc": "2.0",
	    "method": "subscribe", 
	    "params": {
	      "_auth":auth,
	      "streams":[
	        "sys"
	      ]
	    },
	    "id": 1
	  }));

	//--------NEUTRAL TRAINING-------
	w.send(JSON.stringify( {
		    "jsonrpc": "2.0", 
		    "method": "training", 
		    "params": {
		      "_auth":auth,
		      "detection":"mentalCommand",
		      "action":"neutral",
		      "status":"start"
		    }, 
		    "id": 1
		  }));


	setTimeout(function(){
		w.send(JSON.stringify(  {
		    "jsonrpc": "2.0", 
		    "method": "training", 
		    "params": {
		      "_auth":auth,
		      "detection":"mentalCommand",
		      "action":"neutral",
		      "status":"accept"
		    }, 
		    "id": 1
		  }))

		setTimeout(function(){

			w.send(JSON.stringify( {
		    "jsonrpc": "2.0", 
		    "method": "training", 
		    "params": {
		      "_auth":auth,
		      "detection":"mentalCommand",
		      "action":"push",
		      "status":"start"
		    }, 
		    "id": 1
		  	}));
			
			setTimeout(function(){
				w.send(JSON.stringify(  {
			    	"jsonrpc": "2.0", 
			    	"method": "training", 
			    	"params": {
			      	"_auth":auth,
			      	"detection":"mentalCommand",
			      	"action":"push",
			      	"status":"accept"
			    	}, 
			    	"id": 1
		  		}))


				setTimeout(function(){
					w.send(JSON.stringify( {
					    "jsonrpc": "2.0", 
					    "method": "training", 
					    "params": {
					      "_auth":auth,
					      "detection":"mentalCommand",
					      "action":"left",
					      "status":"start"
					    }, 
					    "id": 1
					  	}));

					setTimeout(function(){
						w.send(JSON.stringify(  {
					    	"jsonrpc": "2.0", 
					    	"method": "training", 
					    	"params": {
					      	"_auth":auth,
					      	"detection":"mentalCommand",
					      	"action":"left",
					      	"status":"accept"
					    	}, 
					    	"id": 1
		  				}))

		  				w.send(JSON.stringify({
							"jsonrpc": "2.0",
							"method": "subscribe", 
							"params": {
							"_auth":auth,
							"streams":[
						    "com"
						      ]
						    },
							"id": 1
						}))

					},15000);

				},5000);


			},15000);
		

		},5000);


	},15000);


	}


	w.onmessage = function(e){
		if(JSON.parse(e.data)["com"])
		{
			var thought = JSON.parse(e.data)["com"];
			if(thought[0] == "push" && k == 0)
			{
				request.get('http://192.168.43.235:5000/forward');
				console.log(thought)//
				stat.value = thought;
				k = 1
				
			}
			else if(thought[0] == "left" && k == 1)
			{
				request.get('http://192.168.43.235:5000/pivot_left');
				console.log(thought)//
				stat.value = thought;
				k = 0
			
			}
		}
		

		if(JSON.parse(e.data)["sys"])
		{	
			
			var current = JSON.parse(e.data)["sys"]
			if(current[1] == "MC_Started" || current[1] == "MC_Completed")
			{
				if(current[1] == "MC_Started")
				{
					console.log("Training for " + command[i] + " has started");//
					stat.value = "Training for " + command[i] + " has started";
				}
				
				else if(current[1] == "MC_Completed")
				{
					console.log("Training for " + command[i] + " has been completed");//
					stat.value = "Training for " + command[i] + " has been completed";
					i = i + 1;
				}

				
			}	

			else{
				console.log(current);
				stat.value = current;
			}
		}	
		

		else{
			console.log(e.data.toString());
			stat.value = e.data.toString();
		}
	}



	w.onclose = function(e){
		console.log(e.data.toString());
	}
	w.onerror = function(e){
		console.log(e.data.toString());

	}

}


function hello()
{

	var stat = document.getElementById("status");
	stat.value = "hi";
}