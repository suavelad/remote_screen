import React from "react"
import Header from "./Header"
import Footer from "./Footer"


function Error (){
    return(
        <div className="contact">
            <Header />
            <div className="error_content">
                <div className="error_box">
                    <h2>Error 404</h2>
                </div>
                
            </div>
            <Footer />
        </div>
    )
}

export default Error
