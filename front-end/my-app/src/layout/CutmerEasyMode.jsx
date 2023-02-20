// 이지모드 선택 메뉴 이미지창
import React, { useEffect } from 'react'
import { useState } from 'react'
import CustmerEasyModeCSS from './CutmerEasyMode.css'
import { Link } from "react-router-dom";

export default function CutmerEasyMode(props) {

    const [state, setstate] = useState(0);
    const [, setcount] = useState(0);


   useEffect(() => {
        if(props.imagemenu !== ''){
        props.checkfun(state);
        }
    },[state]);

    useEffect(() => {
     props.setimagemenu("없음");
      setcount({});
  },[props.sidecheck]);
    
  return (
    <div className='imagebar'>
        <img className="imagechange"src={process.env.PUBLIC_URL + `./images/${props.imagemenu}.png`}/>
        <div className="btn">
            <button className="blue" onClick={()=>{console.log(2); props.settype(2)}}>일반모드</button>
            <button  onClick={()=> setstate(state + 1)} className="blue" >이거먹기</button>
        </div>
    </div>
  )
}
