### Simple multi-threaded file-based HTTP server

Functionality:

* multi-threaded using thread pool
* support for GET requests only
* support for static content only
* support for mime types
* support for 200, 206 and 404 HTTP response status codes
* support for single range HTTP GET requests (RFC 2616)

Install:

1. clone repository
2. create virtual enviroment
3. pip install -r requirements.txt
4. nosetests

Run:

1. python run.py
2. open latest Chrome browser
   ** open url: http://localhost:5555/test_1.txt
   ** open url: http://localhost:5555/test_2.html
   ** open url: http://localhost:5555/test_3.html
3. everything works?
4. copy larger mp4 video file to static_files folder
   ** rename file to test_5.mp4
   ** open url: http://localhost:5555/test_5.mp4
   ** video should start streaming beautifully
   ** move video timeline to different position
   ** see how nicely simple HTTP server handles range requests

