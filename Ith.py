#Script to auto-generate dungeons for Dungeons and Dragons and similar systems
#Written for Python 3 by Rimgon, 2019

from random import randint
import time 

#Pieces of ascii drawings, for copy+pasting: ║ ═ ╗ ╔ ╝ ╚ ╣ ╬ ╠ ╦ ╩  

'''
ewHall

╔═════════╗
╚            ╝
╔            ╗
╚═════════╝


nwHall
  ╔═╝ ╚═╗ 
  ║     ║ 
  ║     ║ 
  ║     ║ 
  ║     ║ 
  ╚═╗ ╔═╝ 

neHall
 ╔═╝ ╚═╗   
 ║     ╚═╗ 
 ║          ╚ 
 ║          ╔ 
 ╚═══════╝ 


nRoom
╔═══╝ ╚═══╗
║            ║
║            ║
║            ║
║            ║
╚═════════╝

("╔═══╝ ╚═══╗","║\t  ║","║\t  ║","║\t  ║","║\t  ║","╚═════════╝")

sRoom
╔═════════╗
║            ║
║            ║
║            ║
║            ║
╚═══╗ ╔═══╝

("╔═════════╗","║\t  ║","║\t  ║","║\t  ║","║\t  ║","╚═══╗ ╔═══╝")

eRoom
╔═════════╗
║            ║
║            ╚
║            ╔
║            ║
╚═════════╝

("╔═════════╗","║\t  ║","║\t  ╚","║\t  ╔","║\t  ║","╚═════════╝")

wRoom
╔═════════╗
║            ║
╝            ║
╗            ║
║            ║
╚═════════╝

("╔═════════╗","║\t  ║","║\t  ║","╗\t  ╔","║\t  ║","╚═════════╝")

neRoom
╔═══╝ ╚═══╗
║            ║
║            ╚
║            ╔
║            ║
╚═════════╝

("╔═══╝ ╚═══╗","║\t  ║","║\t  ╚","║\t  ╔","║\t  ║","╚═════════╝")

nwRoom
╔═══╝ ╚═══╗
║            ║
╝            ║
╗            ║
║            ║
╚═════════╝

("╔═══╝ ╚═══╗","║\t  ║","╝\t  ║","╗\t  ║","║\t  ║","╚═════════╝")

seRoom
╔═════════╗
║            ║
║            ╚
║            ╔
║            ║
╚═══╗ ╔═══╝

("╔═════════╗","║\t  ║","║\t  ╚","║\t  ╔","║\t  ║","╚═══╗ ╔═══╝")

swRoom
╔═════════╗
║            ║
╝            ║
╗            ║
║            ║
╚═══╗ ╔═══╝

("╔═════════╗","║\t  ║","╝\t  ║","╗\t  ║","║\t  ║","╚═══╗ ╔═══╝")

nseRoom
╔═══╝ ╚═══╗
║            ║
║            ╚
║            ╔
║            ║
╚═══╗ ╔═══╝

("╔═══╝ ╚═══╗","║\t  ║","║\t  ╚","║\t  ╔","║\t  ║","╚═══╗ ╔═══╝")

nswRoom
╔═══╝ ╚═══╗
║            ║
╝            ║
╗            ║
║            ║
╚═══╗ ╔═══╝

("╔═══╝ ╚═══╗","║\t  ║","╝\t  ║","╗\t  ║","║\t  ║","╚═══╗ ╔═══╝")

newRoom
╔═══╝ ╚═══╗
║            ║
╝            ╚
╗            ╔
║            ║
╚═════════╝

("╔═══╝ ╚═══╗","║\t  ║","╝\t  ╚","╗\t  ╔","║\t  ║","╚═════════╝")

sewRoom
╔═════════╗
║            ║
╝            ╚
╗            ╔
║            ║
╚═══╗ ╔═══╝

("╔═════════╗","║\t  ║","╝\t  ╚","╗\t  ╔","║\t  ║","╚═══╗ ╔═══╝")

nsweRoom
╔═══╝ ╚═══╗
║            ║
╝            ╚
╗            ╔
║            ║
╚═══╗ ╔═══╝

("╔═══╝ ╚═══╗","║\t  ║","╝\t  ╚","╗\t  ╔","║\t  ║","╚═══╗ ╔═══╝")
'''


MAXNODES = 10


nsHall = ("nsHall", (0,-1,'n'),(0,1,'s'))

ewHall = ("ewHall", (-1,0,'e'),(1,0,'w'))


nRoom = (("╔═══╝ ╚═══╗","║         ║","║         ║","║         ║","║         ║","╚═════════╝"),(0,1,'s'))

sRoom = (("╔═════════╗","║         ║","║         ║","║         ║","║         ║","╚═══╗ ╔═══╝"),(0,-1,'n'))

eRoom = (("╔═════════╗","║         ║","║         ╚","║         ╔","║         ║","╚═════════╝"),(1,0,'w'))

wRoom = (("╔═════════╗","║         ║","╝         ║","╗         ║","║         ║","╚═════════╝"),(-1,0,'e'))


neRoom = (("╔═══╝ ╚═══╗","║         ║","║         ╚","║         ╔","║         ║","╚═════════╝"), (1,0,'w'),(0,1,'s'))

nwRoom = (("╔═══╝ ╚═══╗","║         ║","╝         ║","╗         ║","║         ║","╚═════════╝"), (-1,0,'e'),(0,1,'s'))

seRoom = (("╔═════════╗","║         ║","║         ╚","║         ╔","║         ║","╚═══╗ ╔═══╝"), (1,0,'w'),(0,-1,'n'))

swRoom = (("╔═════════╗","║         ║","╝         ║","╗         ║","║         ║","╚═══╗ ╔═══╝"), (-1,0,'e'), (0,-1,'n'))


nseRoom = (("╔═══╝ ╚═══╗","║         ║","║         ╚","║         ╔","║         ║","╚═══╗ ╔═══╝"), (1,0,'w'),(0,1,'s'),(0,-1,'n'))

nswRoom = (("╔═══╝ ╚═══╗","║         ║","╝         ║","╗         ║","║         ║","╚═══╗ ╔═══╝"), (-1,0,'e'),(0,1,'s'),(0,-1,'n'))

newRoom = (("╔═══╝ ╚═══╗","║         ║","╝         ╚","╗         ╔","║         ║","╚═════════╝"), (1,0,'w'),(0,1,'s'),(-1,0,'e'))

sweRoom = (("╔═════════╗","║         ║","╝         ╚","╗         ╔","║         ║","╚═══╗ ╔═══╝"), (-1,0,'e'), (1,0,'w'), (0,-1,'n'))

nsweRoom = (("╔═══╝ ╚═══╗","║         ║","╝         ╚","╗         ╔","║         ║","╚═══╗ ╔═══╝"), (-1,0,'e'), (1,0,'w'), (0,1,'s'), (0,-1,'n'))


#Arrays of rooms by where they open towards, I.E. any rooms in northOpenings can connect to a room to the north
northOpenings = (sRoom, seRoom, swRoom, nseRoom, nswRoom, sweRoom, nsweRoom)		#nsHall, 

southOpenings = (nRoom, neRoom, nwRoom, nseRoom, nswRoom, newRoom, nsweRoom)		#nsHall, 

eastOpenings = (wRoom, nwRoom, swRoom, nswRoom, newRoom, sweRoom, nsweRoom)			#ewHall,  

westOpenings = (eRoom, neRoom, seRoom, nseRoom, newRoom, sweRoom, nsweRoom)			#ewHall, 





def renderMap(tiles):
	#Start by sorting by Y value
	tiles = sorted(tiles, key=lambda x: x[1], reverse=True)
	tilesByRows = [[]]

	#Sort the 1D array of tiles into a 2D array, where each sublist is a row
	i = 0
	rowNum = tiles[1]
	lastNum = tiles[0][1]
	for tile in tiles:
		rowNum = tile[1]
		if(rowNum==lastNum):
			tilesByRows[i].append(tile)
		else:
			tilesByRows.append([])
			i+=1
			lastNum = tile[1]
			tilesByRows[i].append(tile)

	minX = 0
	sortedTiles = []
	#Sort each row in ascending order
	for row in tilesByRows:
		sortedTiles.append(sorted(row, key=lambda x: x[0], reverse=False))

		#find the smallest x value
		if(sortedTiles[len(sortedTiles)-1][0][0]<minX):
			minX = sortedTiles[len(sortedTiles)-1][0][0]

	#print out each line, ordered by X pos. If there's a missing X pos, then fill it with whitespace. Go for 6 lines, then move to the next Y value.
	currXPos = minX
	for row in sortedTiles:
		for i in range(0,6):
			for square in row:
				#fill in empty tiles with whitespace
				while(currXPos<square[0]):
					print("           ", end='')
					currXPos+=1
				#Print out the current row of the tile we're on
				print(square[2][0][i], end='')
				currXPos+=1
			currXPos = minX
			print("")

	#for item in sortedTiles:
	#	print(item)




def printTileset(tileset):			#Debug method, not for production use
	for tile in tileset:
		print(str(tile[0]) + "\t" + str(tile[1]) + "\t" + str(tile[2][0]))


#maintain an array of nodes that need to be populated
#For each node, track its x-y position, as well as the direction it was created from
#place a tile in the first spot in the node array that satisfies the required direction of approach
#add the new nodes this tile has created to the end of the array, then rinse and repeat

#nodes are structured as (x,y,openingDirection)
nodes = [(0,1,'s'),(1,0,'w'),(0,-1,'n'),(-1,0,'e')]				#seed nodes to make sure the dungeon has enough chances to grow

tileset = [[0,0,nsweRoom]]

populatedLocations = [(0,0)]

startTime = time.time()		#Timeout to avoid making dungeons too big in testing

while(len(nodes)!=0 and len(populatedLocations)<MAXNODES):			#time.time()-startTime<0.00001
#if(True):
	#set the location of the new tile
	x = nodes[0][0]
	y = nodes[0][1]
	if((x,y) in populatedLocations):		#Don't overwrite existing nodes. If we get overlap, remove the node from the list and skip it
		nodes.pop(0)
		continue
	populatedLocations.append((x,y))		#A unique node is good, so we add it to the list of used locations and keep going
	newTile = [x, y]						#Start constructing a node by saying where it is

	#figure out what the new tile type should be
	if(nodes[0][2]=='n'):
		newTile.append(southOpenings[randint(0,len(southOpenings)-1)])
	elif(nodes[0][2]=='e'):
		newTile.append(westOpenings[randint(0,len(westOpenings)-1)])
	elif(nodes[0][2]=='s'):
		newTile.append(northOpenings[randint(0,len(northOpenings)-1)])
	elif(nodes[0][2]=='w'):
		newTile.append(eastOpenings[randint(0,len(eastOpenings)-1)])

	for i in range(1, len(newTile[len(newTile)-1])):			#loop over all the dangling nodes associated with a tile
		newNode = list(newTile[2][i])
		newNode[0]+=x
		newNode[1]+=y
		nodes.append(newNode)

	nodes.pop(0)					#Drop the node we just operated on
	tileset.append(newTile)			#Add the tile to the tileset



#if we've timed out, there are still dangling nodes. Populate them all with dead ends. This won't work when nodes overlap, but that's a problem for later.
for node in nodes:
	print(node)
	newTile = [node[0],node[1]]
	if(tuple(newTile) not in populatedLocations):
		populatedLocations.append((node[0],node[1]))
		if(node[2]=='n'):
			newTile.append(nRoom)
		elif(node[2]=='e'):
			newTile.append(eRoom)
		elif(node[2]=='s'):
			newTile.append(sRoom)
		elif(node[2]=='w'):
			newTile.append(wRoom)
		tileset.append(newTile)

#print(tileset)
#print("\n\n\n"+ str(nodes) + "\n\n\n")
renderMap(tileset)
print("\n\n\n"+ str(nodes) + "\n\n\n")