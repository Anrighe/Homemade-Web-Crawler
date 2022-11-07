import requests
import re
from urlextract import URLExtract


def acquireAddress():
    print("Please insert a starting address: ")
    #startingAddress = input()
    startingAddress1 = "https://freebitco.in/"
    startingAddress2 = "https://www.google.com/"
    startingAddress = "https://www.w3schools.com/"
    while(re.search("(?P<url>https?://[^\s]+)", startingAddress) == None or re.search("^https://.*$", startingAddress) == None):
        print("Please insert a valid address with the following structure: https://websitename.topleveldomain[/etc/etc...]")
        startingAddress = input()
    print("Valid address")
    while (startingAddress[-1] == "/"):
        print("Cleaning..")
        startingAddress = startingAddress.removesuffix("/")
    return startingAddress


def webCrawler(startingAddress, visited, currentDepth, maxDepth):
    print("Current depth: " + str(currentDepth))
    if (currentDepth > maxDepth):
        return visited

    #print("Current startingAddress: " + startingAddress) #debug
    #print("Current visited: " + str(visited)) #debug
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        r = requests.get(startingAddress, headers=headers, timeout=3)
    except requests.exceptions.RequestException as e:
        return visited

    print("REQUEST: " + str(r.url)) #debug: check if the request is being re-addressed somewhere else

    extractor = URLExtract()
    urls = extractor.find_urls(r.text)
    urls = list(dict.fromkeys(urls))

    print(urls)

    matches = [] #contains urls that have more depth compared to the startingAddress

    for i in urls:
        #print("Checking if " + startingAddress + " is in " + i)
        #print("REGEX: " + regexp)
        if re.search("^https://.+$", i) != None and "mp4" not in i and "mp3" not in i:
            #print("MATCH")
            matches.append(i)

    print("MATCHES: " + str(matches)) #debug

    for i in matches:
        if (i not in visited):
            print("Visiting " + i)

            #print("VALUESSSSS: " + str(visited.values()))
            #nextVisit = max(visited.values())+1

            visited.update({i:startingAddress})
            visited = webCrawler(i, visited, currentDepth+1, maxDepth)
            print("visited: " + str(visited))

    return visited



startingAddress = acquireAddress()
maxDepth = 3
visited = webCrawler(startingAddress, {startingAddress:startingAddress}, 1, maxDepth) #key = visited address : value = previous address that allowed to visited the current

print("Visited: ")
for key, value in visited.items():
    print(key + " ")












