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
	dist[source_point] = 0
	prev[source_point] = None
	
	#q is list of unvisited nodes
	q = []
	
	#push source_point onto q
	heappush(q, (0,source_point))
	
	#Iterate through q
	while q:
		#This gets dist, then a node (i,j)
		u = heappop(q)
		#Throw away distance, store (i,j) in cell
		_,cell = u
		
		#Go through all boxes, see which one our point is in
		significant_box = find_box(cell, mesh)
		
		print "SIG BOX "
		print significant_box
		print "CELL "
		print cell
				
		#Get all the neighbors of that box
		neighbors = mesh['adj'][significant_box]
		
		#If destination, return
		if source_point == destination_point:
			return traceback(prev,u,source_point)
		for n in neighbors:
			#alt is the distance from source to this neighbor
			next_point = find_border_point(cell,n)
			alt = dist[cell] + distance(cell,next_point)
			#If this is shorter than the previous shortest
			if next_point not in dist or alt < dist[next_point]:
				dist[next_point] = alt
				prev[next_point] = cell
				heappush(q,(alt,next_point))
	
	return path, visited

"""def find_path (source_point, destination_point, mesh) :
	path = []
	visited = []
	
	visited.append(find_box(source_point,mesh))
	visited.append(find_box(destination_point,mesh))
	
	return path, visited"""
	
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
	
def find_box(point, mesh):
	for box in mesh['boxes']:
		if box[0] <= point[0] <= box[1] and box[2] <= point[1] <= box[3] :
			return box
	return None
	
def find_border_point(point, box):
	resultx = point[0];
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