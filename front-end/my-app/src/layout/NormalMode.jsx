import React , {useState,  useEffect}from 'react';
import CommentList from './CommentList';
import Sidebar from './sidebarlist2'
import Header from './Header'
import CustmerList from './CustmerList';
import easycss from './easymode.css';

const styles = {
    wrapper:{
        margin: 0,
        padding: 0,
        display: "flex",
        flexDirection:"row",
        borderRadius: 0,
    },
  };
  


function NormalMode(props) {


  const [selectMenu, setMenu] = useState('');
  const [check, setcheck] = useState('');
  const [check2, setcheck2] = useState('');
  const [custmercheck, setcustmer] = useState(false);
  const [sidecheck, setside] = useState(1);
  const [selectmenu, setmenu] = useState('없음');
  const [price, setprice ] = useState(0);


  useEffect(() => {       
          if (props.height === 1) {
            // console.log(1)
            document.getElementById("level").style.transform = "translateY(0px)"
            document.getElementById("level").style.transition = "transform 2s" 
          } else if (props.height === 2) {
            // console.log(2)
            document.getElementById("level").style.transform = "translateY(250px)"
            document.getElementById("level").style.transition = "transform 2s"
          } else {
            // console.log(3)
            document.getElementById("level").style.transform = "translateY(590px)"
            document.getElementById("level").style.transition = "transform 2s"
          }  
          },[]);
          console.log(custmercheck)
    return (
      <div id="level">
      <Header stye={{border:"1px"}}  settype={props.settype} type={props.type}/>
      {!custmercheck && <Sidebar imagemenu={setMenu} setcustmer={setcustmer} sidecheck={sidecheck} setside={setside} setprice={setprice} checkfun={setcheck2}/>}
      {custmercheck && <CustmerList imagemenu={selectMenu} checkfun={setcheck} check={check}  setcustmer={setcustmer} custmercheck={custmercheck} setmenu={setmenu} selectmenu={selectmenu}/>}
      <CommentList imagemenu={selectMenu} checkfun={setcheck} check={check} selectmenu={selectmenu} price={price} settype={props.settype} check2={check2}/> 
      </div>
  
    );
  }
  
  export default NormalMode;