import java.util.Scanner;
import java.io.*;
import java.util.*; 
public class Tester
{
  public static void main(String [] args)
  {
    
    try
    {
      Scanner sc = new Scanner(new File("maldives.txt"));
      int test=sc.nextInt();
      for(int t=1; t<=test; t++)
      {
        int vertex=0, edge=0;
        int v=sc.nextInt();
        int adj[][]=new int[v+1][v+1];
        int n=sc.nextInt();
        for(int c=1; c<=n; c++)
        {
          vertex = sc.nextInt();
          edge = sc.nextInt();
          adj[vertex][edge]=1;
          adj[edge][vertex]=1;
        }
        System.out.println("Test Case: "+t);
        BridgeFinder c = new BridgeFinder(adj, v);
      }
    }
    catch(IOException e)
    {
      System.out.println(e);
    }
  }
}