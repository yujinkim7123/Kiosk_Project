import React from "react";
import { Link } from "react-router-dom";

const styles = {
    wrapper:{
        marginBottom: 15,
        padding: 0,
        textAlign: "center",
        marginLeft: "120px",
      
    },
    text:{
      fontWeight: "bolder",
      fontSize: 60,
      color: "#003049"
    },
    btn:{
      backgroundColor: "#003049",
      fontWeight: 1000,
      fontSize: "30px",
      color: "white",
      border: 0,
      borderRadius: "0.4em",
      height: 70,
      float: "right",
      marginTop: "12px",
      marginRight: "20px",
    
    }
};

function headerText(props)
{
    return (
    <div>
      <div style={styles.wrapper}>
        <span style={styles.text}>INBurger</span>    
        {props.type===2 && <button style={styles.btn} onClick={() => props.settype(1)}>간편모드</button>} 
      </div>
    </div>  
    );
}

export default headerText;
