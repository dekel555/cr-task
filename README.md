# cr-task



## instructions

run 'sudo ./run.sh' from the root directory.  
the web page with the manipulated data will be available through 'http://localhost' in your browser.


## requirements

 * Docker Engine
 * Docker-Compose
 * python3
 * pandas library
 * json library


## general description  
   
   First, 'DataToJson' converts the data.txt file to a Json file for the mongodb container.  
     
   Then docker-compose creates a docker image with nginx and mongodb containers.  
   note that we are using volumes in the docker-compose for both containers:  
   * the nginx index.html file is mounted to a local custom html file that we can edit later.
   * the json file we created at the first step is now mounted to the mongo container.   
     
   Next, we run Bash commands in the mongo container to create the collection and to export it.  
   and finally app.py manipulates the data we exported from the mongo container and adds it to our index.html file using pandas dataframes,
