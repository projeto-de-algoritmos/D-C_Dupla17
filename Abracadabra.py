# https://codeforces.com/contest/161/problem/C

#include  <bits/stdc++.h>
# using namespace std;

# typedef long long ll;

# int deal(int l1,int r1,int l2,int r2,int k)//区间长度2^k
# {
    
    
#     if(l1>r1||l2>r2)    return 0;
#     if(l1>l2)   {
    
#     swap(l1,l2);swap(r1,r2);}//把第一个区间放左边
#     if(r2<=r1)  return r2-l2+1;//如果第二个区间包含在第一个区间内
#     if(l1==l2)  return r1-l1+1;//第一个区间包含在第二个区间内
#     int len=1<<k;//k从30开始，保证两个区间变换后左端点一定在左半边
#     if(l2>len)  return deal(l1,r1,l2-len,r2-len,k);//左移
#     if(r1<len && r2<len ) return deal(l1,r1,l2,r2,k-1);//都在左半边，区间减半
#     int ans=max(deal(l1,r1,l2,len-1,k),deal(l1,r1,1,r2-len,k));//分治，l1,l2在左半边，r1r2在右半边
#     return max(r1-l2+1,ans);//最大值要么是重叠的部分，要么是分治之后其中一边的最大值
# }
# int main()
# {
    
    
#     ios::sync_with_stdio(false);

#     int l1,l2,r1,r2;
#     cin>>l1>>r1>>l2>>r2;
#     cout<<deal(l1,r1,l2,r2,30)<<endl;
# }


def abracadabra(l1, r1, l2, r2, k):
    if l1 > r1 or l2 > r2:
        return 0
    if l1 > l2:
        l1, l2 = l2, l1
        r1, r2 = r2, r1
    if r2 <= r1:
        return r2 - l2 + 1
    if l1 == l2:
        return r1 - l1 + 1
    len = 1 << k
    if l2 > len:
        return abracadabra(l1, r1, l2 - len, r2 - len, k)
    if r1 < len and r2 < len:
        return abracadabra(l1, r1, l2, r2, k - 1)
    ans = max(abracadabra(l1, r1, l2, len - 1, k), abracadabra(l1, r1, 1, r2 - len, k))
    return max(r1 - l2 + 1, ans)


l1, r1, l2,r2 = list(map(int, input().split()))
print(abracadabra(l1, r1, l2, r2, 30))
































# l1, r1, l2,r2 = list(map(int, input().split()))

# ans = 0


# def abracadabra(l1, r1, l2, r2, l):
#    global ans

#    if l1 > r1 or l2 > r2 or not l:
#        return
  
#    ans = max(ans, min(r1-l2, r1-l1, r2-l1, r2-l2) + 1)
#    if r1-l1 < ans or r2-l2 < ans:
#        return
  
#    mid = 1 << (l-1)
#    print(mid)
#    abracadabra(l1, min(r1, mid-1), l2, min(r2, mid-1), l-1)
#    abracadabra(l1, min(r1, mid-1), max(1, l2-mid), r2-mid, l-1)
#    abracadabra(max(1, l1-mid), r1-mid, l2, min(r2, mid-1), l-1)
#    abracadabra(max(1, l1-mid), r1-mid, max(l2-mid, 1), r2-mid, l-1)
 

# abracadabra(l1, r1, l2, r2, 30)
# print(ans)





































# def abracadabra(l1, r1, l2, r2, ans, k):
#   if l1 > r1 or l2 > r2 or k == 0:
#     return
 
#   len_ans = ans[0]
#   ans[0] = max(len_ans, min(r1-l2, r1-l1, r2-l1, r2-l2) + 1)
 
#   if r1 - l1 < len_ans or r2 - l2 < len_ans:
#     return
 
#   size = pow(2, k - 1)
#   abracadabra(l1, min(r1, size - 1), l2, min(r2, size - 1), ans, k-1)
#   abracadabra(l1, min(r1, size - 1), max(1, l2 - size), r2 - size, ans, k-1)
#   abracadabra(max(1, l1 - size), r1 - size, l2, min(r2, size - 1), ans, k-1)
#   abracadabra(max(1, l1 - size), r1 - size, max(1, l2 - size), r2 - size, ans, k-1)
 
# l1, r1, l2, r2 = list(map(int, input().split()))
# ans = [0]
# abracadabra(l1, r1, l2, r2, ans, 30)
# print(ans[0])
