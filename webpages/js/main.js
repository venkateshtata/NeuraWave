
function pclicked(){

		var user = document.getElementById("un");
		var pass = document.getElementById("pw");

		if(user.value == "123" && pass.value == "123"){
			window.location = 'producercategories.html'
		}
}

function cclicked(){

		var user = document.getElementById("un");
		var pass = document.getElementById("pw");

		if(user.value == "123" && pass.value == "123"){
			window.location = 'consumercategories.html'
		}
}

function uploadgood(){

        if (confirm("Do you confrim this upload?")) {
        window.location = 'Portal.html';
    }
}

function buy() {
		var Web3 = require('web3')
		var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))
	    if(confirm("Do you confirm this purchase?")){}
		// var Web3 = require('web3')
		// var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))
        

		//send eth
		

		var buyer = "0x40bf0de7aaaa20aba9951b5a8f940f8c3938af02"
		var seller = "0xb75e6a7109a7878c409336af8b249e8c2c0db5d6"
		web3.eth.sendTransaction({from:buyer, to:seller, value:web3.toWei(10,'ether'),gasLimit:21000,gasPrice:2000000})

		//make var with hash
		//var txHash = _
		//console.log(web3.eth.getTransaction(txHash))
	}

function check(){
	
	var Web3 = require('web3')
	var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))

	var txHash = document.getElementById("hashtemp").value

	trans = JSON.stringify(web3.eth.getTransaction(txHash))
	window.alert(trans)
	
}
