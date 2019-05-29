import React from 'react'


// // Google Cloud Platform
// // Imports the Google Cloud client library
// const {Storage} = require('@google-cloud/storage');

// // Creates a client
// const storages= new Storage({
//   projectId: 'media_2019',
//   keyFilename: '/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json'
// })

// const bucketName = 'media_2019'

// // Lists files in the bucket
// const [files] =  storages.bucket(bucketName).getFiles();

// console.log('Files:');
// files.forEach(file => {
//   console.log(file.name);
// });

const Table = () => {
  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Size</th>
          <th>Type</th>
          <th>Upload Date</th>
          <th>Edit</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          
          {/* <td>{file.name}</td>
          <td>{(file.metadata.size/1024).toFixed(2)} MB</td> */}
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
  );

}

export default Table