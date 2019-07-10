import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import errorImg from "../images/error.png"


function Error (){
    return(
        <div className="contact">
            <Header />
            <div className="error_content">
                <div className="error_box">
                    {/* <h2>Error 404</h2> */}
                    <img src ={errorImg} className="errorImg" alt="error" width="300px" height="200px"  />
                </div>
                
            </div>
            <Footer />
        </div>
    )
}

export default Error
