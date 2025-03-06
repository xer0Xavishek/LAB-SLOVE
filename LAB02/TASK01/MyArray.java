public class MyArray
{
  int arr[]=new int[10];
  public MyArray(int a[])
  {
    for(int c=0; c<a.length; c++)
    {
      arr[c]=a[c];
    }
  }
  public void insertionSort()
  {
    for(int c=1; c<arr.length; c++)
    {
      int key=arr[c];
      int i=c-1;
      while(i>0 && arr[i]>key)
      {
        arr[i+1]=arr[i];
        arr[i]=key;
        i--;
      }
    }
  }
  void mergeSort(int arr[], int l, int r) 
  { 
    if(l < r) 
    {
      int mid=(l+r)/2;
      mergeSort(arr,l,mid); 
      mergeSort(arr,mid+1,r);
      merge(arr, l, mid, r); 
    } 
  }
  void merge(int arr[], int l, int mid, int r) 
  { 
    int n1=mid-l+1; 
    int n2=r-mid;
    int left[]=new int[n1]; 
    int right[]=new int[n2];
    for(int i=0; i<n1; ++i)
    {
      left[i]=arr[l+i]; 
    }
    for(int j=0; j<n2; ++j) 
    {
      right[j]=arr[mid+1+j];
    }
    int i=0,j=0,k=l; 
    while(i<n1&&j<n2) 
    { 
      if(left[i]<=right[j]) 
      { 
        arr[k]=left[i]; 
        i++; 
      } 
      else
      { 
        arr[k]=right[j]; 
        j++; 
      } 
      k++; 
    }
    while (i<n1) 
    { 
      arr[k]=left[i]; 
      i++; 
      k++; 
    }
    while (j<n2) 
    { 
      arr[k]=right[j]; 
      j++; 
      k++; 
    } 
  }
  public void quickSort(int arr[], int low, int high) 
  { 
    if(low<high) 
    {
      int pi=partition(arr,low,high);
      quickSort(arr,low,pi-1); 
      quickSort(arr,pi+1,high); 
    } 
  } 
  public int partition(int arr[], int low, int high) 
  { 
    int pivot = arr[high];  
    int i = (low-1);
    for (int j=low; j<high; j++) 
    {
      if (arr[j]<=pivot) 
      { 
        i++;
        int temp=arr[i]; 
        arr[i]=arr[j]; 
        arr[j]=temp; 
      } 
    }
    int temp=arr[i+1]; 
    arr[i+1]=arr[high]; 
    arr[high]=temp;
    return i+1; 
  } 
  public String toString()
  {
    return arr[0]+" "+arr[1]+" "+arr[2]+" "+arr[3]+" "+arr[4]+" "+arr[5]+" "+arr[6]+" "+arr[7]+" "+arr[8]+" "+arr[9];
  }
}