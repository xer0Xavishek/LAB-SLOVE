import java.util.Scanner;
import java.io.File;

public class MergeSort
{
  static int[] arr;
  
  public static void main(String[] args)
  {
    input("input.txt");
    
    display(arr);
    
    mergeSort(arr, 0, arr.length-1);
    
    System.out.println();
    
    display(arr);
  }
  
  private static void input(String fileName)
  {
    int i=0;
    try{
      Scanner sc = new Scanner(new File(fileName));
      int total = sc.nextInt();
      arr = new int[total];
      
      while(sc.hasNext()){
        arr[i] = sc.nextInt();
        i++;
      }
    }catch(Exception e){
      System.out.println("File not found!");
    }
  }
  
  private static void display(int[] arr)
  {
    for(int i=0;i<arr.length;i++)
    {
      System.out.println(arr[i]);
    }
  }
  
  private static void mergeSort(int[] arr, int l, int h)
  {
    if(l<h){
      int m = (l+h)/2;
    
      mergeSort(arr, l, m);
      mergeSort(arr, m+1, h);
      merge(arr, l, m, h);
    }
  }
  
  private static void merge(int[] arr, int l, int m, int h)
  {
    int i, j, k;
    int n1 = m-l+1;
    int n2 = h-m;
    
    int[] left = new int[n1];
    int[] right = new int[n2];
    
    //copy left
    for(i=0;i<n1;i++)
    {
     left[i] = arr[l+i]; 
    }
    
    //copy right
    for(j=0;j<n2;j++)
    {
     right[j] = arr[m+1+j]; 
    }
            
    i = 0;
    j = 0;
    k = l;
    
    while(i<n1 && j<n2){
     if(left[i]<=right[j]){
       arr[k] = left[i];
       i++;
     }else{
       arr[k] = right[j];
       j++;
     }
     k++;
    }
    
    while(i<n1){
      arr[k] = left[i];
      i++;
      k++;
    }
    
    while(j<n2){
      arr[k] = right[j];
      j++;
      k++;
    }
  }
}