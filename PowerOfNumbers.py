# https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1/?page=1&category[]=Divide%20and%20Conquer&sortBy=submissions#

#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        if N == 0:
            return 0
        
        if R == 0:
            return 1
            
        y = 0
        
        if R % 2 == 0:
            y = self.power(N, R / 2)
            y = (y * y) % 1000000007
        
        else:
            y = N % 1000000007
            y = (y * self.power(N, R - 1) % 1000000007) % 1000000007
            
        return ((y + 1000000007) % 1000000007)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends