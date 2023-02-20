import React from "react";


const styles = {

    nameTextS:{   
        border: 0,
        width:"250px",
        height:"100%",
        margin: "-36.5px",
        transform: "rotateX(50deg)",
      
    },
    menuBoxS:{
       position: "relative",
       bottom: "-45px",
       padding: 0,
       margin: 0,
       border: 0,
       width: "100%",
       backgroundColor: "#F5F5F5",
      
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