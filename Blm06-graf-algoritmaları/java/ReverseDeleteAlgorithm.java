import java.util.*;

public class ReverseDeleteAlgorithm{
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

        graph.ReverseDelete();

    }
}

class Graph{
	private Map<String, Map<String, Integer>> adjVertices = new HashMap<>();
    private List<Edge> edges = new ArrayList<>();

    public void ReverseDelete(){
        Map<String,Map<String,Integer>> MST = new HashMap<>();
        for (String outerKey : adjVertices.keySet()) {
            Map<String, Integer> innerMap = adjVertices.get(outerKey);
            Map<String, Integer> newInnerMap = new HashMap<>(innerMap); 
            MST.put(outerKey, newInnerMap);
        }
        sortEdges();

        for (Edge edge : edges) {
            removeEdge(edge.source, edge.next, MST);
            if(!isConnected(edge.source, MST)){
                addEdgeMST(edge.source, edge.next, edge.weight, MST);
            }
        }
        System.out.println(MST);
    }

    public List<Edge> getEdges() {
        return edges;
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

        edges.add(new Edge(src, dest, weight));

    }
    private void addEdgeMST(String src, String dest,int weight,Map<String,Map<String,Integer>> graph) {
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

    private void removeEdge(String src, String dest,Map<String,Map<String,Integer>> graph) {
        graph.get(src).remove(dest);
        graph.get(dest).remove(src);
    }

    private boolean isConnected(String node, Map<String,Map<String,Integer>> graph){
        return DFS(node,graph).size()==graph.keySet().size();
    }
    
    private void sortEdges(){
        Comparator<Edge> comparator = (p1, p2) -> Integer.compare(p2.weight, p1.weight);
        Collections.sort(edges, comparator);
    }

    public List<String> DFS(String node,Map<String,Map<String,Integer>> graph){
        List<String> result = new ArrayList<>();
        DFSUtil(node,result,graph);
        return result;
    }

    public void DFSUtil(String node,List<String> result,Map<String,Map<String,Integer>> graph){
        if(!result.contains(node)){
            result.add(node);
            for (String n : graph.get(node).keySet()) {
                DFSUtil(n,result,graph);
            }
        }
    }

}

class Edge{
    public String source;
    public String next;
    public int weight;

    Edge (String source,String next,int weight){
        this.source=source;
        this.next=next;
        this.weight=weight;
    }
}
