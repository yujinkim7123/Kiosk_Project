import React, {userState, useState, useEffect} from "react";
import Ingredient from "./Ingredient2";
import Ingredient3 from "./Ingredient3";
import Jsonfle from "../db/menusetting.json"
//-1: 빼기 1: 넣기//

const styles = {
    wrapper:{
        display: "flex",
        flexDirection:"row",
        padding: 0,
    },
    foodBox:{
        padding: 0,
        margin: 0,
        border:"1px",
        width: "70%",
        backgroundColor: "#F5F5F5",
        borderRadius: 20, 
        margin: "20px",
    },
    sideBox:{
        width: "50%",
        backgroundColor: "#F5F5F5",
        borderRadius: 20, 
        margin: "20px",
    },
};

var jsonfile = JSON.parse(JSON.stringify(Jsonfle));

function CustmertImage(props){
    let keyitems = 0;
    const [check, setcheck] = useState(false);

    useEffect(() => {
        console.log(props.selectmenu);
        if(props.selectmenu !== '없음'){
            jsonfile[props.menuname]['ingrdent'].splice(1,0,props.selectmenu);
            setcheck(!check);
        }
    },[props.selectmenu]);

    useEffect(() => {
        if(props.selectmenu !== '없음'){
            console.log("리셋해라.");
            jsonfile = JSON.parse(JSON.stringify(Jsonfle));
        }
    },[props.check]);


    return(
       <div style={styles.wrapper}>
        <div style={styles.foodBox}>
          {
            jsonfile[props.menuname]['ingrdent'].map((comment) => {
                return (<Ingredient key={ keyitems++} name={comment}/>);
            })}
       </div>
       
       {props.togglech&&
        <div style={styles.sideBox}>
       <Ingredient3 name={Jsonfle[props.menuname]['sider']}/>
       <Ingredient3 name={Jsonfle[props.menuname]["drink"]}/>
       </div>

    }
    </div>
    );
}


export default CustmertImage;