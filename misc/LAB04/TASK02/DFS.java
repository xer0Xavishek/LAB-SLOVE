import java.io.*;
import java.util.*;
public class DFS
{
  int [] f;
  int [] top;
  int visited[];
  int time;
  int index2[];
  public static int counter2=1;
  public static int counter3=1;
  public DFS(int adj[][], int start)
  {
    f=new int[adj.length];
    top=new int[adj.length];
    index2=new int[adj.length];
    visited=new int[adj.length];
    time=0;
    System.out.println("After Topological Sort: Nodes: ");
    for(int c=1; c<adj.length; c++)
    {
      DFS_Visit(adj,c);
    }
    for(int c=adj.length-1; c>0; c--)
    {
      System.out.print((top[c])+"-->");
    }
    System.out.println();
    System.out.println("Finishing times:");
    for(int c=adj.length-1; c>0; c--)
    {
      System.out.print((f[index2[c]])+" ");
    }
  }
  public void DFS_Visit(int adj[][],int start)
  {
    if(visited[start]==0)
    {
      visited[start]=1;
      time++;
    }
    
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
      time++;
      f[start]=time;
      index2[counter2]=start;
      top[counter3]=start;
      counter3++;
      counter2++;
    }
  }
}