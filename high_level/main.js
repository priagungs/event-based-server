var http = require('http');
var fs = require('fs'); 
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  console.log("Listening")
  if(req.url === "/small"){
    fs.readFile('../files/small.html', function (error, pgResp) {
        if (error) {
            res.writeHead(404);
            res.write('Contents you are looking are Not Found');
        } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(pgResp);
        }
        res.end();
    });
  }else if(req.url === "/large"){
    fs.readFile('../files/large.html', function (error, pgResp) {
        if (error) {
            res.writeHead(404);
            res.write('Contents you are looking are Not Found');
        } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(pgResp);
        }
        res.end();
    });
  }
}).listen(8080);