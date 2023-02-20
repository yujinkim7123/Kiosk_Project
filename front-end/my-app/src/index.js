import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import EasyMode from './layout/EasyMode';
import NomalMode from './layout/NormalMode';
import Choose from './layout/Choose';
import reportWebVitals from './reportWebVitals';
import { Link, Route, BrowserRouter ,Routes } from "react-router-dom";
import Delay from './layout/delay';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
   <BrowserRouter>
    <App />
      <Routes>
        <Route path="/Easy" element={ <EasyMode /> }></Route>
        <Route path="/NomalMode" element={ <NomalMode /> }></Route>
        <Route path="/Choose" element={ <Choose /> }></Route>
        <Route path="/Delay" element={ <Delay /> }></Route>
      </Routes>
    </BrowserRouter>

);

reportWebVitals();
