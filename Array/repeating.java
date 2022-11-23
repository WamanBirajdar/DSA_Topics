/*
Given an array arr[] of N+2 elements. All elements of the array are in the range of 1 to N. 
And all elements occur once except two numbers which occur twice. Find the two repeating numbers. 
*/

package Array;

public class printRepeating {
	
	static void RepeatNumber(int arr[],int size)
	{
		int i,j;
		System.out.print("Repeating numbers are: ");
		for(i=0;i<size-1;i++)
		{
			for(j=i+1;j<size;j++)
			{
				if(arr[i]==arr[j])
				{
					System.out.print(arr[i]+"  ");
				}
						
			}
		}
	}

	public static void main(String[] args) {
		int arr[] = { 4, 2, 4, 5, 2, 3, 1 };
		int n=arr.length;
		
		RepeatNumber(arr,n);
		
	}

}
