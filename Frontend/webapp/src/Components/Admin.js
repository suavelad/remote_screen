import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import Table from "./Table"
import axios from 'axios'

// const {Storage}= require('@google-cloud/storage')
// const storage= new Storage({
//   projectId: 'media_2019',
//   keyFilename: '/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json'
// })
// const bucketName= 'media_2019'

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
    axios.post("http://localhost:8000/upload",data, {

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
                    <h2>Upload Media File</h2>
                    {/* <form action= "http://localhost:8000/upload" method="POST" enctype="multipart/form-data"> */}
                  
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