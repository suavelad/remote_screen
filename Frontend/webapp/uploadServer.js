var express= require('express')
var app = express()
var multer =require('multer')
var cors = require('cors')
app.use(cors())
var port=8000


// Google Cloud Platform
// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// Creates a client
const storages= new Storage({
  projectId: 'media_2019',
  keyFilename: '/home/s/Documents/Projects/Remote_Screen/Media-606208d3d348.json'
})

const bucketName = 'media_2019'



var storage = multer.diskStorage({
    destination:function(req,file,cb){
        cb(null,'public/uploads')
    },
    filename:function(req,file,cb){
        cb(null,file.originalname )
        // console.log(name)
    }
})

var upload = multer({storage: storage}).single('file')

app.post('/upload',function(req,res){

    upload(req,res, function(err){

        if (err instanceof multer.MulterError){
            return res.state(500).json(err)
        } else if (err){
            return res.status(500).json(err)
        }
        var fileName = req.file.path
        console.log(req.file.mimetype)
        // async function Upload(fileName){
            storages.bucket(bucketName).upload(fileName, {
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


        // }

    return res.status(200).send(req.file)
          



    })
})


app.listen(port, function(){
    console.log('App running on port ' + port)
})