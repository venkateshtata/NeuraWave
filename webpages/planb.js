const http = require('http');

const server  = http.createServer((req, res) => {
	console.log("listening...")
	if (req.method === 'POST'){
		let body = '';
		req.on('data', chunk => {
			body += chunk.toString();
		});
		req.on('end', () => {
			console.log(body);
			res.end('ok');
		});
	}

});

server.listen(7777);

console.log("listening...")