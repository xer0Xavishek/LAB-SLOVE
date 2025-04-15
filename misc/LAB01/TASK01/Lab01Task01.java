import java.util.Scanner;
import java.io.*;

public class Lab01Task01
{
  public static void main(String[] args)
  {
    //int[][] adjacencyMatrix = null;
    
    try
    {
      Scanner sc = new Scanner(new File("input.txt"));
      int vertex=0, edge=0, vertex1=0;
      vertex1 = sc.nextInt();
      edge = sc.nextInt();
      int adjacencyMatrix[][]=new int[vertex1][vertex1];
      
      while(sc.hasNextInt())
      {
        vertex = sc.nextInt();
        edge = sc.nextInt();
        
        adjacencyMatrix[vertex][edge]=1;
        
        //write remaining code here
      }
      for(int c=0; c<vertex1; c++)
      {
        for(int c2=0; c2<vertex1; c2++)
        {
          System.out.print(adjacencyMatrix[c][c2]+" ");
        }
        System.out.println();
      }
    }
    catch(IOException e)
    {
      System.out.println(e);
    }
  }
}