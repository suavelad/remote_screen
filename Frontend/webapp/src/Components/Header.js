import React from "react"
import logo from "../images/logo.png"
import {Link} from "react-router-dom"

function Header(){
    return (
        <header className= "header">
        
          <Link to= "/">
                <img src= {logo} alt="logo" className="logo"/>
            </Link>
            
            <div className="nav">
                <Link to="/">HOME</Link> 
                <Link to= "/about">ABOUT</Link>
                <Link to= "/contact">CONTACT</Link>
                <Link to= "/admin">ADMIN</Link>
            </div>
          
        </header>
    )

}

export default Header
