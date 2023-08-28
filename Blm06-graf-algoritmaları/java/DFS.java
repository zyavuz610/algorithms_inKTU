import java.util.*;

public class DFS {
    
    public static void main(String[] args) {
        Map<String, List<String>> adjVertices1 = new HashMap<>();
        adjVertices1.put("A", Arrays.asList("E"));
        adjVertices1.put("B", Arrays.asList("D","E"));
        adjVertices1.put("C", Arrays.asList("D"));
        adjVertices1.put("D", Arrays.asList("B","C","E"));
        adjVertices1.put("E", Arrays.asList("A","B","D"));

        Map<String, List<String>> adjVertices2 = new HashMap<>();
        adjVertices2.put("1", Arrays.asList("2","3"));
        adjVertices2.put("2", Arrays.asList("1","3","8"));
        adjVertices2.put("3", Arrays.asList("1","2","4","5"));
        adjVertices2.put("4", Arrays.asList("3","5"));
        adjVertices2.put("5", Arrays.asList("3","4","6"));
        adjVertices2.put("6", Arrays.asList("5","7"));
        adjVertices2.put("7", Arrays.asList("6","8","10"));
        adjVertices2.put("8", Arrays.asList("2","7","9"));
        adjVertices2.put("9", Arrays.asList("9","10"));
        adjVertices2.put("10", Arrays.asList("7","9","11"));
        adjVertices2.put("11", Arrays.asList("10","12"));
        adjVertices2.put("12", Arrays.asList("11"));


        Graph graph1 = new Graph(adjVertices1);
        Graph graph2 = new Graph(adjVertices2);

        System.out.println(graph1.DFS("E"));
        System.out.println(graph2.DFS("7"));
        System.out.println(graph1.BFS("E"));
        System.out.println(graph2.BFS("7"));
    }
}

class Graph{
	private Map<String, List<String>> adjVertices;

    public Graph(Map<String, List<String>> adjVertices) {
        this.adjVertices = new HashMap<>(adjVertices);
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
    public List<String> BFS(String node){
        List<String> result = new ArrayList<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(node);
        while(!queue.isEmpty()){
            String current = queue.remove();
            if(!result.contains(current)){
                result.add(current);
                queue.addAll(adjVertices.get(current));
            }
        }
        return result;
    }

    public Map<String, List<String>> getAdj() {
		return adjVertices;
	}
    
}
