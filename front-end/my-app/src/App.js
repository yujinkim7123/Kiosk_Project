import './App.css';
import React, {userState, useState, useEffect} from "react";
import io from 'socket.io-client';
import { Link, Route, BrowserRouter , Routes } from "react-router-dom";
import axios from 'axios'
import Delay from './layout/delay';
import EasyMode from './layout/EasyMode';
import NomalMode from './layout/NormalMode';
import socketIOClient from "socket.io-client";


function App() {

  const [type, settype] = useState(0);
  const [height, setheight] = useState(1);
  const [name, setname] = useState('none');


  useEffect(()=>
  {
    const socket = socketIOClient("http://3.36.49.220:4001");
    socket.on('react', (data) => {

      setname(data['name']);
      setheight(data['height']);
      settype(data['mode']);

      axios.post('http://3.36.49.220:8081/inburger/menu/user', {
        name: data['name'],
        height: data['height'],
        isEasy: data['mode']
      },{
        headers: {
            'Access-Control-Allow-origin' : 'http://3.36.49.220:8081',
            'Access-Control-Allow-Credentials': true,
            'Content-Type' : 'application/json'
          },
          proxy: {
            host: '3.36.49.220',
            port: 80
          },
        }).then((response) => {
          console.log(response.data);
          localStorage.setItem('reacommend', JSON.stringify(response.data));
          localStorage.setItem('height', data['height']);
        })
      .catch((err)=> {
      console.log('errot!')
      console.log(err)});

  });

  }, []);

   if(type === 0){
     return (
      
       <Delay height={height}/>
      
     );
   }
   else if(type === 1){
       return(
       
       <EasyMode height={height} settype={settype} type={type}/>
     
       );
   }
   else if(type === 2)
   {
       return(
       
       <NomalMode height={height} settype={settype} type={type}/>
     
       );
   }

}

export default App;
