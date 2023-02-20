import React from "react";


const styles = {
    nameTextS:{   
        border: 0,
        width:"350px",
        height:"100%",
        marginTop: 10,
    },
    menuBoxS:{
       position: "relative",
       top: "30px",
       padding: 0,
       margin:0,
       border: 0,
       backgroundColor: "#F5F5F5",
       width: "100%",
    } 
};

function Ingredient(props){
    return(
        <button style={styles.menuBoxS}>
         <img style={styles.nameTextS} src={process.env.PUBLIC_URL + `./images/${props.name}.png`} alt={props.name}/>
         </button>
    );
}

export default Ingredient;