# Author: Nick Zombor
# Date: 11/07/22
# Description: CS 361 Microservice to be used by Raymond Randall.
# Receives a URL for a news article webpage and returns the image at the top of
# that webpage.
# Citations:
# Python Web Scraper Tutorial -
# https://www.makeuseof.com/python-scrape-web-images-how-to/
# Beautiful Soup Documentation -
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# The Open Graph Protocol Documentation - https://ogp.me/

import requests
import time
import zmq
import json
from bs4 import BeautifulSoup

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Image Scraper Microservice listening on Port 5555...")

while True:
    #  Wait for next request from client
    raw_data = socket.recv()
    start_time = time.time()
    print(f"Received data: {type(raw_data)}")

    # Validate user input
    try:
        # decode byte string into a JSON string, then parse string into a list
        urls_list = json.loads(raw_data.decode())
    except TypeError as err:
        print("Type Error:", err)
        socket.send(b"Error: could not convert data to a Python List.")
        raise
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        socket.send(b"Unexpected error.")
        raise

    urls_dict = dict()  # populate with url : image url
    images_found = 0
    for url in urls_list:
        print(f"Searching for image at url: {url}")

        try:
            getURL = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        except Exception as err:
            print(f"Error retrieving image {err=}. {type(err)}")
            image_url = None
        else:
            soup = BeautifulSoup(getURL.text, 'html.parser')
            # find the first image with og:image tag, else returns None
            findImageTag = soup.find('meta', property="og:image")
            if findImageTag:
                image_url = findImageTag.get('content')
                images_found += 1
            else:
                image_url = None

        # Add image url to dictionary if found, else add None
        urls_dict[url] = image_url

    end_time = time.time()
    print(f"Parsed {len(urls_list)} news articles, found {images_found} "
          f"images in {round(end_time - start_time, 1)} seconds.")

    #  Send response to client
    resp = json.dumps(urls_dict)
    socket.send(resp.encode())

