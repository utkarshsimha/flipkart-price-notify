import urllib2
import re
import pynotify
import sys
num_a = 0
r = open("flipkart_price_data.txt","r")
lst = r.readlines()
if(len(lst)!=0):
	a = lst[len(lst)-1]
	num_a = int(re.sub(',','',a))
r.close()
print "Enter URL. Press Ctrl+D to end"
url = sys.stdin.read()
response = urllib2.urlopen(url)
web_page = response.read()
pattern = ";value=[\d\,]+"
m = re.search(pattern, web_page)
text = m.group(0)
if(text == None):
	print "Error"
	exit()
pattern = '[0-9]+\,?\.?[0-9]*'
amount = re.search(pattern, text)
if(amount == None):
	print "Error"
	exit()
amt = amount.group(0)
num_amt = int(re.sub(',','',amt))
if(num_amt < num_a):
	if not pynotify.init("summary-body"):
		exit()
	n = pynotify.Notification("Flipkart Price notifier","Price has dropped")
	n.show()
g = open("flipkart_price_data.txt","a")
g.write(amt+"\n")
g.close()
exit()
