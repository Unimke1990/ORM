import requests
import urllib.request
# how to parse a url

# from urllib.parse import urlparse

# url = "https://intranet.alxswe.com/projects/299"
# parsedurl = urlparse(url)

# # scheme represents the protocol used
# print(parsedurl.scheme)
# print(parsedurl)

# how to parse a url and extract the port
# url = "https://intranet.alxswe.com/projects/299"
# url_parse = urlparse(url)

# print(url_parse.port)

# using urllib with APIs
# my_url = " https://dog.ceo/api/breeds/list/all"
# response = requests.get(my_url)
# print(response.content)

with urllib.request.urlopen('http://google.com') as reply:
    html = reply.read()
    print(html)