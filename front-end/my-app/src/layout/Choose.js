import React, { useEffect, useState } from 'react';
// import { useNavigate } from "react-router-dom"
import Modal from "./Modal";
import choose from "./choose.css"
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import socketIOClient from "socket.io-client";


function Choose(props) {
  // 매장식사, 포장 여부 모달
  const [takeoutModal, setTakeoutModal] = useState(true);

  // 결제 완료 모달
  const [payModal, setPayModal] = useState(false);

  // 먹고가기 선택 여부 state
  const [isSelect, setSelect] = useState(false);

  // 가져가기 선택 여부 state
  const [isClick, setClick] = useState(false);

  // 첫화면으로 이동
  const navigate = useNavigate()
const {location} = props;
  // useEffect(() => {
   
  //   if(isClick)
  //   {
  //     let color = document.getElementsByTagName("button");
  //     color[2].style.backgroundColor = "red";
  //     setClick(false);
  //   }

  //   if(isSelect)
  //   {
  //     let color = document.getElementsByTagName("button");
  //     color[1].style.backgroundColor = "red";
  //     setSelect(false);
  //   }

  //   set

  // }, [isClick, isSelect]); 
  
  function send()
  {
    const socket = socketIOClient("http://3.36.49.220:4001");
    socket.emit('react', 999);

  }


  return (
  <div>
      {takeoutModal && (
        <Modal closeModal={() => setTakeoutModal(!takeoutModal)}>
          <div id="rectangle">
            <button className="box" onClick={() => { 
              setSelect(!isSelect)
                setTakeoutModal(!takeoutModal)
                setPayModal(!payModal)
              }}> 먹고 가기 </button> 
            <button className="box" onClick={() => { 
              setClick(!isClick)
              setTakeoutModal(!takeoutModal)
              setPayModal(!payModal)}} > 가져 가기 </button>
          </div>
        </Modal>
      )}
        {payModal && (
        <Modal closeModal={() => setPayModal(!payModal)}>
          <div id="rectangle">
            <button className="bigbox" onClick={() => {
              setPayModal(!payModal);
              navigate('/'); send();}}> <div style={{margin:"120px"}}>결제가<br/>완료 되었습니다</div></button>     
          </div>
        </Modal>
        )}
  </div>
  );
}

export default Choose;

