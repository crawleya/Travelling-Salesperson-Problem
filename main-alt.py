''''' 
CS 325 Project 4: Traveling Salesperson Problem
Group 13: Janel Buckingham, Alisha Crawley-Davis, Sara Sakamoto
'''''
import sys
import math

#Function to calculate distances between 2 cities
#Input: x and y coordinates of two cities (x1,y1) and (x2,y2)
#Output: Distance between the two cities rounded to nearest int
def findDistance(x1, y1, x2, y2):
  return int(round(math.sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))))

#Function to make a matrix that gives the distance between all cities
# Input: a list in the form [[city1ID, x1, y1], [city2ID, x2, y2], ...]
# Output: a matrix of the distances between any two cities
#distMatrix[1,2] returns the distance between City 1 and City 2
#Note: Do not use for large n like Example 3!!
def makeMatrix(theList):
  distMatrix = {}
  for i, (c1id,x1,y1) in enumerate(theList):
    for j, (c2id,x2,y2) in enumerate(theList):
      distMatrix[c1id,c2id] = findDistance(x1,y1,x2,y2)
  return distMatrix

#Function to calculate length of a path
#Input: a path list in the form [[city1ID, x1, y1], [city2ID, x2, y2]...]
#Output: an integer that is the length of the path
def pathLength(pathList):
  return sum(findDistance(pathList[n-1][1], pathList[n-1][2], pathList[n][1], pathList[n][2]) for n in range(len(pathList)))

#Function to check if there is a better tour
#Input: a list in the form [[city1ID, x1, y1], [city2ID, x2, y2],...]
#Output: a list in the form [[city1ID, x1, y1], [city2ID, x2, y2]...]
def twoOptimization(tl):
  for i in range(len(tl) - 1):
    for j in range(i+2, len(tl) - 1):
      a = findDistance(tl[i][1], tl[i][2], tl[i+1][1], tl[i+1][2])
      b = findDistance(tl[j][1], tl[j][2], tl[j+1][1], tl[j+1][2])
      c = findDistance(tl[i][1], tl[i][2], tl[j][1], tl[j][2])
      d = findDistance(tl[i+1][1], tl[i+1][2], tl[j+1][1], tl[j+1][2])
      if a+b > c+d:
        tl[i+1:j+1] = reversed(tl[i+1:j+1])
  return tl

#Function to calculate the tour using the nearest neighbor algorithm
#Input: a list in the form [[city1ID, x1, y1], [city2ID, x2, y2], ...]
#Output: a list in the form [length of tour, city1, city2, city3,...]
def nearestNeighbor(theList):
  #tourList will end up being the tour in the form [path length, city1, city2,...]
  tourList = []
  #unvisited is the list of cities that have not yet been visited
  unvisited = list(theList)
  #visited is the list of cities that have been visited - first city is last one in list of cities
  visited = [unvisited.pop()]
  while unvisited:
    #Find the city that is closest to the current city
    city = min(unvisited, key=lambda c: findDistance(visited[-1][1], visited[-1][2], c[1], c[2]))
    #Add the closest city to the visited list and remove from unvisited list
    visited.append(city)
    unvisited.remove(city)
  #Find the length of the tour and add that to the tourList
  newTour = twoOptimization(visited)
  tourList.append(pathLength(visited))
  #Add the list of cities to the tourList
  for i in range(len(visited)):
    tourList.append(visited[i][0])
  return tourList

#Get input and output files
if len(sys.argv) != 2:
  print("Corret usage: python main.py nameofFile.txt")
  sys.exit()

inputFile = sys.argv[1]
outputFile = inputFile.replace("txt","txt.tour")

#open input file and put city id, x-coord, and y-coord  into list
#The list named values will be in form [[city1ID, x1, y1], [city2ID, x2,y2],...]
with open(inputFile,'r') as f:
  values=[map(int,line.split()) for line in f]

#Call function to calculate the length of tour and the order of the cities visited
tourList = nearestNeighbor(values)

#open output file and write tour to it
target = open(outputFile,'w')
for item in tourList:
  target.write("%s\n" % item)

#close files
target.close()
