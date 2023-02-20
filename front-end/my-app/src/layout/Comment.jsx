import React from "react";

const styles = {
    wrapper:{
        margin: 0,
        padding: 10,
        border: "1px solid grey",
        borderRadius: 0,
        display: "flex",
        backgroundColor: "#D9D9D9",
    },
    nameText:{
        color: "black",
        fontSize: 25,
        fontWeight: "bold",
        marginLeft: "13%",
        width: "200px",   
    }
};
function Comment(props){
    return(
       <div style={styles.wrapper}>
         <div style={styles.nameText}>{props.menu}</div>
         <div style={styles.nameText}>{props.count}</div>
         <div style={styles.nameText}>{props.price}</div>
        </div>
    );
}
export default Comment;