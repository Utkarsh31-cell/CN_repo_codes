#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
       // priority_queue<int,vector<int>,greater<int>>pq;//min heap // priority queue
       priority_queue<int>pq; //max heap 
       queue<int>q;
        int a[n],i,j,cnt=0;
        for(int i=0;i<n;i++){
            cin>>a[i];
            pq.push(a[i]);
            q.push(i);
        }
        cin>>j;
        //simply do the same whatever quesion wants from us 
        while(1){
           if(a[q.front()]==pq.top()&&q.front()==j){
               cnt+=1;
               break;
           }
           if(a[q.front()]==pq.top()){
               cnt+=1;
               pq.pop();
               q.pop();
           }else{
               q.push(q.front());
               q.pop();
           }
        }
       
        cout<<cnt<<"\n";
    }
    return 0;
}
/*
2
3
3 9 4
2
5
2 3 2 2 4
3

output:
2
4
*/
