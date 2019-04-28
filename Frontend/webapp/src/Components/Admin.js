import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import Table from "./Table"
import axios from 'axios'

const {join}= require('path')
const {client}= require ('google-cloud-bucket')
const storage = client.new ({
  jsonKeyFile: join(__dirname, '.../Media-606208d3d348.json')
}) 

class Admin extends React.Component{
  
  state = {
    selectedFile: null
  }
    fileSelectedHandler = event => {
      this.setState({
            selectedFile:event.target.files[0]
      })

}

    fileUploadHandler= ()=> {
      const fd = new FormData();
      fd.append('image',this.state.selectedFile,this.state.selectedFile.name);
      axios.post("");

    }
    render(){
      return (
        <div>
          <Header />
          <div className="admin_content"> 
              {/* <div className="uploads"> */}
              <table  className="uploads">
                <tr>
                  <h2>Upload Media File</h2>
                </tr>

                <tr>
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
                  <input type= "file" name="file" className="file_upload" onChange={this.fileSelectedHandler} />
                  </tr>
                  <tr>
                    <button className="upload_button" onClick={this.fileUploadHandler}>Upload</button>
                  </tr>
                </table>

              {/* </div> */}
            <hr />
            {/* <div className="admin_table"> */}
            <Table />
            {/* </div> */}
          </div>
          <Footer />
    
        </div>
      )
    }
  }


export default Admin