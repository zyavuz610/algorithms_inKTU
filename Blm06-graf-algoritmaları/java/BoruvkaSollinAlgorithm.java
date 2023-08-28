import java.util.*;

public class BoruvkaSollinAlgorithm{
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

        graph.Boruvka();

        Graph graph2 = new Graph();

        graph2.addEdge("0","1",4);
        graph2.addEdge("0","7",8);
        graph2.addEdge("1","7",11);
        graph2.addEdge("1","2",8);
        graph2.addEdge("7","8",7);
        graph2.addEdge("7","6",1);
        graph2.addEdge("2","8",2);
        graph2.addEdge("8","6",6);
        graph2.addEdge("2","3",7);
        graph2.addEdge("2","5",4);
        graph2.addEdge("6","5",2);
        graph2.addEdge("3","5",14);
        graph2.addEdge("3","4",9);
        graph2.addEdge("4","5",10);

        graph2.Boruvka();
    }
}


class Graph{
	private Map<String, Map<String, Integer>> adjVertices = new HashMap<>();

    public void Boruvka(){
        Map<String, Map<String, Integer>> MST = new HashMap<>();
        Map<String, Map<String, Integer>> copyAdjVertices = new HashMap<>();
        UnionFind unionFind = new UnionFind();

        for (String string : adjVertices.keySet()) {
            unionFind.makeSet(string);
            for (String string2 : adjVertices.get(string).keySet()) {
                addEdgeToGraph(string, string2, adjVertices.get(string).get(string2), copyAdjVertices);
            }
        }

        for (String string : adjVertices.keySet()) {
            String current = string;
            String next = null;
            int cost = Integer.MAX_VALUE;
            for (String string2 : adjVertices.get(current).keySet()) {
                if(adjVertices.get(current).get(string2)<cost){
                    next = string2;
                    cost = adjVertices.get(current).get(next);
                }
            }
            addEdgeToGraph(current, next, cost, MST);
            removeEdge(current, next, copyAdjVertices);
        }

        for (String string : MST.keySet()) {
            for (String string2 : MST.get(string).keySet()) {
                unionFind.union(string, string2);
            }
        }

        List<List<String>> connectedNodes = unionFind.listConnectedNodes();
        while(connectedNodes.size()!=1){
            for (List<String> list : connectedNodes) {
                lessWeightEdge(list, MST, copyAdjVertices, unionFind);
                connectedNodes=unionFind.listConnectedNodes();
                break;
            }
        }

        System.out.println(MST);

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

    public void addEdgeToGraph(String src, String dest,int weight,Map<String, Map<String, Integer>> graph) {
        if(!graph.containsKey(src)){
            addVertex(graph,src);
        }
        if(!graph.containsKey(dest)){
            addVertex(graph,dest);
        }
        if(!graph.get(src).containsKey(dest)){
            graph.get(src).put(dest,weight);
        }      
        if(!graph.get(dest).containsKey(src)){
            graph.get(dest).put(src,weight);
        }
    }

    private void addVertex(Map<String,Map<String,Integer>> graph,String vertex) {
        graph.putIfAbsent(vertex, new HashMap<String,Integer>());
    }

    private void removeEdge(String src, String dest,Map<String,Map<String,Integer>> graph) {
        if(graph.get(src).containsKey(dest)){
            graph.get(src).remove(dest);
        }
        if(graph.get(dest).containsKey(src)){
            graph.get(dest).remove(src);
        }
    }

    private void lessWeightEdge(List<String> groups,Map<String,Map<String,Integer>> graph,Map<String,Map<String,Integer>> copy, UnionFind unionFind){
        String current = null;
        String next = null;
        int cost = Integer.MAX_VALUE;
        for (String node : groups) {
            for (String node2 : copy.get(node).keySet()) {
                if(node2==null){continue;}
                if(copy.get(node).get(node2)<cost && !groups.contains(node2)){
                    current = node;
                    next = node2;
                    cost = copy.get(node).get(node2);
                }
            }
        }
        if(current==null && next == null && cost == Integer.MAX_VALUE){return;}
        addEdgeToGraph(current, next, cost, graph);
        unionFind.union(current, next);
    }

}

class UnionFind {
    private Map<String, String> parent;
    private Map<String, Integer> rank;

    public UnionFind() {
        parent = new HashMap<>();
        rank = new HashMap<>();
    }

    public void makeSet(String node) {
        if (!parent.containsKey(node)) {
            parent.put(node, node);
            rank.put(node, 0);
        }
    }

    private String find(String node) {
        if (!parent.containsKey(node)) return null;

        if (!parent.get(node).equals(node)) {
            parent.put(node, find(parent.get(node)));
        }
        return parent.get(node);
    }

    public void union(String node1, String node2) {
        String root1 = find(node1);
        String root2 = find(node2);

        if (root1 == null || root2 == null || root1.equals(root2)) return;

        int rank1 = rank.get(root1);
        int rank2 = rank.get(root2);

        if (rank1 > rank2) {
            parent.put(root2, root1);
        } else if (rank1 < rank2) {
            parent.put(root1, root2);
        } else {
            parent.put(root2, root1);
            rank.put(root1, rank1 + 1);
        }
    }

    public boolean isConnected(String node1, String node2) {
        String root1 = find(node1);
        String root2 = find(node2);

        return root1 != null && root1.equals(root2);
    }

    public List<List<String>> listConnectedNodes() {
        Map<String, List<String>> connectedGroups = new HashMap<>();

        for (String node : parent.keySet()) {
            String root = find(node);
            connectedGroups.computeIfAbsent(root, k -> new ArrayList<>()).add(node);
        }

        return new ArrayList<>(connectedGroups.values());
    }
}