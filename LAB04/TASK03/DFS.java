import java.io.*;
import java.util.*;
public class DFS
{
  int [] d;
  int [] f;
  int visited[];
  int time;
  int index[];
  public static int counter=1;
  public DFS(int adj[][], int start)
  {
    d=new int[adj.length];
    f=new int[adj.length];
    index=new int[adj.length];
    visited=new int[adj.length];
    time=0;
    for(int c=1; c<adj.length; c++)
    {
      DFS_Visit(adj,c);
    }
    System.out.println();
  }
  public void DFS_Visit(int adj[][],int start)
  {
    if(visited[start]==0)
    {
      visited[start]=1;
      System.out.print(start+"-->");
      if(start==9)
      {
        for(int c=1; c<visited.length; c++)
        {
          visited[c]=1;
        }
      }
    }
    time++;
    d[start]=time;
    for(int c=1; c<adj.length; c++)
    {
      if(adj[start][c]==1)
      {
        if(visited[c]==0)
        {
          DFS_Visit(adj,c);
        }
      }
    }
    if(f[start]==0)
    {
      f[start]=time+1;
      index[counter]=start;
      counter++;
    }
  }
}