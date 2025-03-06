import java.util.Scanner;
import java.io.*;
import java.util.*; 
public class MST
{
  public static void main(String [] args)
  {
    try
    {
      Scanner sc = new Scanner(new File("graph.txt"));
      int n=sc.nextInt();
      String cities[]=new String[n+1];
      for(int c=1; c<=n; c++)
      {
        cities[c]=sc.next();
      }
      int adj[][]=new int[n+1][n+1];
      int counter=1;
      while(sc.hasNextInt())
      {
        adj[counter][1]=sc.nextInt();
        adj[counter][2]=sc.nextInt();
        adj[counter][3]=sc.nextInt();
        counter++;
      }
      Kruskal a=new Kruskal(adj,1,cities);
    }
    catch(IOException e)
    {
      System.out.println(e);
    }
  }
}