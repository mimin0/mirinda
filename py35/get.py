import urllib.request
import json

#url = "https://teamcity.jetbrains.com/guestAuth/app/rest/agents"
url = 'http://www.reddit.com/r/all/top/.json'
#headers = {'Media-Type':'application/json'}
req = urllib.request.Request(url)
#req.add_header('Accept','application/json')

r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0
for item in cont['data']['children']:
    counter += 1
    print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
    print("----")

#print (json.dumps(cont, indent=4, sort_keys=True))

#print("\n ---------------------- \n")
print("Number of titles: ", counter)