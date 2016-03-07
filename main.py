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

#Function to calculate the tour
#Input: a list in the form [[city1ID, x1, y1], [city2ID, x2, y2], ...]
#Output: a list in the form [length of tour, city1, city2, city3,...]
def calculateTour(theList):
  tourList = [3,5,6,7] #Placeholder
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
tourList = calculateTour(values)

#open output file and write tour to it
target = open(outputFile,'w')
for item in tourList:
  target.write("%s\n" % item)

#close files
target.close()
