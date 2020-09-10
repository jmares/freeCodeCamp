import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pre4.org/romeo.txt')
#fhand = urllib.request.urlopen('http://www.pannix.net/index.html')

for line in fhand:
    print(line.decode().strip())
