import java.util.Scanner;
import java.io.*;
import java.util.*; 
public class Graph
{
  public static void main(String [] args)
  {
    
    try
    {
      Scanner sc = new Scanner(new File("graph.txt"));
      
      int vertex=0, edge=0;
      int v=sc.nextInt();
      int adj[][]=new int[v+1][v+1];
      while(sc.hasNextInt())
      {
        vertex = sc.nextInt();
        edge = sc.nextInt();
        adj[vertex][edge]=1;
      }
      BFS c = new BFS(adj, 1);
    }
    catch(IOException e)
    {
      System.out.println(e);
    }
  }
}