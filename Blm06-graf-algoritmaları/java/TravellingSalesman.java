import java.util.*;

public class TravellingSalesman {
    public static void main(String [] args){
        Graph graph = new Graph();

        graph.addEdge("A", "B", 10);
        graph.addEdge("A", "C", 15);
        graph.addEdge("A", "D", 20);
        graph.addEdge("A", "E", 25);
        graph.addEdge("B", "C", 35);
        graph.addEdge("B", "D", 40);
        graph.addEdge("B", "E", 45);
        graph.addEdge("C", "D", 30);
        graph.addEdge("C", "E", 50);
        graph.addEdge("D", "E", 55);

        graph.tsp("A");

    }
}

class Graph{
	private  Map<String, Map<String, Integer>> adjVertices = new HashMap<>();

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

    public void tsp(String current) {
        int cost=0;
        List<String> path = new ArrayList<>();
        Map<String, Boolean> visited = new HashMap<>();

        for (String city : adjVertices.keySet()) {
            visited.put(city, false);
        }

        String currentCity = current;
        path.add(currentCity);
        visited.put(currentCity, true);

        while (path.size() < adjVertices.keySet().size()) {
            int minDistance = Integer.MAX_VALUE;
            String nextCity = null;

            for (Map.Entry<String, Integer> neighbor : adjVertices.get(currentCity).entrySet()) {
                String city=neighbor.getKey();
                if (!visited.get(city)) {
                    int distance = neighbor.getValue();
                    if (distance < minDistance) {
                        minDistance = distance;
                        nextCity = city;
                    }
                }
            }

            path.add(nextCity);
            cost =  cost + minDistance;
            visited.put(nextCity, true);
            currentCity = nextCity;
        }

        System.out.println("Euler path: "+ path);
        System.out.println("Total cost: "+ cost);
        
    }

}
