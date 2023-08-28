import java.util.*;

public class FleuryAlgorithm {
 
    public static void main(String[] args) {
        Graph graph = new Graph();
        
        graph.addEdge("A","B");
        graph.addEdge("A","C");
        graph.addEdge("B","C");
        graph.addEdge("C","D");
        graph.addEdge("D","E");
        graph.addEdge("D","F");
        graph.addEdge("D","G");
        graph.addEdge("E","F");
        graph.addEdge("F","G");
        
        System.out.print("Euler Path: ");
        graph.printEulerPath();
    }
}


class Graph{
	private Map<String, List<String>> adjVertices= new HashMap<>();

    public void addEdge(String src, String dest) {
        if(!adjVertices.containsKey(src)){
            addVertex(src);
        }
        if(!adjVertices.containsKey(dest)){
            addVertex(dest);
        }
        adjVertices.get(src).add(dest);
        adjVertices.get(dest).add(src);
    }

    private void removeEdge(String u, String v) {
        adjVertices.get(u).remove(v);
        adjVertices.get(v).remove(u);
    }

    public void addVertex(String vertex) {
        adjVertices.putIfAbsent(vertex, new ArrayList<>());
    }

    public Map<String, List<String>> getAdj() {
		return adjVertices;
	}

    private boolean isValidNextEdge(String u, String v) {
        
        if (adjVertices.get(u).size() == 1) {
            return true;
        }
        
        int count1 = DFS(u).size();
        
        removeEdge(u, v);

        int count2 = DFS(u).size();
        
        addEdge(u, v);
        
        return (count1 > count2) ? false : true;
    }

    public List<String> DFS(String node){
        List<String> result = new ArrayList<>();
        DFSUtil(node,result);
        return result;
    }
    public void DFSUtil(String node,List<String> result){
        if(!result.contains(node)){
            result.add(node);
            for (String n : adjVertices.get(node)) {
                DFSUtil(n,result);
            }
        }
    }

    public void printEulerPath() {
        String u = null;
        Iterator <String> iterator = adjVertices.keySet().iterator();
        if (iterator.hasNext()) {
            u = (String) iterator.next();
        }        

        for (String i : adjVertices.keySet()) {
            if (adjVertices.get(i).size() % 2 != 0) {
                u = i;
                break;
            }
        }
        printEulerUtil(u);
        System.out.println();
    }

    private void printEulerUtil(String u) {
        for (String v : adjVertices.get(u)) {
            if (isValidNextEdge(u, v)) {
                System.out.print(u + "-" + v + " ");
                removeEdge(u, v);
                printEulerUtil(v);
                break;
            }
        }
    }

}