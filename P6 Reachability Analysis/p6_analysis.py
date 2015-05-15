from p6_game import Simulator
from heapq import heappush, heappop

ANALYSIS = {}

shortest_paths = {}

#design is a dict containing information loaded from
#the map file named on the cmd line
def analyze(design):
  #Use this dict to construct a Simulator object.
  sim = Simulator(design)
  init = sim.get_initial_state()
  iPos, iAb = init
  moves = sim.get_moves()
	
  #dictionaries
  prev = {}
  dist = {}

  #initial values for dictionaries
  dist[iPos] = 0
  prev[iPos] = None
    
  #heapq of unvisited nodes
  q = []

  #push initial value
  heappush(q, (0, init))
  #while we have values in the immediate surrounding unvisited nodes we plan to visit, loop
  while q:
    #pull a state out of q and get pertinent information about node within and surrounding nodes
    u = heappop(q)
    _, state = u
    cPos, cAb = state
    
    if sim.is_end_state(state):
      print "End state reachable"

    #check neighbors and inserting info from shortest path
    for move in moves:
      next_state = sim.get_next_state(state, move)
      if next_state:
          nPos = ()
          nPos, nAb = next_state
          alt = dist[cPos] + 1
          if nPos not in dist or alt < dist[nPos]:
            dist[nPos] = alt
            prev[nPos] = cPos
            heappush(q, (alt, next_state))
	
  return prev

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    raise NotImplementedError