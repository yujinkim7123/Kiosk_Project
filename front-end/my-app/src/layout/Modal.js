import React from "react";
import choose from "./choose.css"
// import ModalItem from "./ModalItem"
import { Link, Route, Switch, BrowserRouter as Router } from "react-router-dom";

function Modal(props) {
 
function closeModal() {
  props.closeModal(); 
  }

  const value = localStorage.getItem('height');
  var index = "0px";
  if(Number(value) === 1)
  {
    index = "0px";
  }
  else if(Number(value) === 2)
  {
    index = "300px";
  }
  else if(Number(value) === 3)
  {
    index = "650px";
  }
 // document.getElementByClassName("Modal").style.top = "100px";



    return (

      <div className="Modal" style={{top: `${index}`}}onClick={closeModal}>
        <div className="modalBody" onClick={(e) => e.stopPropagation()}>
          <Link to="/">
          <button id="modalCloseBtn" onClick={closeModal}>
            <span style={{fontSize : "70px"}}>❌</span>
          </button>
          </Link>
          {/* <ModalItem/>   */}
          {props.children}
        </div>
      </div>
    );
  }     
export default Modal;

