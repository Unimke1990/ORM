import urllib.error
import requests
import urllib.request
import shutil
import tempfile
import urllib.parse
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

# more request examples
# with urllib.request.urlopen('http://google.com') as reply:
#     html = reply.read()
#     print(html)

# making an explicit request which will allow for headers to be added
# req = urllib.request.Request('https://google.com/')
# with urllib.request.urlopen(req) as reply:
#     with tempfile.NamedTemporaryFile(delete=False) as file:
#         shutil.copyfileobj(reply, file)
#         file.seek(0)
#         files = file.read()
#         print(files)

    # response = reply.read()
    # print(response)


# How to download a resource from URL and storing in a temp file
# with urllib.request.urlopen('https://google.com/') as response:
#     with tempfile.NamedTemporaryFile(delete=False) as tem_file:
#         shutil.copyfileobj(response, tem_file)
#         tem_file.seek(0)
#         reply = tem_file.read()
#         print(reply)

# making posts with data - data needs encoding
# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# values = {
#     'name': 'Given',
#     'age': 34,
#     'gender': 'make'
# }

# data = urllib.parse.urlencode(values)
# data = data.encode('ascii')
# req = urllib.request.Request(url, data, method='POST')
# with urllib.request.urlopen(req) as response:
#     if response.status == 200:
#         file = response.read()
#     else:
#         print(f"Error: {response.status}")


# making get requests with additional data
# values = {
#     'name': 'Given',
#     'age': 34,
#     'gender': 'make'
# }
# data = urllib.parse.urlencode(values)
# print(data)
# url = 'https://google.com'
# data_url = url + '?' + data
# print(data_url)
# response = urllib.request.urlopen(data_url)
# print(response.read())

# How to add a user-agent to a POST request
# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
# values = {'name': 'Michael Foord',
#           'location': 'Northampton',
#           'language': 'Python' }
# headers = {'User-Agent': user_agent}

# data = urllib.parse.urlencode(values)
# data = data.encode('ascii')
# req = urllib.request.Request(url, data, headers)
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()

# Handling URLError
url = 'http://tryme_pretend.o'
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        print(response.read())
except urllib.error.URLError as e:
    print(e.reason)