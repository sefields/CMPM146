import collections
import pickle
import sys
import random
import traceback
import Tkinter
from heapq import heappush, heappop
from math import sqrt

def find_path (source_point, destination_point, mesh) :
	path = []
	visited = []
			
	#Dictionary declarations:
	prev = {}
	dist = {}
	
	#set dist and prev for src
	dist[find_box(source_point, mesh)] = 0
	prev[find_box(source_point, mesh)] = None
	
	#q is list of unvisited boxes
	q = []
	
	#push source_point onto q
	heappush(q, (0,find_box(source_point,mesh)))
	
	destination_box = find_box(destination_point , mesh);
	inDist = 0
	altDist = 0
	#Iterate through q
	while q:
		#This gets dist, then a node (i,j)
		u = heappop(q)
		#Throw away distance, store (x1,x2,y1,y2) in cell
		_,cell = u
		
		#Go through all boxes, see which one our point is in
		#significant_box = find_box(cell, mesh)
		# print "SIG BOX "
		# print significant_box
		# print "CELL "
		# print cell
				
		#Get all the neighbors of that box
		neighbors = mesh['adj'][cell]
		
		#If destination, return
		if cell == destination_box:
			print "This doesn't happen"
			return (traceback(prev,cell,source_point), visited)
		for n in neighbors:
		
			visited.append(n)
			#alt is the distance from source to this neighbor
			#next_point = find_border_point(cell,n)
			alt = dist[cell] + distance(cell,n)
			#If this is shorter than the previous shortest
			
			if n not in dist or alt < dist[n]:
				dist[n] = alt
				prev[n] = cell
				heappush(q,(alt,n))
	
	return path, visited

"""def find_path (source_point, destination_point, mesh) :
	path = []
	visited = []
	
	visited.append(find_box(source_point,mesh))
	visited.append(find_box(destination_point,mesh))
	
	return path, visited"""
	
"""def traceback(prevlist, cell, src):
	path = []
	lastPoint = cell
	cell = prevlist[cell];
	while cell != None:
		path.append((lastPoint, cell));
		
		cell = prevlist[cell];
		lastPoint = cell
		
	return path"""
	
def traceback(prevlist, cell, src):
	path = []
	lastPoint = cell
	lastPointMP = midpoint(lastPoint)
	cell = prevlist[cell];
	cellMP = midpoint(cell)
	while cell != None:
		cellMP = midpoint(cell)
		path.append((lastPointMP, cellMP));
		
		lastPoint = cell
		lastPointMP = midpoint(lastPoint)
		cell = prevlist[cell];
		
	#print src
	#path.append((lastPointMP,src))	
	return path
	
def midpoint(box):
	x = round((0.5*(box[0]+box[1])), 0)
	y = round((0.5*(box[2]+box[3])), 0)
	return (x,y)
	
def distance(cell1, cell2):
	x1 = 0.5*(cell1[0]+cell1[1])
	y1 = 0.5*(cell1[2]+cell1[3])
	x2 = 0.5*(cell2[0]+cell2[1])
	y2 = 0.5*(cell2[2]+cell2[3])
	# x1, y1 = cell1
	# x2, y2 = cell2
	# #Distance formula
	return sqrt((x2-x1)**2 + (y2-y1)**2);
	
def find_box(point, mesh):
	for box in mesh['boxes']:
		if box[0] <= point[0] <= box[1] and box[2] <= point[1] <= box[3] :
			return box
	return None
	
def find_border_point(point, box):
	resultx = point[0]
	resulty = point[1]
	
	if point[0] > box[1]:
		resultx = box[1]
	if point[0] < box [0]:
		resultx = box[0]
	if point[1] > box[3]:
		resulty = box[3]
	if point[1] < box[2]:
		resulty = box[2]
	result = (resultx, resulty)
	return result
	"""currX = point[0]
	currY = point[1]
	
	borderX1 = box[0]
	borderX2 = box[1]
	borderY1 = box[2]
	borderY2 = box[3]
	
	currX = min(borderX2-1,max(borderX1,currX))
	currY = min(borderY2-1,max(borderY1,currY))
		
	return (currX, currY)"""