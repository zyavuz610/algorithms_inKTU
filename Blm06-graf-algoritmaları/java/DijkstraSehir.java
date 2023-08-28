import java.util.*;

public class DijkstraSehir {
    public static void main(String[] args) {

        HashMap<String,HashMap<String, Double>> hashMap = new HashMap<>();


        HashMap<String, Double> map1 = new HashMap<>();
        map1.put("31", 1.19);
        map1.put("80", 0.88);
        map1.put("46", 1.72);
        map1.put("38", 1.74);
        map1.put("51", 1.16);
        map1.put("33", 0.72);
        hashMap.put("1", map1);

        HashMap<String, Double> map2 = new HashMap<>();
        map2.put("63", 0.8);
        map2.put("21", 1.96);
        map2.put("44", 0.59);
        map2.put("46", 1.35);
        map2.put("27", 1.14);
        hashMap.put("2", map2);

        HashMap<String, Double> map3 = new HashMap<>();
        map3.put("32", 0.99);
        map3.put("42", 2.12);
        map3.put("26", 1.03);
        map3.put("43", 0.88);
        map3.put("64", 1.15);
        map3.put("20", 1.76);
        map3.put("15", 1.38);
        hashMap.put("3", map3);

        HashMap<String, Double> map4 = new HashMap<>();
        map4.put("65", 1.28);
        map4.put("76", 0.97);
        map4.put("36", 0.9);
        map4.put("25", 1.79);
        map4.put("49", 1.51);
        map4.put("13", 1.62);
        hashMap.put("4", map4);

        HashMap<String, Double> map5 = new HashMap<>();
        map5.put("66", 1.32);
        map5.put("60", 0.79);
        map5.put("55", 0.81);
        map5.put("19", 0.89);
        hashMap.put("5", map5);

        HashMap<String, Double> map6 = new HashMap<>();
        map6.put("42", 2.09);
        map6.put("68", 1.95);
        map6.put("40", 1.53);
        map6.put("39", 5.92);
        map6.put("18", 1.02);
        map6.put("14", 1.43);
        map6.put("26", 2.34);
        map6.put("3", 2.58);
        hashMap.put("6", map6);

        HashMap<String, Double> map7 = new HashMap<>();
        map7.put("33", 3.93);
        map7.put("70", 2.54);
        map7.put("42", 2.03);
        map7.put("32", 0.89);
        map7.put("15", 0.86);
        map7.put("48", 2.37);
        hashMap.put("7", map7);

        HashMap<String, Double> map8 = new HashMap<>();
        map8.put("53", 1.31);
        map8.put("25", 1.4);
        map8.put("75", 0.89);
        hashMap.put("8", map8);

        HashMap<String, Double> map9 = new HashMap<>();
        map9.put("48", 0.83);
        map9.put("20", 1.25);
        map9.put("45", 0.87);
        map9.put("35", 0.91);
        hashMap.put("9", map9);

        HashMap<String, Double> map10 = new HashMap<>();
        map10.put("35", 1.44);
        map10.put("45", 1.12);
        map10.put("43", 2.11);
        map10.put("16", 1.33);
        map10.put("17", 1.55);
        hashMap.put("10", map10);


        HashMap<String, Double> map11 = new HashMap<>();
        map11.put("43", 0.65);
        map11.put("26", 0.53);
        map11.put("14", 1.6);
        map11.put("54", 0.74);
        map11.put("16", 1.02);
        hashMap.put("11", map11);

        HashMap<String, Double> map12 = new HashMap<>();
        map12.put("21", 1.27);
        map12.put("49", 0.99);
        map12.put("25", 0.98);
        map12.put("24", 1.44);
        map12.put("62", 1.35);
        map12.put("23", 1.59);
        hashMap.put("12", map12);

        HashMap<String, Double> map13 = new HashMap<>();
        map13.put("56", 0.49);
        map13.put("65", 1.29);
        map13.put("4", 1.62);
        map13.put("49", 0.66);
        map13.put("72", 1.11);
        hashMap.put("13", map13);

        HashMap<String, Double> map14 = new HashMap<>();
        map14.put("26", 1.33);
        map14.put("6", 1.43);
        map14.put("18", 2.03);
        map14.put("67", 0.91);
        map14.put("81", 0.5);
        map14.put("54", 1.15);
        map14.put("11", 1.6);
        hashMap.put("14", map14);

        HashMap<String, Double> map15 = new HashMap<>();
        map15.put("48", 1.72);
        map15.put("7", 0.86);
        map15.put("32", 0.58);
        map15.put("3", 1.38);
        map15.put("20", 1.03);
        hashMap.put("15", map15);

        HashMap<String, Double> map16 = new HashMap<>();
        map16.put("10", 1.33);
        map16.put("43", 1.25);
        map16.put("11", 1.02);
        map16.put("54", 1.44);
        map16.put("41", 1.01);
        map16.put("77", 0.43);
        hashMap.put("16", map16);

        HashMap<String, Double> map17 = new HashMap<>();
        map17.put("10", 1.55);
        map17.put("59", 1.38);
        map17.put("22", 1.53);
        hashMap.put("17", map17);

        HashMap<String, Double> map18 = new HashMap<>();
        map18.put("6", 1.02);
        map18.put("71", 0.76);
        map18.put("19", 1.34);
        map18.put("37", 0.81);
        map18.put("67", 2.01);
        map18.put("14", 2.03);
        map18.put("78", 1.16);
        hashMap.put("18", map18);

        HashMap<String, Double> map19 = new HashMap<>();
        map19.put("66", 0.75);
        map19.put("5", 0.89);
        map19.put("55", 1.56);
        map19.put("57", 1.49);
        map19.put("37", 1.44);
        map19.put("18", 1.34);
        map19.put("71", 1.6);
        hashMap.put("19", map19);

        HashMap<String, Double> map20 = new HashMap<>();
        map20.put("48", 0.92);
        map20.put("15", 1.03);
        map20.put("3", 1.76);
        map20.put("64", 0.96);
        map20.put("45", 1.86);
        map20.put("9", 1.25);
        hashMap.put("20", map20);

        HashMap<String, Double> map21 = new HashMap<>();
        map21.put("63", 1.62);
        map21.put("47", 0.77);
        map21.put("72", 0.91);
        map21.put("49", 1.84);
        map21.put("12", 1.27);
        map21.put("23", 1.26);
        map21.put("44", 1.97);
        map21.put("2", 1.96);
        hashMap.put("21", map21);

        HashMap<String, Double> map22 = new HashMap<>();
        map22.put("17", 1.53);
        map22.put("59", 1.18);
        map22.put("71", 7.19);
        hashMap.put("22", map22);

        HashMap<String, Double> map23 = new HashMap<>();
        map23.put("21", 1.26);
        map23.put("12", 1.59);
        map23.put("62", 0.66);
        map23.put("24", 1.1);
        map23.put("44", 0.97);
        hashMap.put("23", map23);

        HashMap<String, Double> map24 = new HashMap<>();
        map24.put("23", 1.1);
        map24.put("62", 0.45);
        map24.put("12", 1.44);
        map24.put("25", 1.78);
        map24.put("69", 0.88);
        map24.put("29", 0.69);
        map24.put("28", 1.61);
        map24.put("58", 2.48);
        map24.put("44", 1.83);
        hashMap.put("24", map24);

        HashMap<String, Double> map25 = new HashMap<>();
        map25.put("12", 0.98);
        map25.put("49", 1.07);
        map25.put("4", 1.79);
        map25.put("36", 1.97);
        map25.put("75", 1.88);
        map25.put("8", 1.4);
        map25.put("53", 1.35);
        map25.put("69", 1.1);
        map25.put("24", 1.78);
        hashMap.put("25", map25);

        HashMap<String, Double> map26 = new HashMap<>();
        map26.put("3", 1.03);
        map26.put("42", 2.74);
        map26.put("6", 2.34);
        map26.put("14", 1.33);
        map26.put("11", 0.53);
        map26.put("43", 0.65);
        hashMap.put("26", map26);

        HashMap<String, Double> map27 = new HashMap<>();
        map27.put("79", 0.44);
        map27.put("63", 1.42);
        map27.put("2", 1.14);
        map27.put("46", 0.68);
        map27.put("80", 1.22);
        map27.put("31", 1.23);
        hashMap.put("27", map27);

        HashMap<String, Double> map28 = new HashMap<>();
        map28.put("29", 1.22);
        map28.put("61", 1.33);
        map28.put("24", 1.61);
        map28.put("58", 1.8);
        map28.put("52", 0.52);
        hashMap.put("28", map28);

        HashMap<String, Double> map29 = new HashMap<>();
        map29.put("24", 0.69);
        map29.put("69", 0.74);
        map29.put("61", 0.6);
        map29.put("28", 1.22);
        hashMap.put("29", map29);

        HashMap<String, Double> map30 = new HashMap<>();
        map30.put("65", 0.96);
        map30.put("73", 1.25);
        hashMap.put("30", map30);

        HashMap<String, Double> map31 = new HashMap<>();
        map31.put("79", 0.83);
        map31.put("27", 1.23);
        map31.put("80", 0.83);
        map31.put("1", 1.19);
        hashMap.put("31", map31);

        HashMap<String, Double> map32 = new HashMap<>();
        map32.put("7", 0.89);
        map32.put("42", 1.93);
        map32.put("3", 0.99);
        map32.put("15", 0.58);
        hashMap.put("32", map32);

        HashMap<String, Double> map33 = new HashMap<>();
        map33.put("1", 0.72);
        map33.put("51", 1.17);
        map33.put("42", 2.4);
        map33.put("70", 1.45);
        map33.put("7", 3.93);
        hashMap.put("33", map33);

        HashMap<String, Double> map34 = new HashMap<>();
        map34.put("41", 0.92);
        map34.put("59", 1.46);
        map34.put("39", 1.9);
        hashMap.put("34", map34);

        HashMap<String, Double> map35 = new HashMap<>();
        map35.put("9", 0.91);
        map35.put("45", 0.36);
        map35.put("10", 1.44);
        hashMap.put("35", map35);

        HashMap<String, Double> map36 = new HashMap<>();
        map36.put("4", 0.9);
        map36.put("76", 1.16);
        map36.put("75", 0.63);
        map36.put("25", 1.97);
        hashMap.put("36", map36);

        HashMap<String, Double> map37 = new HashMap<>();
        map37.put("19", 1.44);
        map37.put("57", 1.51);
        map37.put("18", 0.81);
        map37.put("74", 1.34);
        map37.put("78", 1.18);
        hashMap.put("37", map37);

        HashMap<String, Double> map38 = new HashMap<>();
        map38.put("1", 1.74);
        map38.put("46", 1.85);
        map38.put("58", 1.84);
        map38.put("66", 1.27);
        map38.put("50", 0.79);
        map38.put("51", 1.1);
        hashMap.put("38", map38);

        HashMap<String, Double> map39 = new HashMap<>();
        map39.put("22", 0.66);
        map39.put("59", 0.81);
        map39.put("34", 1.9);
        hashMap.put("39", map39);

        HashMap<String, Double> map40 = new HashMap<>();
        map40.put("50", 0.68);
        map40.put("66", 0.93);
        map40.put("71", 0.96);
        map40.put("6", 1.53);
        map40.put("68", 0.79);
        hashMap.put("40", map40);

        HashMap<String, Double> map41 = new HashMap<>();
        map41.put("77", 0.65);
        map41.put("34", 0.92);
        map41.put("16", 1.01);
        map41.put("11", 0.82);
        map41.put("54", 0.58);
        hashMap.put("41", map41);

        HashMap<String, Double> map42 = new HashMap<>();
        map42.put("3", 2.12);
        map42.put("6", 2.09);
        map42.put("7", 2.03);
        map42.put("26", 2.74);
        map42.put("32", 1.93);
        map42.put("70", 1.02);
        map42.put("33", 2.4);
        map42.put("51", 2.2);
        map42.put("68", 1.63);
        hashMap.put("42", map42);

        HashMap<String, Double> map43 = new HashMap<>();
        map43.put("26", 0.65);
        map43.put("11", 0.65);
        map43.put("45", 2.68);
        map43.put("64", 0.93);
        map43.put("3", 0.88);
        map43.put("16", 1.25);
        map43.put("10", 2.11);
        hashMap.put("43", map43);

        HashMap<String, Double> map44 = new HashMap<>();
        map44.put("23", 0.97);
        map44.put("58", 1.9);
        map44.put("24", 1.83);
        map44.put("46", 1.57);
        map44.put("21", 1.97);
        hashMap.put("44", map44);

        HashMap<String, Double> map45 = new HashMap<>();
        map45.put("10", 1.12);
        map45.put("43", 2.68);
        map45.put("64", 1.98);
        map45.put("20", 1.86);
        map45.put("9", 0.87);
        map45.put("35", 0.36);
        hashMap.put("45", map45);

        HashMap<String, Double> map46 = new HashMap<>();
        map46.put("2", 1.35);
        map46.put("27", 0.68);
        map46.put("79", 0.89);
        map46.put("1", 1.72);
        map46.put("80", 0.85);
        map46.put("38", 1.85);
        map46.put("58", 2.16);
        map46.put("44", 1.57);
        hashMap.put("46", map46);

        HashMap<String, Double> map47 = new HashMap<>();
        map47.put("73", 1.77);
        map47.put("56", 1.37);
        map47.put("72", 0.69);
        map47.put("21", 0.77);
        map47.put("63", 1.93);
        hashMap.put("47", map47);

        HashMap<String, Double> map48 = new HashMap<>();
        map48.put("7", 2.37);
        map48.put("15", 1.72);
        map48.put("20", 0.92);
        map48.put("9", 0.83);
        hashMap.put("48", map48);

        HashMap<String, Double> map49 = new HashMap<>();
        map49.put("25", 1.07);
        map49.put("4", 1.51);
        map49.put("13", 0.66);
        map49.put("72", 1.23);
        map49.put("21", 1.84);
        map49.put("12", 0.99);
        hashMap.put("49", map49);

        HashMap<String, Double> map50 = new HashMap<>();
        map50.put("38", 0.79);
        map50.put("66", 1.13);
        map50.put("40", 0.68);
        map50.put("68", 0.73);
        map50.put("51", 0.73);
        hashMap.put("50", map50);

        HashMap<String, Double> map51 = new HashMap<>();
        map51.put("50", 0.73);
        map51.put("68", 0.76);
        map51.put("42", 2.2);
        map51.put("33", 1.17);
        map51.put("1", 1.16);
        map51.put("38", 1.1);
        hashMap.put("51", map51);

        HashMap<String, Double> map52 = new HashMap<>();
        map52.put("28", 0.52);
        map52.put("55", 1.58);
        map52.put("60", 1.48);
        map52.put("58", 1.51);
        hashMap.put("52", map52);

        HashMap<String, Double> map53 = new HashMap<>();
        map53.put("25", 1.35);
        map53.put("8", 1.31);
        map53.put("61", 0.81);
        map53.put("69", 0.82);
        hashMap.put("53", map53);

        HashMap<String, Double> map54 = new HashMap<>();
        map54.put("41", 0.58);
        map54.put("81", 0.74);
        map54.put("14", 1.15);
        map54.put("11", 0.74);
        map54.put("16", 1.44);
        hashMap.put("54", map54);

        HashMap<String, Double> map55 = new HashMap<>();
        map55.put("57", 1.39);
        map55.put("19", 1.56);
        map55.put("5", 0.81);
        map55.put("60", 1.0);
        map55.put("52", 1.58);
        hashMap.put("55", map55);

        HashMap<String, Double> map56 = new HashMap<>();
        map56.put("65", 1.56);
        map56.put("73", 0.75);
        map56.put("47", 1.37);
        map56.put("72", 0.82);
        map56.put("13", 0.49);
        hashMap.put("56", map56);

        HashMap<String, Double> map57 = new HashMap<>();
        map57.put("55", 1.39);
        map57.put("19", 1.49);
        map57.put("37", 1.51);
        hashMap.put("57", map57);

        HashMap<String, Double> map58 = new HashMap<>();
        map58.put("52", 1.51);
        map58.put("28", 1.8);
        map58.put("24", 2.48);
        map58.put("44", 1.9);
        map58.put("46", 2.16);
        map58.put("38", 1.84);
        map58.put("66", 2.2);
        map58.put("60", 0.74);
        hashMap.put("58", map58);

        HashMap<String, Double> map59 = new HashMap<>();
        map59.put("22", 1.18);
        map59.put("39", 0.81);
        map59.put("34", 146.0); 
        map59.put("17", 1.38);
        hashMap.put("59", map59);

        HashMap<String, Double> map60 = new HashMap<>();
        map60.put("52", 1.48);
        map60.put("55", 1.0);
        map60.put("5", 0.79);
        map60.put("66", 1.81);
        map60.put("58", 0.74);
        hashMap.put("60", map60);

        HashMap<String, Double> map61 = new HashMap<>();
        map61.put("53", 0.81);
        map61.put("69", 0.9);
        map61.put("29", 0.6);
        map61.put("28", 1.33);
        hashMap.put("61", map61);

        HashMap<String, Double> map62 = new HashMap<>();
        map62.put("24", 0.45);
        map62.put("12", 1.35);
        map62.put("23", 0.66);
        hashMap.put("62", map62);

        HashMap<String, Double> map63 = new HashMap<>();
        map63.put("47", 1.93);
        map63.put("21", 1.62);
        map63.put("2", 0.8);
        map63.put("27", 1.42);
        hashMap.put("63", map63);

        HashMap<String, Double> map64 = new HashMap<>();
        map64.put("43", 0.93);
        map64.put("3", 1.15);
        map64.put("20", 0.96);
        map64.put("45", 1.98);
        hashMap.put("64", map64);

        HashMap<String, Double> map65 = new HashMap<>();
        map65.put("30", 0.96);
        map65.put("73", 1.41);
        map65.put("56", 1.56);
        map65.put("13", 1.29);
        map65.put("4", 1.28);
        hashMap.put("65", map65);

        HashMap<String, Double> map66 = new HashMap<>();
        map66.put("60", 1.81);
        map66.put("58", 2.2);
        map66.put("38", 1.27);
        map66.put("50", 1.13);
        map66.put("40", 0.93);
        map66.put("71", 1.3);
        map66.put("19", 0.75);
        map66.put("5", 1.32);
        hashMap.put("66", map66);

        HashMap<String, Double> map67 = new HashMap<>();
        map67.put("78", 0.86);
        map67.put("74", 0.67);
        map67.put("14", 0.91);
        map67.put("81", 0.89);
        hashMap.put("67", map67);

        HashMap<String, Double> map68 = new HashMap<>();
        map68.put("6", 1.95);
        map68.put("42", 1.63);
        map68.put("40", 0.79);
        map68.put("50", 0.73);
        map68.put("51", 0.76);
        hashMap.put("68", map68);

        HashMap<String, Double> map69 = new HashMap<>();
        map69.put("25", 1.1);
        map69.put("53", 0.82);
        map69.put("61", 0.9);
        map69.put("29", 0.74);
        map69.put("24", 0.88);
        hashMap.put("69", map69);

        HashMap<String, Double> map70 = new HashMap<>();
        map70.put("42", 1.02);
        map70.put("33", 1.45);
        map70.put("7", 2.54);
        hashMap.put("70", map70);
        
        HashMap<String, Double> map71 = new HashMap<>();
        map71.put("19", 1.6);
        map71.put("66", 1.3);
        map71.put("40", 0.96);
        map71.put("6", 0.67);
        map71.put("18", 0.76);
        hashMap.put("71", map71);

        HashMap<String, Double> map72 = new HashMap<>();
        map72.put("56", 0.82);
        map72.put("13", 1.11);
        map72.put("49", 1.23);
        map72.put("21", 0.91);
        map72.put("47", 0.69);
        hashMap.put("72", map72);

        HashMap<String, Double> map73 = new HashMap<>();
        map73.put("56", 0.75);
        map73.put("65", 1.41);
        map73.put("30", 1.25);
        map73.put("47", 1.77);
        hashMap.put("73", map73);

        HashMap<String, Double> map74 = new HashMap<>();
        map74.put("78", 0.41);
        map74.put("37", 1.34);
        map74.put("67", 0.67);
        hashMap.put("74", map74);

        HashMap<String, Double> map75 = new HashMap<>();
        map75.put("25", 1.88);
        map75.put("36", 0.63);
        map75.put("8", 0.89);
        hashMap.put("75", map75);

        HashMap<String, Double> map76 = new HashMap<>();
        map76.put("4", 0.97);
        map76.put("36", 1.16);
        hashMap.put("76", map76);

        HashMap<String, Double> map77 = new HashMap<>();
        map77.put("41", 0.65);
        map77.put("16", 0.43);
        hashMap.put("77", map77);

        HashMap<String, Double> map78 = new HashMap<>();
        map78.put("74", 0.41);
        map78.put("37", 1.18);
        map78.put("18", 1.16);
        map78.put("67", 0.86);
        hashMap.put("78", map78);

        HashMap<String, Double> map79 = new HashMap<>();
        map79.put("27", 0.44);
        map79.put("31", 0.83);
        hashMap.put("79", map79);

        HashMap<String, Double> map80 = new HashMap<>();
        map80.put("27", 1.22);
        map80.put("46", 0.85);
        map80.put("1", 0.88);
        map80.put("31", 0.83);
        hashMap.put("80", map80);

        HashMap<String, Double> map81 = new HashMap<>();
        map81.put("67", 0.89);
        map81.put("14", 0.5);
        map81.put("54", 0.74);
        hashMap.put("81", map81);
        
        Graph trGraph= new Graph(hashMap);

        trGraph.Dijkstra("35", "7");


    }
    
}

class Graph{

    private  HashMap<String, HashMap<String, Double>> adjVertices = new HashMap<>();
    private  Set<String> visitedNodes = new HashSet<>();
    private  Map<String, Double> distance = new HashMap<>();
    private  Map<String, String> previousNode = new HashMap<>();

    public Set<String> getVisitedNodes() {
        return visitedNodes;
    }

    public Map<String, Double> getDistance() {
        return distance;
    }

    public Graph(HashMap<String, HashMap<String, Double>> adjVertices) {
        this.adjVertices = adjVertices;
    }

    public void Dijkstra(String start,String finish){

        for (String node : adjVertices.keySet()) {
            if (node==start) {
                distance.put(node, 0.00);
            } else {
                distance.put(node, Double.MAX_VALUE);
            }
            previousNode.put(node, null);
        }

        while (!visitedNodes.contains(finish)) {
            String currentNode = getNodeWithShortestDistance();
            visitedNodes.add(currentNode);

            Map<String, Double> neighbors = adjVertices.get(currentNode);
            for (String neighbor : neighbors.keySet()) {
                double cost = neighbors.get(neighbor);
                double totalCost = cost + distance.get(currentNode);
                if (totalCost < distance.get(neighbor)) {
                    distance.put(neighbor, totalCost);
                    previousNode.put(neighbor, currentNode);
                }
            }
        }

        System.out.println("En kısa yol: " + getShortestPath(finish));
        System.out.println("Maliyet: " + distance.get(finish)*100);
    }

    private  String getNodeWithShortestDistance() {
        String result = null;
        double shortestDistance = Double.MAX_VALUE;
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