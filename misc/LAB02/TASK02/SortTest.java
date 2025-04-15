public class SortTest
{
  public static void main(String [] args)
  {
    int arr[]={3, 5 , 10, 23, 25, 8, 7, 9, 50, 47};
    MyArray a=new MyArray(arr);
    long x=(System.nanoTime());
    a.insertionSort();
    long y=System.nanoTime();
    System.out.println(a);
    System.out.println("Current time nano: "+(y-x));
    MyArray b=new MyArray(arr);
    x=(System.nanoTime());
    b.mergeSort(b.arr,0,b.arr.length-1);
    y=System.nanoTime();
    System.out.println(b);
    System.out.println("Current time nano: "+(y-x));
    MyArray c=new MyArray(arr);
    x=(System.nanoTime());
    c.quickSort(c.arr,0,c.arr.length-1);
    y=System.nanoTime();
    System.out.println(c);
    System.out.println("Current time nano: "+(y-x));
  }
}