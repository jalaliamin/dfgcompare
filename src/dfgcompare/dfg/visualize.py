from graphviz import Digraph

def normalize(val, min_val, max_val):
    normalized = ((val - min_val) * 5 / (max_val - min_val)) +1
    return int(normalized)

def drawDFG(dfg):
    g = Digraph('G', node_attr={'color': 'lightblue2', 'style': 'filled', 'shape': 'box'})
    # layout: fdp, neato, sfdp, twopi
    g.attr(layout='twopi', overlap='scale', splines='true')
    #g.attr(size='6,6', rankdir='RL') #"TB", "LR", "BT", "RL"
    
    min_weight = max_weight = total_weight = 0
    
    nodes = set()
    for (a,b) in dfg.keys():
        nodes.add(a)
        nodes.add(b)
        weight = dfg[(a,b)]
        if min_weight>weight:
            min_weight = weight 
        if max_weight<weight:
            max_weight = weight 
        total_weight += weight
        
    for n in nodes:
        g.node(n, label=n, style='filled,rounded', fillcolor='#22556633', fontcolor='black', color='black')
        
    for (a,b) in dfg.keys():
        weight = dfg[(a,b)]
        g.edge(a, b, constraint='false', w='1', penwidth=str(normalize(weight, min_weight, max_weight)), label=str(weight), color='#222222dd')
    
    return g