import requests
import re
from urlextract import URLExtract



def acquireAddress():
    print("Please insert a starting address: ")
    # startingAddress = input()
    startingAddress1 = "https://freebitco.in/"
    startingAddress2 = "https://www.google.com/"
    startingAddress = "https://www.w3schools.com/"
    while (re.search("(?P<url>https?://[^\s]+)", startingAddress) == None or re.search("^https://.*$",
                                                                                       startingAddress) == None):
        print(
            "Please insert a valid address with the following structure: https://websitename.topleveldomain[/etc/etc...]")
        startingAddress = input()
    print("Valid address")
    while (startingAddress[-1] == "/"):
        print("Cleaning..")
        startingAddress = startingAddress.removesuffix("/")
    print("Cleaned address: " + startingAddress)
    return startingAddress


def webCrawler(startingAddress, visited, currentDepth, maxDepth):
    #print("Current depth: " + str(currentDepth)) # debug

    """    if (interrupted == True):
        return (visited, True)"""

    if (currentDepth > maxDepth):
        return visited

    # print("Current startingAddress: " + startingAddress) #debug
    # print("Current visited: " + str(visited)) #debug
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    try:
        r = requests.get(startingAddress, headers=headers, timeout=3)


        #print("REQUEST: " + str(r.url))  # debug: check if the request is being re-addressed somewhere else

        extractor = URLExtract()
        urls = extractor.find_urls(r.text)
        urls = list(dict.fromkeys(urls))
        #print(urls)  # debug

        matches = []  # contains urls that have more depth compared to the startingAddress

        for i in urls:
            # print("Checking if " + startingAddress + " is in " + i)
            # print("REGEX: " + regexp)  # debug
            if re.search("^https://.+$", i) != None and "mp4" not in i and "mp3" not in i:
                # print("MATCH")
                matches.append(i)

        #print("MATCHES: " + str(matches))  # debug

        for i in matches:
            if (i not in visited):
                #print("Visiting " + i) # debug

                # nextVisit = max(visited.values())+1 #REMOVED

                #print("Updating visited with: " + i + " : " + startingAddress) # debug
                visited.update({i : startingAddress})
                visited = webCrawler(i, visited, currentDepth + 1, maxDepth)
                #print("visited: " + str(visited)) # debug

        return visited
    except requests.exceptions.RequestException:
        #print("Request exception inside webCrawler, returning visited")
        return visited
    except KeyboardInterrupt: #TODO: revisit this except
        #print("KeyboardInterrupt exception inside webCrawler, returning visited")
        return visited


def main():
    startingAddress = acquireAddress()
    maxDepth = 2
    visited = webCrawler(startingAddress, {startingAddress: startingAddress}, 1, maxDepth)  # key = visited address : value = previous address that allowed to visit the current one

    print("Visited: ")
    for key, value in visited.items():
        print(key + " ")
    f = open("crawlerPath.txt", "w")
    f.write("{")
    for key, value in visited.items():
        f.write("\'" + key + "\':\'" + value + "\',")
    f.write("}")

    f.close()




main()

