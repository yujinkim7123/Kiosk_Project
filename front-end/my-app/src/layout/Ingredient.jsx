import React, { useEffect } from "react";


const styles = {
    nameTextS:{   
        border: 0,
        width:"150px",
        height:"100%",
        marginTop: 30,
    },
    menuBoxS:{
        position: "relative",
        top: "5px",
        padding: 0,
        margin: 0,
        border: 0,
        borderRadius: 50,
        width: "100%",
        backgroundColor: "#F5F5F5",
    } 
};

function Ingredient(props){
    return(
        <button onClick={()=>{props.setmenu(props.name); props.setcheck(1);}}style={styles.menuBoxS}>
         <img style={styles.nameTextS} src={process.env.PUBLIC_URL + `./images/${props.name}.png`} alt={props.name}/>
        </button>
    );
}

export default Ingredient;