import java.util.*;

public class DijkstraAlgorithm {
    public static void main(String[] args) {

        Map<String, Map<String, Integer>> adjVertices1= new HashMap<>();

        adjVertices1.put("start", new HashMap<String, Integer>() {{
            put("a", 4);
            put("b", 2);
        }});
        adjVertices1.put("a", new HashMap<String, Integer>() {{
            put("b", 3);
            put("c", 1);
            put("d", 7);
        }});
        adjVertices1.put("b", new HashMap<String, Integer>() {{
            put("a", 3);
            put("c", 5);
            put("d", 8);
        }});
        adjVertices1.put("c", new HashMap<String, Integer>() {{
            put("a", 1);
            put("b", 5);
            put("d", 4);
            put("finish", 7);
        }});
        adjVertices1.put("d", new HashMap<String, Integer>() {{
            put("a", 7);
            put("c", 4);
            put("b", 8);
            put("finish", 2);
        }});
        adjVertices1.put("finish", new HashMap<String, Integer>()); 

        Map<String, Map<String, Integer>> adjVertices2= new HashMap<>();

        adjVertices2.put("start", new HashMap<String, Integer>() {{
            put("a", 2);
        }});
        adjVertices2.put("a", new HashMap<String, Integer>() {{
            put("b", 3);
            put("c", 4);
            put("e", 9);
        }});
        adjVertices2.put("b", new HashMap<String, Integer>() {{
            put("a", 3);
            put("c", 5);
            put("e", 3);
            put("f", 1);
        }});
        adjVertices2.put("c", new HashMap<String, Integer>() {{
            put("a", 4);
            put("b", 5);
            put("d", 2);
        }});
        adjVertices2.put("d", new HashMap<String, Integer>() {{
            put("c", 2);
            put("e", 2);
            put("h", 7);
        }});
        adjVertices2.put("e", new HashMap<String, Integer>() {{
            put("a", 9);
            put("b", 3);
            put("d", 2);
            put("f", 4);
            put("g", 8);
        }});
        adjVertices2.put("f", new HashMap<String, Integer>() {{
            put("b", 1);
            put("e", 4);
            put("g", 12);
        }});
        adjVertices2.put("g", new HashMap<String, Integer>() {{
            put("e", 8);
            put("f", 12);
            put("h", 10);
            put("finish",7);
        }});
        adjVertices2.put("h", new HashMap<String, Integer>() {{
            put("d", 7);
            put("g", 10);
        }});
        adjVertices2.put("finish", new HashMap<String, Integer>());


        Graph graph1= new Graph(adjVertices1);

        graph1.Dijkstra("start", "finish");

        Graph graph2= new Graph(adjVertices2);

        graph2.Dijkstra("start", "finish");
        
        System.out.println(graph2.getDistance());
        System.out.println(graph2.getVisitedNodes());
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

    public Graph(Map<String, Map<String, Integer>> adjVertices) {
        this.adjVertices = adjVertices;
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
    
}