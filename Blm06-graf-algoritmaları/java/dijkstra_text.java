import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class dijkstra {
    public static void main(String [] args){
        String fileName = "dijkstra_graf.txt" ;
    
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line ;
            Graph graph = new Graph();

            while ((line = br.readLine()) != null) {
                String[] parts = line.split(" ");
                String u = parts[0];
                String v = parts[1];
                int w = Integer.parseInt(parts[2]);
                graph.addEdge(u,v,w);
            }
            System.out.println(graph.getAdj());
            graph.Dijkstra("A", "G");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


class Graph{

    private  Map<String, Map<String, Integer>> adjVertices = new HashMap<>();
    private  Set<String> visitedNodes = new HashSet<>();
    private  Map<String, Integer> distance = new HashMap<>();
    private  Map<String, String> previousNode = new HashMap<>();

    public Set<String> getVisitedNodes() {
        return visitedNodes;
    }

    public Map<String, Integer> getDistance() {
        return distance;
    }

    public void Dijkstra(String start,String finish){

        for (String node : adjVertices.keySet()) {
            if (node.equals(start)) {
                distance.put(node, 0);
            } else {
                distance.put(node, Integer.MAX_VALUE);
            }
            previousNode.put(node, null);
        }

        while (!visitedNodes.contains(finish)) {
            String currentNode = getNodeWithShortestDistance();
            visitedNodes.add(currentNode);

            Map<String, Integer> neighbors = adjVertices.get(currentNode);
            for (String neighbor : neighbors.keySet()) {
                int cost = neighbors.get(neighbor);
                int totalCost = cost + distance.get(currentNode);
                if (totalCost < distance.get(neighbor)) {
                    distance.put(neighbor, totalCost);
                    previousNode.put(neighbor, currentNode);
                }
            }
        }

        System.out.println("En kısa yol: " + getShortestPath(finish));
        System.out.println("Maliyet: " + distance.get(finish));
    }

    private  String getNodeWithShortestDistance() {
        String result = null;
        int shortestDistance = Integer.MAX_VALUE;
        for (String node : distance.keySet()) {
            if (!visitedNodes.contains(node) && distance.get(node) < shortestDistance) {
                result = node;
                shortestDistance = distance.get(node);
            }
        }
        return result;
    }

    private  List<String> getShortestPath(String endNode) {
        List<String> path = new ArrayList<>();
        String currentNode = endNode;
        while (currentNode != null) {
            path.add(0, currentNode);
            currentNode = previousNode.get(currentNode);
        }
        return path;
    }
    public void addVertex(String vertex) {
        adjVertices.putIfAbsent(vertex, new HashMap<String,Integer>());
    }

    public void addEdge(String src, String dest,int weight) {
        if(!adjVertices.containsKey(src)){
            addVertex(src);
        }
        if(!adjVertices.containsKey(dest)){
            addVertex(dest);
        }
        adjVertices.get(src).put(dest,weight);
        adjVertices.get(dest).put(src,weight);
    }

    public Map<String, Map<String,Integer>> getAdj() {
		return adjVertices;
	}
    
}