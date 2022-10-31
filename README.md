# News Image Scraper Microservice
A ZeroMQ microservice that responds to a list of news article URLs with a JSON
containing properties as article URLs, and values as the primary image URL 
associated with the article. 

The main image for each article designated by the [OpenGraph Protocol](https://ogp.me/) HTML meta 
tag "og:image". If the article doesn't have such a tag, the value will be None.

## To run this Microservice:
* Activate the project's [virtual environment] (https://docs.python.org/3/tutorial/venv.html). 
  * In a terminal on MacOS from the project's root directory, `run source venv/bin/activate`

* Then, run the program by entering the command python3 image_scraper.py

## To request data from this microservice: 
* Connect a socket to the correct address and port 5555. 
* Then, send a list (array in non-python terms) of URL strings.

## To receive data from this microservice: 
You will receive a JSON response from
the server as a response in the same socket for which you sent the request.

## Example call to the microservice:
```python
import zmq
import test_urls

context = zmq.Context()

#  Socket to talk to server
print("Connecting to image scraper server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send URL array as a byte string
print(f"Sending data …")
data = "[
         'https://www.theguardian.com/us-news/2022/oct/04/ballistics'
         '-tests-link-seven-shootings-in-california-in-possible-serial'
         '-killer-case',
         'https://www.reuters.com/world/major-un-powers-question-pacific'
         '-islanders-call-nuclear-legacy-help-2022-10-05/',
         ]"
socket.send(data.encode())

#  Get the reply.
message = socket.recv()
print(f"Received reply [ {message} ]")
```
