London_walk = ox.graph_from_place('London, UK', network_type='walk')
London_walk_simple=nx.Graph(London_walk)

street_bus=London_walk_simple.copy()
street_bus.add_nodes_from(BN.nodes(data=True))
street_bus.add_edges_from(BN.edges(data=True))

# create tree
street_nodes=[]
for node,data in London_walk_simple.nodes(data=True):
    street_nodes.append(data['pos'])
street_nodes_array=np.vstack(street_nodes)

tree = KDTree(street_nodes_array)

def passenger_node_mapping(node,prestige_id,easting,northing,to_be_mapped_graph,tree_graph,tree):
    to_be_mapped_graph.add_node(node,
                                easting_amt = easting,
                                northing_amt=northing,
                                pos=(easting,northing),
                                prestige_id=prestige_id,
                                mode='walk',specific_mode='passenger',
                                size=0.01,color='#2ECCFA'
                               )
    to_be_mapped_graph.add_edge(node,
                                tree_graph.nodes()[tree.query([easting,northing])[1]], 
                                length=tree.query([easting,northing])[0],
                                weight=tree.query([easting,northing])[0]/80,
                                color='#A4A4A4',
                                ivt=None,
                                waiting_time=None,
                                walking_time=tree.query([easting,northing])[0]/80,
                                boarding=None,
                                mode='walk',
                                specific_mode='street',
                                width=0.005,
                                size=0.01                          
                                    ),
    to_be_mapped_graph.add_edge(tree_graph.nodes()[tree.query([easting,northing])[1]], 
                                node,
                                length=tree.query([easting,northing])[0],
                                weight=tree.query([easting,northing])[0]/80,
                                color='#A4A4A4',
                                ivt=None,
                                waiting_time=None,
                                walking_time=tree.query([easting,northing])[0]/80,
                                boarding=None,
                                mode='walk',
                                specific_mode='street',
                                width=0.005,
                                size=0.01                          
                                    )
           
    return to_be_mapped_graph

## example
## passenger_node_mapping('walala',prestige_id=189765768,easting=529997,northing=181436,to_be_mapped_graph=street_bus, tree_graph=London_walk_simple,tree=tree)
