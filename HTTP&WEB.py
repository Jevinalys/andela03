import urllib
import json

#ajax.googleapis.com/ajax/services/search/web?v=1.0&q=
exampleSearch = 'python'
encoded = urllib.quote(exampleSearch)

rawData = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+encoded).read()

jsonData = json.loads(rawData)
searchResults = jsonData['responseData']

title =  searchResults
print title
print '''
 

            '''
