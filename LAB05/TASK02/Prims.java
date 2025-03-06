import java.io.*;
import java.util.*;
public class Prims
{
  int [] distance;
  int visited[];
  boolean path[];
  public Prims(int adj[][], int start, String cities[])
  {
    distance=new int[adj.length];
    for(int c=1; c<adj.length; c++)
    {
      distance[c]=100000;
    }
    visited=new int[adj.length];
    path=new boolean[adj.length];
    LinkedList<Integer> queue = new LinkedList<Integer>(); 
    visited[start]=1;
    distance[start]=0;
    queue.add(start);
    path[start]=true;
    while (queue.size() != 0) 
    { 
      int u = queue.poll();
      int min=0, cnt=0;
      for(int c=1; c<adj.length; c++)
      {
        if(adj[u][c]!=0 && cnt==0 && visited[c]==0)
        {
          min=c;
          cnt++;
          if(distance[c]>adj[u][c])
          {
            distance[c]=adj[u][c];
          }
        }
        else if(adj[u][c]!=0 && cnt!=0 && visited[c]==0)
        {
          if(adj[u][c]<adj[u][min])
          {
            min=c;
            if(distance[c]>adj[u][c])
            {
              distance[c]=adj[u][c];
            }
          }
        }
        else
        {
          if(distance[c]>adj[u][c])
          {
            distance[c]=adj[u][c];
          }
        }
      }
      if(min!=0)
      {
        visited[min]=1;
        path[min]=true;
        queue.add(min);
      }
    }
    System.out.println("Shortest Path:");
    for(int c=1; c<adj.length; c++)
    {
      if(path[c]==true)
      {
        System.out.print(cities[c]+" --> ");
      }
    }
    System.out.println();
    
  }
}