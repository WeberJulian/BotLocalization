var app = require('express')();
var express = require('express')
app.use(express.static('files'))
var http = require('http').Server(app);
var io = require('socket.io')(http);
const fs = require('fs');
const readLastLines = require('read-last-lines');
var THREE = require('three');


file = "./positions.log"

app.get('/', function(req, res){
  res.sendFile(__dirname + '/visu.html');
});

app.get('/event', function(req, res){
  res.send("Event")
  io.emit("event")
});

io.on('connection', function(socket){
  console.log('a user connected');
});

fs.watchFile(file, { interval: 100 }, () => {
  console.log("New pos");
  readLastLines.read(file, 1)
    .then((lines) => {
      lines = lines.split("|")
      for (var i = 0; i < lines.length; i++){
        lines[i] = lines[i].split(" ")
      }
      io.emit("event", lines)
    });
  
  
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});