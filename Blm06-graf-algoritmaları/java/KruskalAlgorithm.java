import java.util.*;

public class KruskalAlgorithm{
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
        
        graph.Kruskal();
    }
}


class Graph{
	private Map<String, Map<String, Integer>> adjVertices = new HashMap<>();
    private List<Edge> edges = new ArrayList<>();

    public List<Edge> getEdges() {
        return edges;
    }

    public void Kruskal(){
        Map<String,Map<String,Integer>> MST = new HashMap<>();
        sortEdges();
        int cost = 0;
        for (Edge edge : edges) {
            String source = edge.source;
            String next = edge.next;
            int weight = edge.weight;
            addEdgeMST(source,next,weight,MST);
            cost = cost + weight;
            if(isCyclic(MST)){
                removeEdge(source, next, MST);
                cost = cost - weight;
            }
        }

        System.out.println(MST);
        System.out.println("-----");
        System.out.println("Maliyet :"+cost);
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

    private void sortEdges(){
        Comparator<Edge> comparator = (p1, p2) -> Integer.compare(p1.weight, p2.weight);
        Collections.sort(edges, comparator);
    }

    Boolean isCyclic(Map<String,Map<String,Integer>> graph)
    {
        Set<String> visited = new HashSet<>();

        for (String string : graph.keySet()) {
            if(!visited.contains(string)){
                if(isCyclicUtil(string, visited, null, graph)){
                    return true;
                }
            }
        }
        
        return false;
    }

    Boolean isCyclicUtil(String current, Set<String> visited, String parent,Map<String,Map<String,Integer>> graph)
    {
        visited.add(current);
        String key;
        Set<String> keySet= graph.get(current).keySet();
        Iterator<String> it = keySet.iterator();
        while (it.hasNext()) {
            key = it.next();
 
            if (!visited.contains(key)) {
                if (isCyclicUtil(key, visited, current, graph)){
                    return true;
                }
            }

            else if (!key.equals(parent)){
                return true;
            }
        }
        return false;
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
