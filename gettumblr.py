import json, requests, io, sys

outputf = io.open('pukicho.json', mode = 'a',  encoding="utf-8") #the output file
r = requests.get('https://api.tumblr.com/v2/blog/pukicho.tumblr.com/posts?api_key=SaLAoKzhrDeg9F9HNE2vqn2O0qCnjWxetdWbXlPrPNYPHj648b&limit=50')
whole_file = r.json()
bodylist = []
bodylist.extend([body["body"] for body in r.json()["response"]["posts"] if body["type"] == "text"])
totalposts = whole_file["response"]["total_posts"]
#print(totalposts)
counter = 50
#outputf.write("[")
for i in range(totalposts//50 - 1):
    r = requests.get('https://api.tumblr.com/v2/blog/pukicho.tumblr.com/posts?api_key=SaLAoKzhrDeg9F9HNE2vqn2O0qCnjWxetdWbXlPrPNYPHj648b&limit=50&offset=' + str(counter))
    counter += 50
    temp = r.json()
    bodylist.extend([body["body"] for body in r.json()["response"]["posts"] if body["type"] == "text"])
wholejson = json.dumps(bodylist)
outputf.write(wholejson)    
#outputf.write("]")
outputf.close()