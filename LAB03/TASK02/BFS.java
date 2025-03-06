import java.io.*;
import java.util.*;
public class BFS
{
  int [] distance;
  int visited[];
  boolean path[];
  public BFS(int adj[][], int start)
  {
    distance=new int[adj.length];
    visited=new int[adj.length];
    LinkedList<Integer> queue = new LinkedList<Integer>(); 
    visited[start]=1;
    distance[start]=0;
    queue.add(start);
    while (queue.size() != 0) 
    { 
      int s = queue.poll(); 
      System.out.print(s+" distance from source "+distance[s]+", path-> ");
      int path[]=new int[adj.length];
      if(s==1)
      {
        System.out.print("1");
      }
      else
      {
        int y=s-1,x=s;
        pathFinder(adj, y, x, path);
        for(int c=1; c<path.length; c++)
        {
          if(path[c]==1)
          {
            System.out.print(c+" --> ");
          }
        }
        System.out.print(s);
      }
      System.out.println();
      path=new int[adj.length];
      for(int i=1; i<adj.length; i++)
      {
        if(adj[s][i]!=0)
        {
          int n = i;
          if (visited[n]==0)
          { 
            visited[n] = 1;
            distance[n]=distance[s]+1;
            queue.add(n);
          }
        }
      }
      visited[s]=2;
    }
  }
  public void pathFinder(int adj[][], int i, int j, int path[])
  {
    if(!checkLevel(adj,i,j))
    {
      if(adj[i][j]==1)
      {
        path[i]=1;
        if(i>0)
        {
          j=i;
          i--;
          pathFinder(adj, i, j, path);
        }
      }
    }
    if(i>0)
    {
      i--;
      pathFinder(adj, i, j, path);
    }
  }
  public boolean checkLevel(int adj[][], int i, int j)
  {
    if(j==adj.length-1)
      return false;
    for(int c=1; c<i; c++)
    {
      if(adj[c][i]==adj[c][j])
      {
        return true;
      }
    }
    return false;
  }
}