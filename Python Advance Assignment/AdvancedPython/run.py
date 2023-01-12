from flaskApp import create_app


# Host="0.0.0.0" tells that it is open to use in the production server

#http:localhost:5000 or http:127.0.0.1:5000 this tell the browser to where to locate the resources i.e to the local machine


create_app().run(host="0.0.0.0")