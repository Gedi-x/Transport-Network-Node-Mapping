def graph_update(street_network,previous_graph,taget_transport_graph,mode,specific_mode):
    from scipy.spatial import KDTree, cKDTree
    previous_graph.add_nodes_from(taget_transport_graph.nodes(data=True))
    previous_graph.add_edges_from(taget_transport_graph.edges(data=True))
    street_nodes=[]
    for node,data in street_network.nodes(data=True):
        street_nodes.append(data['pos'])
    street_nodes_array=np.vstack(street_nodes)
    tree = KDTree(street_nodes_array)
    stop_list=[]
    for node,data in previous_graph.nodes(data=True):
        if data['mode']==mode and data['specific_mode']==specific_mode:# add mode and specific mode
            stop_list.append(node)
    for node in stop_list:
         previous_graph.add_edge(node,
                                street_network.nodes()[tree.query(previous_graph.node[node]['pos'])[1]],
                                length=tree.query(previous_graph.node[node]['pos'])[0],
                                weight=tree.query(previous_graph.node[node]['pos'])[0]/80,
                                color='#A4A4A4',
                                ivt=None,
                                waiting_time=None,
                                walking_time=tree.query(previous_graph.node[node]['pos'])[0]/80,
                                boarding=None,
                                mode='walk',
                                specific_mode='street',
                                width=0.005,
                                size=0.01
                )
 
    for node in stop_list:
        previous_graph.add_edge(street_network.nodes()[tree.query(previous_graph.node[node]['pos'])[1]],
                                node,
                                length=tree.query(previous_graph.node[node]['pos'])[0],
                                weight=tree.query(previous_graph.node[node]['pos'])[0]/80,
                                color='#A4A4A4',
                                ivt=None,
                                waiting_time=None,
                                walking_time=tree.query(previous_graph.node[node]['pos'])[0]/80,
                                boarding=None,
                                mode='walk',
                                specific_mode='street',
                                width=0.005,
                                size=0.01
                )
    return previous_graph
