/*
Given an array A[] of n numbers 
and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x.
*/

package Array;

import java.util.*;

class sum{
	
	boolean checkAdd(int A[],int size,int X)
	{
		for(int i=0;i<(size-1);i++)
		{
			for(int j=(i+1);j<size;j++)
			{
				if(A[i]+A[j]==X)
				{
					return true;
				}
			}
		}
		return false;
	}
	
	
	
}

public class given_sum {

	public static void main(String[] args) {
		sum s=new sum();
	

		int A[]= {0,-1,2,-3,1};
		int x=-2;
		int size=A.length;
		
		
		if(s.checkAdd(A, size, x))
		{
			System.out.println("yes");
		}
		else {
			System.out.println("no");
		}

	}

}
