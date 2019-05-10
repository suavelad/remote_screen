
// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// Creates a client
const storage= new Storage({
  projectId: 'media_2019',
  keyFilename: '/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json'
})

const bucketName = 'media_2019'
const fileName = '../images/logo.png'

// Uploads a local file to the bucket
async function Upload(fileName){
    await storage.bucket(bucketName).upload(fileName, {
        // Support for HTTP requests made with `Accept-Encoding: gzip`
        gzip: true,
        // By setting the option `destination`, you can change the name of the
        // object you are uploading to a bucket.
        metadata: {
          // Enable long-lived HTTP caching headers
          // Use only if the contents of the file will never change
          // (If the contents will change, use cacheControl: 'no-cache')
          cacheControl: 'public, max-age=31536000',
        },
      });
      
      console.log(`${fileName} uploaded to ${bucketName}.`);
}
Upload(fileName)
// export default Upload