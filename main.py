from webCrawler import acquireAddress, webCrawler

if __name__ == '__main__':
    startingAddress = acquireAddress()
    maxDepth = 2

    # key = visited address
    # value = previous address that allowed to visit the current one
    visited = webCrawler(startingAddress, {startingAddress: startingAddress}, 1, maxDepth)

    print('Visited: ')
    for key, value in visited.items():
        print(key + ' ')
    f = open('crawlerPath.txt', 'w')
    f.write('{')
    for key, value in visited.items():
        f.write('\'' + key + '\':\'' + value + '\',')
    f.write('}')

    f.close()

