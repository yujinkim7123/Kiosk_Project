import React from 'react';
import CommentList from './CommentList';
import Sidebar from './sidebarlist'
import Menu from './Menulist'
import CustmerList from './CustmerList';
import Header from './Header'
import CutmerEasyMode from './CutmerEasyMode';

const styles = {
    wrapper:{
        margin: 0,
        padding: 0,
        display: "flex",
        flexDirection:"row",
        border: "1px solid grey",
        borderRadius: 0,
    },
  };
  
function CommonMode() {
    return (
      <div>
       <Header/>
       <CutmerEasyMode/>
       <div style={styles.wrapper}>
        <Sidebar/>
        <Menu/>
      </div>
      <CommentList/> 
      </div>
  
    );
  }
  
  export default CommonMode;