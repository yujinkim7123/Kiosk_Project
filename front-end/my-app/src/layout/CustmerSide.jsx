import React, {userState, useState, useEffect} from "react";
import Jsonfle from "../db/sidebutton.json"
import Ingredient from "./Ingredient"


const styles = {
    wrapper:{
        marginLeft: 0,
        padding: 0,
        borderRadius: 20,
        backgroundColor: "#F5F5F5",
        width: "40%",
        height: 600,
        margin: "20px",
    },
};


function CustmerSide(props){
    let keyitems = 0;
    
    return(
        <div style={styles.wrapper}>
        {Jsonfle[props.selectbutton]["name"].map((comment) => {
            return (<Ingredient key={keyitems++} name={comment} selectmenu={props.selectmenu} setmenu={props.setmenu}  setcustmerlist={props.setcustmerlist}/>);
          })}
       </div>
    );
}


export default CustmerSide;