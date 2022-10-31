# News Image Scraper Microservice
A ZeroMQ microservice that receives a list of news article and responds with a JSON
containing all of the news articles as properties, and the values as the primary image URL 
associated with the article. 

The microservice searches for the main image in each article designated by the [OpenGraph Protocol](https://ogp.me/) HTML meta 
tag "og:image". If the article doesn't have such a tag, the value will be None.

## To run this Microservice:
* It's recommended to install the package dependencies in a [virtual environment](https://docs.python.org/3/tutorial/venv.html).
* Activate the project's virtual environment. 
  * In a terminal on MacOS from the project's root directory, run `source venv/bin/activate`
  * Install dependencies: `pip install -r /path/to/requirements.txt`

* Then, run the program by entering the command `python3 image_scraper.py`

## To request data from this microservice: 
* Connect a socket to the correct address and port 5555. 
* Then, send an array of URL strings.

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
         'https://www.ctvnews.ca/business/canadian-businesses-can-charge'
         '-credit-card-fees-starting-oct-6-1.6096370',
         'https://www.reuters.com/world/major-un-powers-question-pacific'
         '-islanders-call-nuclear-legacy-help-2022-10-05/',
         ]"
socket.send(data.encode())

#  Get the reply.
message = socket.recv()
print(f"Received reply [ {message} ]")
```
## Unified Modeling Language (UML) Sequence Diagram
![News Image Scraper Microservice](https://user-images.githubusercontent.com/91298281/199120513-8bac2745-6712-43aa-a8f4-0cb98d5f003e.jpeg)

