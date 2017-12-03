import urllib.request
import urllib.parse

url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

if __name__ == '__main__':
    print(resp_data)
