class mdNode():
    def __init__(self, data=None, dimensions=None, next_nodes=None, prev_nodes=None):
        self.data = data
        self.dims = dimensions
        self.nexts = next_nodes
        self.prevs = prev_nodes

root = mdNode('a',[0,1,2,3,4],
              [mdNode('h',[0,1,2,3,4]),
               mdNode('d1',[0,1,2,3,4]),
               mdNode('d2',[0,1,2,3,4]),
               mdNode('d3',[0,1,2,3,4]),
               mdNode('t',[0,1,2,3,4])])
