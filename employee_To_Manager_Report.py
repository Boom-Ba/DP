# employeeToManagerMappings = {'A': 'A', 'B': 'A', 'C': 'B',
#                               'D': 'B', 'E': 'D', 'F': 'E'}
##output: {'A': {'E', 'F', 'C', 'B', 'D'}, 
#         'E': {'F'}, 'F': set(), 'C': set(), 
#         'B': {'C', 'E', 'F', 'D'}, 'D': {'E', 'F'}}
def dfs(i,adj,visited,temp):
  visited.add(i)
  for w in adj[i]:
    temp.append(w)
    dfs(w,adj,visited,temp)
  return temp
def employeeToManager_Report(employeeToManagerMappings):
  V=set()
  adj={}
  for k,v in employeeToManagerMappings.items():
    V.add(k)
    V.add(v)
  adj ={i:[] for i in V}
  for k,v in employeeToManagerMappings.items():
    if k!=v:
      adj[v].append(k)

  res={i:set() for i in V}
  for i in V:
    t=set()
    visited=set()
    if i not in visited:
      t= set(dfs(i,adj,visited,[]))
    res[i]=t
  return res
