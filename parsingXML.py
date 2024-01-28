import urllib.request
import xml.etree.ElementTree as ET

Url= input('Enter the url')

# read the XML data from URL 

try:
    response= urllib.request.urlopen(Url)
    data= response.read()
except Exception as e:
    print('Error reading the url',e)
    quit()

tree= ET.fromstring(data)

counts= tree.findall('.//count')

comment_sum= sum(int(count.text)for count in counts)

print('Sum of comment counts', comment_sum)
