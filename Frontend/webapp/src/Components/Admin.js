import React from "react"
import Header from "./Header"
import Footer from "./Footer"
import Table from "./Table"
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
      try {
        if (this.state.selectedFile.__dirname ==="null"){
          alert('No file inserted')
        }
        else{
          
          fd.append('image',this.state.selectedFile,this.state.selectedFile.__dirname)
          console.log("the selected file is : ",this.state.selectedFile.__dirname)
          // Upload(this.state.selectedFile.name)
        // axios.post("https://www.googleapis.com/upload/storage/v1/b/media_2019/o?uploadType=media&name="+ this.state.selectedFile.name)
        // .then ( res=> {
        //   console.log(res)
        // });
      }
      }
      catch(e){
        console.log('error', e)
      }
 

    }



    
    render(){
      
      
      return (
        <div>
          <Header />
          <div className="admin_content"> 
              <div className="uploads">
                    <h2>Upload Media File</h2>

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
                    <div className="uploadButton">
                      <button className="upload_button" onClick={this.fileUploadHandler}>Upload</button>
                    </div>
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