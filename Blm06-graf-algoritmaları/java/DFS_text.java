import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class DFStext {

    public static void main(String [] args){
        String fileName = "ornek_graf.txt" ;
    
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line ;
            Graph graph = new Graph();

            while ((line = br.readLine()) != null) {
                String[] parts = line.split(" ");
                String v = parts[0];
                String w = parts[1];
                graph.addEdge(v, w);
            }
            System.out.println(graph.getAdj());

            System.out.println(graph.DFS("A"));

            System.out.println(graph.BFS("A"));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Graph{
	private Map<String, List<String>> adjVertices= new HashMap<>();

    public List<String> DFS(String node){
        List<String> result = new ArrayList<>();
        DFSUtil(node,result);
        return result;
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
