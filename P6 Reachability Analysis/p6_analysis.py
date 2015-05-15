from p6_game import Simulator
from heapq import heappush, heappop

ANALYSIS = {}

shortest_paths = {}


#design is a dict containing information loaded from
#the map file named on the cmd line
def analyze(design):
  prevs = []
  states_list = []
  last_states = []
  
  #Use this dict to construct a Simulator object.
  sim = Simulator(design)
  init = sim.get_initial_state()
  
  er = False
  
  prev, states, last_state, end_reachable = _search(sim, init)
  if er is False:
    er = end_reachable
  
  prevs.append(prev)
  states_list.append(states)
  last_states.append(last_state)
  
  while last_state:
      prev, states, last_state, end_reachable = _search(sim, last_state)
      if er is False:
        er = end_reachable
      
      prevs.append(prev)
      states_list.append(states)
      last_states.append(last_state)
  
  if er:
    print "End state reachable"
  else:
    print "End state unreachable"
  
  #prevs.reverse()
  #states_list.reverse()
  #last_states.reverse()
  
  global ANALYSIS
  ANALYSIS = (prevs, states_list, last_states)
  
  return prev

  
def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    
    node = (i, j)
    prevs, states_list, last_states = ANALYSIS
    
    i = -1
    for index, prev in enumerate(prevs):
        if node in prev:
            i = index
            break
    
    if i is -1:
        print "No path to this location"
        return
    else:
        print "Path found to location"
        
    prev = prevs[i]
    
    nprev = prev[node]
        
    while nprev:
        draw_line(node, nprev, (0, 0), states_list[i][nprev][1])
        node = nprev
        nprev = prev[nprev]
    
    i -= 1
    
    while i >= 0:
        prev = prevs[i]
        node = last_states[i][0]
        
        nprev = prev[node]
        
        while nprev:
            draw_line(node, nprev, (0, 0), states_list[i][nprev][1])
            node = nprev
            nprev = prev[nprev]
            
        i -= 1
        
        
def _search(simulator, initial_state):
  end_reachable = False
  iPos, iAb = initial_state
  moves = simulator.get_moves()
	
  #dictionaries
  prev = {}
  dist = {}
  states = {}

  #initial values for dictionaries
  dist[iPos] = 0
  prev[iPos] = None
  states[iPos] = initial_state
    
  #heapq of unvisited nodes
  q = []

  #push initial value
  heappush(q, (0, initial_state))
  #while we have values in the immediate surrounding unvisited nodes we plan to visit, loop
  while q:
    #pull a state out of q and get pertinent information about node within and surrounding nodes
    u = heappop(q)
    _, state = u
    cPos, cAb = state
    
    if simulator.is_end_state(state):
      end_reachable = True

    #check neighbors and inserting info from shortest path
    for move in moves:
      next_state = simulator.get_next_state(state, move)
      if next_state:
          nPos = ()
          nPos, nAb = next_state
          states[nPos] = next_state
          alt = dist[cPos] + 1
          if nPos not in dist or alt < dist[nPos]:
            dist[nPos] = alt
            prev[nPos] = cPos
            heappush(q, (alt, next_state))
            if nAb is not cAb:
              #abilities have changed, start search again from the current location
              last_state = next_state
              states[nPos] = next_state
              if simulator.is_end_state(state):
                end_reachable = True
              return prev, states, last_state, end_reachable
	
  return prev, states, None, end_reachable #search exhausted
    
    