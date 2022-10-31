A ZeroMQ microservice that responds to a list of news article URLs with a JSON
containing properties as article URLs, and values as the primary image URL 
associated with the article. 

The main image for each article designated by the OpenGraph Protocol HTML meta 
tag "og:image". If the article doesn't have such a tag, the value will be None.

To run this Microservice:
First, activate the project's virtual environment. In a terminal on MacOS from 
the project's root directory, run source venv/bin/activate.

Then, run the program by entering the command python3 image_scraper.py

To request data from this microservice, connect a socket to the correct address
and port 5555. Then, send a list (array) of URL strings.

To receive data from this microservice, you will receive a JSON response from
the server as a response in the same socket for which you sent the request.