from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
	#Dictionary declarations:
	prev = {}
	dist = {}
	
	#set dist and prev for src
	dist[src] = 0
	prev[src] = None
	
	#q is list of unvisited nodes
	q = []
	
	#push tuples onto q. (dist, node)
	heappush(q, (0,src))
	
	#Iterate through q
	while q:
		#This gets dist, then a node (i,j)
		u = heappop(q)
		#Throw away distance, store (i,j) in cell
		_,cell = u
		#Get and iterate through neighbors
		neighbors = adj(graph,cell)
		#If destination, return
		if u == dst:
			return traceback(prev,u,src)
		for n in neighbors:
			#alt is the distance from source to this neighbor
			alt = dist[cell] + distance(cell,n)
			#If this is shorter than the previous shortest
			if n not in dist or alt < dist[n]:
				dist[n] = alt
				prev[n] = cell
				heappush(q,(alt,n))
	
def traceback(prevlist, cell, src):
	path = []
	while cell != None:
		path.append(cell);
		cell = prevlist[cell];
	return path
  
	
def distance(cell1, cell2):
	x1, y1 = cell1
	x2, y2 = cell2
	#Distance formula
	return sqrt((x2-x1)**2 + (y2-y1)**2);
	
#Compute the neighbours of the given cell in the given level
def navigation_edges(level, cell):
  steps = []
  x, y = cell
  for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x + dx, y + dy)
			dist = sqrt(dx*dx+dy*dy)
			if dist > 0 and next_cell in level['spaces']:
				steps.append(next_cell)

  return steps

def test_route(filename, src_waypoint, dst_waypoint):
	#Level gets stored
	level = load_level(filename)

	#print level['waypoints']['a']
	
	#Level gets drawn on screen
	show_level(level)
	
	#src and dst are set.
	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]

	#Path is found.
	path = dijkstras_shortest_path(src, dst, level, navigation_edges)

	if path:
		show_level(level, path)
	else:
		print "No path possible!"

if __name__ ==  '__main__':
	import sys
	#Store the relevant arguments on the cmd line
	_, filename, src_waypoint, dst_waypoint = sys.argv
	test_route(filename, src_waypoint, dst_waypoint)
