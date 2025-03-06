import java.io.*;
import java.util.*;
public class Kruskal
{
  int [] set;
  int visited[];
  boolean path[];
  public Kruskal(int adj[][], int start, String cities[])
  {
    set=new int[adj.length];
    int size=1;
    int min=0, cnt=0, idx1=0, idx2=0;
    for(int i=1; i<adj.length; i++)
    {
      for(int c=1; c<adj.length; c++)
      {
        for(int c1=1; c1<adj.length; c1++)
        {
          if(adj[c][c1]!=0 && cnt==0)
          {
            idx1=c;
            idx2=c1;
            min=adj[c][c1];
            cnt++;
          }
          else if(adj[c][c1]!=0 && cnt!=0)
          {
            if(adj[c][c1]<min)
            {
              min=adj[c][c1];
              idx1=c;
              idx2=c1;
            }
          }
        }
      }
      if(size<set.length)
      {
        int disC1=0, disC2=0;
        for(int k=1; k<set.length; k++)
        {
          if(set[k]==idx2)
          {
            disC1++;
          }
          if(set[k]==idx1)
          {
            disC2++;
          }
        }
        if(disC1==0)
        {
          set[size]=idx2;
          size++;
        }
        if(disC2==0)
        {
          set[size]=idx1;
          size++;
        }
      }
      adj[idx1][idx2]=100000;
      adj[idx2][idx1]=100000;
      min=0;
      cnt=0;
      idx1=0;
      idx2=0;
    }
    System.out.println("Shortest Path:");
    for(int c=1; c<adj.length; c++)
    {
      
        System.out.print(cities[set[c]]+" --> ");
      
    }
    System.out.println();
    
  }
}