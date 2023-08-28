import java.util.*;

public class PrimAlgorithm{
    public static void main(String [] args){

        Graph graph = new Graph();

        graph.addEdge("A","B",5);
        graph.addEdge("A","C",7);
        graph.addEdge("B","C",9);
        graph.addEdge("C","D",6);
        graph.addEdge("D","E",2);
        graph.addEdge("D","F",1);
        graph.addEdge("D","G",5);
        graph.addEdge("E","F",3);
        graph.addEdge("F","G",2);

        graph.Prim();
    }
}


class Graph{
	private Map<String, Map<String, Integer>> adjVertices = new HashMap<>();

    public void Prim(){
        Map<String, Map<String, Integer>> MST = new HashMap<>();

        Set<String> keySet=adjVertices.keySet();
        Iterator<String> it=keySet.iterator();
        String node = it.next();

        addVertex(MST, node);
        
        for(int i = 0 ; i < adjVertices.keySet().size()-1 ; i++){
            PrimUtil(MST, adjVertices);
        }
        System.out.println(MST);
    }

    private void PrimUtil(Map<String,Map<String,Integer>> graph,Map<String,Map<String,Integer>> copy){
        int cost = Integer.MAX_VALUE;
        String currentNode = null;
        String edgeNode = null;
        List<String> cEdgeInfo = new ArrayList<>();

        for (String string : graph.keySet()) {
            cEdgeInfo = getCloseEdge(string, cost, copy, cEdgeInfo, graph);
            if(cEdgeInfo.isEmpty()){
                continue;
            }
            currentNode = cEdgeInfo.get(0);
            edgeNode = cEdgeInfo.get(1);
            cost = Integer.parseInt(cEdgeInfo.get(2));
        }

        addEdgeToMST(currentNode, edgeNode, cost, graph);
        
    }

    private List<String> getCloseEdge(String node ,int cost,Map<String,Map<String,Integer>> copy,List<String> edge,Map<String,Map<String,Integer>> graph){
        List<String> closeEdge = new ArrayList<>();
        closeEdge = edge;

        for (String string : copy.get(node).keySet()) {
            if(graph.keySet().contains(string)){
                continue;
            }
            if(copy.get(node).get(string)<cost){
                closeEdge.clear();
                closeEdge.add(node);
                closeEdge.add(string);
                closeEdge.add(copy.get(node).get(string).toString());
                cost = copy.get(node).get(string);
            }
        }
        return closeEdge;
    }
    
    public Map<String, Map<String,Integer>> getAdj() {
		return adjVertices;
	}

    public void addEdge(String src, String dest,int weight) {
        if(!adjVertices.containsKey(src)){
            addVertex(adjVertices,src);
        }
        if(!adjVertices.containsKey(dest)){
            addVertex(adjVertices,dest);
        }
        adjVertices.get(src).put(dest,weight);
        adjVertices.get(dest).put(src,weight);
    }
    
    public void addEdgeToMST(String src, String dest,int weight,Map<String, Map<String, Integer>> graph) {
        if(!graph.containsKey(src)){
            addVertex(graph,src);
        }
        if(!graph.containsKey(dest)){
            addVertex(graph,dest);
        }
        graph.get(src).put(dest,weight);
        graph.get(dest).put(src,weight);
    }
    
    private void addVertex(Map<String,Map<String,Integer>> graph,String vertex) {
        graph.putIfAbsent(vertex, new HashMap<String,Integer>());
    }

}
