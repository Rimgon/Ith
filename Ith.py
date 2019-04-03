#Script to auto-generate dungeons for Dungeons and Dragons and similar systems
#Written for Python 3 by Rimgon, 2019

#Pieces of ascii drawings, for copy+pasting: ║ ═ ╗ ╔ ╝ ╚ ╣ ╬ ╠ ╦ ╩  

'''
ewHall

╔═════════╗
╚         ╝
╔         ╗
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
 ║       ╚ 
 ║       ╔ 
 ╚═══════╝ 


nRoom
╔═══╝ ╚═══╗
║         ║
║         ║
║         ║
║         ║
╚═════════╝

sRoom
╔═════════╗
║         ║
║         ║
║         ║
║         ║
╚═══╗ ╔═══╝

eRoom
╔═════════╗
║         ║
║         ╚
║         ╔
║         ║
╚═════════╝

wRoom
╔═════════╗
║         ║
╝         ║
╗         ║
║         ║
╚═════════╝

neRoom
╔═══╝ ╚═══╗
║         ║
║         ╚
║         ╔
║         ║
╚═════════╝

nwRoom
╔═══╝ ╚═══╗
║         ║
╝         ║
╗         ║
║         ║
╚═════════╝

seRoom
╔═════════╗
║         ║
║         ╚
║         ╔
║         ║
╚═══╗ ╔═══╝

swRoom
╔═════════╗
║         ║
╝         ║
╗         ║
║         ║
╚═══╗ ╔═══╝

nseRoom
╔═══╝ ╚═══╗
║         ║
║         ╚
║         ╔
║         ║
╚═══╗ ╔═══╝

nswRoom
╔═══╝ ╚═══╗
║         ║
╝         ║
╗         ║
║         ║
╚═══╗ ╔═══╝

newRoom
╔═══╝ ╚═══╗
║         ║
╝         ╚
╗         ╔
║         ║
╚═════════╝

sewRoom
╔═════════╗
║         ║
╝         ╚
╗         ╔
║         ║
╚═══╗ ╔═══╝

nsewRoom
╔═══╝ ╚═══╗
║         ║
╝         ╚
╗         ╔
║         ║
╚═══╗ ╔═══╝
'''

nsHall = ("nsHall", (0,-1),(0,1))

ewHall = ("ewHall", (-1,0),(1,0))


nRoom = ("nRoom",(0,1))

sRoom = ("sRoom",(0,-1))

eRoom = ("eRoom",(1,0))

wRoom = ("wRoom",(-1,0))


neRoom = ("neRoom", (1,0),(0,1))

nwRoom = ("nwRoom", (-1,0),(0,1))

seRoom = ("seRoom", (1,0),(0,-1))

swRoom = ("swRoom", (-1,0), (0, -1))


nseRoom = ("nseRoom", (1,0),(0,1),(0,-1))

nswRoom = ("nswRoom", (-1,0),(0,1),(0,-1))

newRoom = ("newRoom", (1,0),(0,1),(-1,0))

sweRoom = ("sweRoom", (-1,0), (1,0), (0, -1))

nsewRoom = ("nsweRoom", (-1,0), (1,0), (0,1), (0, -1))


print(cornerRoom[0])
print(lrHall[0])