from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop

def dijkstras_shortest_path(src, dst, graph, adj):
  raise NotImplementedError	

def navigation_edges(level, cell):
  raise NotImplementedError

def test_route(filename, src_waypoint, dst_waypoint):
	#Level gets stored
	level = load_level(filename)

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
