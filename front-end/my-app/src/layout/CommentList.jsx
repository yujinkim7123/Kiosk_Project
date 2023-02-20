import React , {useState,useCallback, useEffect, useMemo}from "react";
import Comment from "./Comment";
import { Link, Route, Switch, BrowserRouter as Router } from "react-router-dom";
import Choose from "./Choose";
import CommentListcss from "./CommentList.css";
import jsonfle from "../db/menuprice.json";

let Maxid;
var pp = 0;

function CommentList(props)
{
  const [Cartlist, setCart] = useState([]);


  useEffect(() => {
    if(props.imagemenu !== ''){

      var addcomment = {};
      
      if(props.sidecheck === 1)
      {
        addcomment = {
          id: `${Maxid + 1}`,
          name: props.imagemenu,
          price: `${props.price + pp}`,
          count: 1,
        }
      }
      else{
        addcomment = {
        id: `${Maxid + 1}`,
        name: props.imagemenu,
        price: `${jsonfle[props.imagemenu].price + pp}`,
        count: 1,
        }
      }
      pp = 0;
      setCart([...Cartlist, addcomment]);
    }

  }, [props.check]);

  useEffect(() => {
    if(props.imagemenu !== ''){
     
      var addcomment = {};
      
      if(props.sidecheck === 1)
      {
        addcomment = {
          id: `${Maxid + 1}`,
          name: props.imagemenu,
          price: `${props.price + pp}`,
          count: 1,
        }
      }
      else{
        addcomment = {
        id: `${Maxid + 1}`,
        name: props.imagemenu,
        price: `${jsonfle[props.imagemenu].price + pp}`,
        count: 1,
        }
      }
      pp = 0;
      setCart([...Cartlist, addcomment]);
    }

  }, [props.check2]);

  useEffect(() => {
    if(props.selectmenu !== '없음'){
         pp = pp + 100;
    }
  }, [props.selectmenu]);
  
const Sumprice = () =>{

    let total = 0;
    
    Cartlist.map((comment) => {
      total += Number(comment.price);
    })
    console.log(total);
    return total;
  }

  const location1 = useMemo(() =>Sumprice(), [Cartlist]);


    return (
      <div className="wrapper">
        <div className="wrapper2"> 
         <div className="headerText">메뉴</div>
         <div className="headerText">갯수</div>
         <div className="headerText">가격</div>
        </div>
        <div style={{ height: "200px", overflow: "auto"}}>
        {Cartlist.map((comment) => {
            Maxid = comment.id;
            return (<Comment key={comment.id} menu={comment.name} count={comment.count} price={comment.price}/>);
          })}
          </div>  
        <div className="wrapper2"> 
         <div className="headerText">총합</div>
         <div className="headerText">{location1}</div>
         <Link to={{pathname:"/Choose",
                    type: props.settype,
                    }}> 
         <button  className="Button">결제</button>
         </Link>
        </div>
      </div>  
    );
}


export default CommentList;


