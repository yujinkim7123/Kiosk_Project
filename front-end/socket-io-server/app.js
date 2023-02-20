console.log("hello world")

const express = require("express");
const http = require("http");
const sockeIo = require("socket.io");


const port = process.env.PORT || 4001;
const index = require("./routes/index");
const app = express();
app.use(index);

const server = http.createServer(app);

const io = sockeIo(server, {
    cors: {
        origin: ['http://localhost:80', 'http://3.36.49.220:80','http://70.12.246.87:80', 'http://3.36.49.220', 'http://i8a203.p.ssafy.io'],
        megthods: ["GET", "POST"]
    }
});

let interval;



io.on("connection", (socket) =>{
    console.log("접속");
    let count = 0;
    socket.on("pi", (data) =>{
        console.log(`pi에서 들어온 메시지 수신${count}: ${data}`);
        socket.broadcast.emit('react', data);
        console.log(data);
        count ++;
    }); 

    socket.on("react", (data) =>{
        console.log(`react에서 들어온 메시지 수신: ${data}`);
        socket.broadcast.emit('pi', data);
    }); 

    socket.on("disconnect", () => {
        console.log("나감");
        clearInterval(interval);
    });
});


server.listen(port, ()=> console.log(`Listening on port ${port}`));
