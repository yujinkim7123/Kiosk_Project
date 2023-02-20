import React, { useState, useEffect } from "react";
import Menu from "./Menulist2"

const comments = [
  {
    id:1,
    name: "추천메뉴",
  },
  {
    id:2,
    name: "세트만",
  },
  {
    id:3,
    name: "버거만",
  },
  {
    id:4,
    name: "음료",
  }
  ,  
  {
    id:5,
    name: "사이드",
  }
 
];

const styles = {
  wrapper2:{
    margin: 0,
    padding: 5,
    display: "flex",
    flexDirection:"row",
    borderBottom: "1px solid black",
    borderTop: 0,
    borderLeft: 0,
    borderRight: 0,
    borderRadius: 0,
    height: 150,
    width: "100%",
    justifyContent: "center",
    backgroundColor: "#FDF0D5",
},
nameText:{
    color: "black",
    fontSize: 35,
    fontWeight: "bold",
    lineHeight : 4.5,
},
  wrapper:{
      margin: 0,
      padding: 0,
      width: "25%",
      borderRadius: 0,
  },
  wrapper3:{
    margin: 0,
    padding: 0,
    display: "flex",
    flexDirection:"row",
    borderRadius: 0,
},

};

let count = 1;

function Sidebalist2(props)
{
  const [,setCount] = useState(0);
  
  let incrementCount = (e) =>{

  count = e;
  console.log(e);
  let list =  document.getElementsByClassName("sidebar");

  for(let i = 0; i < 5; i++)
  {
    list[i].style.backgroundColor = "#FDF0D5";
  }
  list[count - 1].style.backgroundColor = "#C1121F";

  let list2 = document.getElementsByClassName("menu");
   for(let i = 0; i < list2.length; i++)
      list2[i].style.backgroundColor  = "#FDF0D5";

      props.imagemenu("없음");
      props.setside(e);
      setCount({});
  }

  useEffect(() => { 
    let list =  document.getElementsByClassName("sidebar");
    list[0].style.backgroundColor = "#C1121F";
  },[]);


    return (
      <div  style={styles.wrapper3}>
      <div style={styles.wrapper}>
        {comments.map((comment) => {
            return (
            <button className="sidebar" key={comment.id} onClick={()=>incrementCount(comment.id)} style={styles.wrapper2}>
            <span style={styles.nameText}>{comment.name}</span>
           </button>
           );
          })}
        </div>
          <Menu imageMenu={props.imagemenu} number={count} setcustmer={props.setcustmer} sidecheck={props.sidecheck} setside={props.setside} setprice={props.setprice} checkfun={props.checkfun}></Menu>
        </div>
    );
}


export default Sidebalist2;

