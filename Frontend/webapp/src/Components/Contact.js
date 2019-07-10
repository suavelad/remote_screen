import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import addr from "../images/addr.png"
import email from "../images/email.png"
import phone from "../images/phone.png"



function Contact (){
    return(
        <div className="contact">
            <Header />
            <div className="contact_content">
                <div className="main_contact">
                    <h3>
                        <img src={addr} className="contact_addr" width="40" height="40"  alt="address"/> {" "} No.5 Johnson street, V.I, Lagos
                    </h3>

                    <h3>
                        <img src={email} className="contact_email" width="35" height="30"  alt="email"/> info@remotescreen.com.ng
                    </h3>

                    <h3>
                    <img src={phone} className="contact_phone" width="28" height="30" alt="phone"/> (+234) 806-771-5394
                    </h3>
                </div>
                    
            </div>
            <Footer />
        </div>
    )
}

export default Contact