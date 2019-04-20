# Project Title
Remote Billboard Screen Manager
# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Backend 


## Prerequisites

This system requires the knowledge of the following:
- Google Cloud Storage Platform
     
- Linux Operating system
- Python3 (latest version is preferred)
- Pip3: PIP is a package manager for Python packages. I recommend you install python3 version of pip.

- Virtual Environment
- MQTT - Messaging Queuing Telemetry Transport
- Mosquitto(Broker and Client)



## Installing

A step by step series of examples that tell you how to get a development env running

#Setting up the Main.py
* Setup a Virtual Environment
Step 1: Install pip 
    To install: sudo apt install python3-pip

Step 2: Install the Virtual Environment
    To install: "sudo pip install virtualenv" 

Step 3: Create a virtual environment
    "virtualenv Remotescreen" or "virtualenv -p python3 Remotescreen"

Step 4: Activate the virtual environment
    - "cd" - to go back to the home directory. if your virtual environment was install on the    home directory.
    - "source flaskBlog/bin/activate"

** To deactivate the virtual environment, use "deactivate" 

* Setup Up the Google Cloud Platform 
    1. Install Google Cloud SDK: https://cloud.google.com/sdk/docs/

    2. Download the latest version compatible with your OS

    3. Extract the download file (tar -xzvf  filename.tar.gz)

    4. Open your terminal, go to : $ ./google-cloud-sdk/install.sh

    5. Run gcloud init to initialize the SDK:$ ./google-cloud-sdk/bin/gcloud init

    6. while in the virtual environment install gsutil python package: 
        "pip install gsutil"

    7. Follow the steps to authenticate with your google account (if it does not ask you to authenticate,  use : "gsutil -config"     on the terminal while in the virtual environment

    8. Then you are ready to work 



#Setting up the MQTT Broker Server

* Install mosquitto
- sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
- sudo apt-get update
- sudo apt-get install mosquitto 
- sudo apt-get mosquitto-clients : if you also want to use the broker server as a client also

* Install paho-mqtt-python 
- first create a virtual Environment 
- pip install paho-mqtt

#Setting up the Raspberry Device
* Setup up GCP
    - pip install google-cloud-storage
    - In the GCP Console, go to the "Create service account key page".
      * GO TO THE CREATE SERVICE ACCOUNT KEY PAGE
      * From the Service account list, select New service account.
      * In the Service account name field, enter a name.
      * From the Role list, select Project > Owner
      * Click Create. A JSON file that contains your key downloads to your computer [PATH] of your choice
      * On your shell terminal, type : export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
        (Example: export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json") 


* Setup up the MQTT Consumer 

> Install mosquitto-client
   - sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
   - sudo apt-get update
   - sudo apt install mosquitto-clients

> Install paho-mqtt-python 
   - first create a virtual Environment 
   - pip install paho-mqtt
> Create a folder called "Content" into the "Backend" folder

### Frontend

## Prerequisites
- Install node packages: npm, React.js
   > node version: 
   > react version:

## Deployment

Add additional notes about how to deploy this on a live system

- While deploying it live, it is important to get a ssl certificate (such as: certbot ssl)
   Sample: https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04

## Built With

* [Mosquitto ](https://mosquitto.org/man/mosquitto-8.html/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Sunday Ajayi** - *Initial work* - [PurpleBooth](https://github.com/suavelad)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 
* 
* 
