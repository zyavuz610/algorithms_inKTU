import java.util.*;

public class WelshPowellAlgorithm {
    public static void main(String [] args){

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

        graph.WelshPowell();
    }
}

class Graph{
	private Map<String, List<String>> adjVertices= new HashMap<>();
    
    public void WelshPowell(){
        
        Map<String, String> vertexColor = new HashMap<>();
        Map<String, Integer> vertexList = new HashMap<>();
        String[] colors = {"RED","BLUE","GREEN","YELLOW","PURPLE","ORANGE"};


        for (String string : adjVertices.keySet()) {
            vertexList.put(string,adjVertices.get(string).size());
            vertexColor.put(string,null);
        }

        List<Map.Entry<String, Integer>> sortedList = new ArrayList<>(vertexList.entrySet());
        sortedList.sort(Map.Entry.comparingByValue());
        Collections.reverse(sortedList);

        int i=0;
        while(vertexColor.containsValue(null)){
            for (Map.Entry<String,Integer> entry : sortedList) {
                String node = entry.getKey();
                if(vertexColor.get(node)==null && nodeCheck(adjVertices.get(node),vertexColor,colors[i])){
                    vertexColor.put(node,colors[i]);
                }
            }
            i++;
        }  
        System.out.println(vertexColor);
    }

    private boolean nodeCheck(List<String> adjNodes, Map<String, String> vertexColor, String control) {
        for (String string : adjNodes) {
            String color = vertexColor.get(string);
            if (color != null && color.equals(control)) {
                return false;
            }  
        }
        return true;
    }

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

    public void addVertex(String vertex) {
        adjVertices.putIfAbsent(vertex, new ArrayList<>());
    }

    public Map<String, List<String>> getAdj() {
		return adjVertices;
	}

}