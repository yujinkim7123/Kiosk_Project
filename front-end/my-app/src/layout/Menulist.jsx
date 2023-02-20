import React, {userState, useState, useEffect} from "react";
import Comment from "./Menu";
import Jsonfle1 from "../db/recommend.json"
import Jsonfle2 from "../db/setmenu.json"
import Jsonfle3 from "../db/single.json"
import Jsonfle4 from "../db/drink.json"
import Jsonfle5 from "../db/sidemenu.json"

const styles = {
    wrapper:{
        margin: 0,
        padding: 25,
        display: "flex",
        flexDirection:"row",
        flexWrap: "wrap",
        width: "75%",
        borderTop: "2px solid grey",
        borderIeft: "2px solid grey",
        borderRadius: 0,
        justifyContent: "space-between",
    },
};

function MenuList(props)
{

  let jsonfile = [];
  const [,setCount] = useState(1);
  const save = localStorage.getItem('reacommend');
  Jsonfle1 = JSON.parse(localStorage.getItem('reacommend'));
  jsonfile.push(Jsonfle1);
  jsonfile.push(Jsonfle2);
  jsonfile.push(Jsonfle3);
  jsonfile.push(Jsonfle4);
  jsonfile.push(Jsonfle5);
  
  const [select, setselect] = useState(-1);

    useEffect(() => {
        if(props.sidecheck > 1){

          if(select !== -1){
          let list = document.getElementsByClassName('menu');
  
          for(let i = 0; i < list.length; i++)
          {
              list[i].style.backgroundColor  = "#FDF0D5";
          }

          list[select - 1].style.backgroundColor="#C1121F";
          }
        }
      },[props.menu]);


      useEffect(() => {    
        setCount({});
    
      },[props.type]);
    

      if(save === null && props.number === 1)
      { 
        return(<div style={styles.wrapper}></div>);
      }
      else
      {
        return (
          <div style={styles.wrapper}>
            { 
              jsonfile[props.number - 1].map((comment, id) => { 
                console.log(props.number);
                if(props.number === 1){
                  if(id < 2){
                    return (<Comment imageMenu={props.imageMenu} key={id} name={comment.menuName} price={comment.menuPrice} setuse={setselect} side={props.side} number={props.number}  setprice={props.setprice}/>);
                  }
                }
                else{
                    return (<Comment imageMenu={props.imageMenu} key={comment.id} id={comment.id} name={comment.name} price={comment.price} setuse={setselect} side={props.side} number={props.number}  setprice={props.setprice}/>);
                }
              })
            }
          </div>  
        );
    }

}

export default MenuList;
