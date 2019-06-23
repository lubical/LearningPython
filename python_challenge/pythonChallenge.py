#http://www.pythonchallenge.com/pc/return/romance.html
import urllib.request, urllib.error, urllib.parse
from urllib.parse import quote_plus, unquote_plus
from urllib import request,response,parse
import http.cookiejar
import re
print("Staring to follow the busynothing chain, but also picking up the crumbs!")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPHandler())
def getPage(nothing="12345"):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
	req = urllib.request.Request(url+nothing)
	response = opener.open(req)
	return response.read().decode()

pat = re.compile(r"(.*?)and the next busynothing is (\d*)$")
num = 12345
cookievals = []
count = 0
while True:
	count += 1
	m = pat.match(getPage(str(num)))
	for cookie in cj:
		cookievals.append(cookie.value)
	if m == None:
		break
	elif count > 400:
		print("400 times is more than enough")
		break
	else:
		print(str(count) + ": " + m.group(0))
		num = int(m.group(2))
print("Done retrieving cookies")
print()
print("Decompressing the message")
import bz2
ans = "".join(cookievals)
message = bz2.decompress(parse.unquote_to_bytes(ans.replace('+', '%20'))).decode('ascii')
print("The message is: %s" % message)
print()
print("Mozart was born to Leopold...")
print("Looking up Leopold")
##Call his father Leopold
import xmlrpc.client
x= xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
number = x.phone("Leopold")
print("Leopold's number is: %s" % number) 
print()
print("Calling Leopold and sending him the mssage")
o = urllib.request.build_opener()
message = "the flowers are on their way"
o.addheaders.append(('Cookie', 'info='+quote_plus(message)))
res = o.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print("Message sent!")
print()
print("His response is...")
print(res.read())