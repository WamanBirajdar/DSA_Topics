/*
Given an array of positive integers. 
All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.
*/

package Array;

public class getOddOccurence {
	static int OddOccurence(int arr[],int n)
	{
		int count=0;
		int i;
		for(i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(arr[i]==arr[j])
				{
					count++;
				}
			}
			if(count%2!=0)
			{
				return arr[i];
			}
		}
		return -1;
		
	}

	public static void main(String[] args) {
		int arr[] = { 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 };
		int n=arr.length;
	
		System.out.println(OddOccurence(arr,n));
		

	}

}
