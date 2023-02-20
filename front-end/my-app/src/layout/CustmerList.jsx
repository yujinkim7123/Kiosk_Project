import CustmerBar from "./CustmerBar";
import CustmerSide from "./CustmerSide";
import CustmerImage from "./CustmerImage";
import React, {userState, useState, useEffect} from "react";
import toggle from './toggle.css'
import { Link} from "react-router-dom";


const styles = {
    wrapper:{
        margin: 20,
        padding: 0,
        borderRadius: 30,
        display: "flex",
        flexDirection:"column",
        height: 900,
        backgroundColor: "#D6CECE",
    },
    wrapper2:{
        margin: 0,
        borderRadius: 20,
        display: "flex",
        flexDirection:"row",
        backgroundColor: "#D6CECE",
    },
    wrapper3:{
        margin: 6,
        borderRadius: 20,
        display: "flex",
        flexDirection:"row-reverse",
        flexWrap: "wrap",
        justifyContent:"space-between",
     
    },
    menuBox:{
        margin: 0,
        padding: 0,
        border: "1px solid grey",
        borderRadius: 20,
        width: "20%",
    },
    Button: {
        width: 150,
        height: 80,
        textAlign: "center",
        lineHeight : 2,
        border: 0,
        borderRadius: 25,
        fontSize: 30,
        marginTop: "15px",
        marginRight: "10px",
        backgroundColor: "#006400",
        fontColor: "white",
    }

};
function CustmerList(props){

    const [selectbutton, setbutton] = useState('패티');
    const [custmenu, setcustmenu] = useState('')
    const [state, setstate] = useState(0);
    const [seleccheck, setcheck] = useState(0);
    const [togglech, settoggle] = useState(true);

    return(
        <div style={styles.wrapper}>
        <div style={styles.wrapper3}>
        <button style={styles.Button} onClick={()=> {props.setcustmer(!props.custmercheck); props.checkfun(!props.check)}}><span style={{color:"white"}}>담기</span></button>
        <input type="checkbox" id="toggle" hidden /> 
        <label htmlFor="toggle" className="toggleSwitch" onClick={() => settoggle(!togglech)}>
        {togglech && <span className="toggleButton">세트</span>}
        {!togglech && <span className="toggleButton">단품</span>}
        </label>
        </div>

        <CustmerBar  setbutton={setbutton}/>
         <div style={styles.wrapper2}>
        <CustmerSide selectbutton={selectbutton} selectmenu={props.selectmenu} setmenu={props.setmenu}  setcustmerlist={props.setcustmerlist} />
        <CustmerImage menuname={props.imagemenu} selectmenu={props.selectmenu} setmenu={props.setmenu} togglech={togglech} check = {props.check}/>
         </div>
        </div>
     );
}


export default CustmerList;