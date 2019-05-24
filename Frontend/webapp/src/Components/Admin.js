import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import Table from "./Table"

import axios from 'axios'

// const axios = require("axios")


// import Upload from "./Upload"
// import axios from 'axios'

// const {Storage}= require('@google-cloud/storage')
// const fs= require('fs')
// const storage= new Storage({
//   projectId: 'media_2019',
//   keyFilename: '/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json'
// })
// const bucketName= 'media_2019'

// const storage = new Storage()



class Admin extends React.Component{

  onChangeHandler=event=>{
    this.setState({
      selectedFile:event.target.files[0],
      loaded:0,
    })
    // console.log(event.target.files[0])
  }

  onClickHandler=()=> {
    const data = new FormData()
    data.append('file',this.state.selectedFile)
    axios.post("http://localhost:8007/upload",data, {

    })
    .then(res=>{
      console.log(res.statusText)
    })
  }
    render(){
      
      
      return (
        <div>
          <Header />
          <div className="admin_content"> 
              <div className="uploads">
                    <h1>Upload Media File</h1>
                    {/* <form action= "/admin" method="POST" enctype="multipart/form-data"> */}
                      <h3> Category:    
                      <label>
                        <input 
                          type="radio" 
                          name="category" 
                          value="video" 
                          className="category"
                          />
                          Video
                      
                      </label>

                      <label>
                        <input 
                          type="radio" 
                          name="category" 
                          value= "image"  
                          className="category"
                          />
                          Image
                      </label>
                      </h3>
                      {/* <input type= "file" name="uploadFile" className="file_upload" onChange={this.onChange} /> */}
                      <input type= "file" name="uploadFile" onChange={this.onChangeHandler} className="file_upload"  />
                      <div className="uploadButton">
                      <button type = "submit" className="upload_button" onClick={this.onClickHandler}>Upload </button>
                      </div>
                  {/* </form> */}
              </div>
            <hr />
            <Table />
          </div>
          <Footer />
    
        </div>
      )
    }
  }


export default Admin