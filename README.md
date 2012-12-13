### Simple multi-threaded file-based HTTP server

##### Functionality:
* multi-threaded using thread pool
* support for GET requests only
* support for static content only
* support for mime types
* support for 200, 206 and 404 HTTP response status codes
* support for single range HTTP GET requests (RFC 2616)

##### Install:

1. clone repository from github
	```
	$ git clone https://github.com/ercchy/simpleHttpServer.git simpleHttpServer
	```

2. create virtual enviroment
	```
	$ virtualenv simpleserver
	souce simpleserver/bin/activate
	```
	
3. install requirements for server
	```
	$ pip install -r requirements.txt
	```

4. run tests to check if eveything is OK
	```
	$ nosetests .
	```

#### Run:

1. run server

	```
	$ python run.py
	```

2. open latest Chrome browser
    * open url: http://localhost:5555/test_1.txt
    * open url: http://localhost:5555/test_2.html
    * open url: http://localhost:5555/test_3.html	
3. everything works?
4. copy larger mp4 video file to static_files folder
    * rename file to test_5.mp4
    * open url: http://localhost:5555/test_5.mp4
    * video should start streaming beautifully
    * move video timeline to different position
    * see how nicely simple HTTP server handles range requests

#### Possibilities:
* Command line parameters for run.py
* Add dynamic url routes and views
* Templating
* And so much more ...

