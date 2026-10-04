#include <iostream>
#include <string>
#include <stack>
#include <deque>
#include <algorithm>
#include <queue>
using namespace std;
/*int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        queue<char> q;
        int cnt[26]={};
        for(int i=0;i<n;i++){
            char a;
            cin>>a;
            cnt[a-'a']++;
            q.push(a);
            while(!q.empty() && cnt[q.front()-'a']>1){
                q.pop();
            }
            if(q.empty()){
                cout<<"-1 ";
            }
            else{
                cout<<q.front()<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        int a;
        cin>>a;
        if(a%2!=0){
            cout<<a<<" ";
        }
    }
    return 0;
}
int main(){
    int n;
    cin>>n;
    vector<string> st;
    string pr;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        if(i==0 || pr!=s){
            st.push_back(s);
        }
        pr=s;
    }
    cout<<st.size()<<endl;
    for(int i=0;i<st.size();i++){
        cout<<st[i]<<endl;
    }
    return 0;
}
 int main(){
    int n;
    cin>>n;
    int a[10000];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=n-1;i>=0;i--){
        cout<<a[i]<<" ";
    }
    return 0;
 }
int main(){
    int n;
    cin>>n;
    int a[10000];
    int b=n/2;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        if(i==b){
            continue;
        }
        cout<<a[i]<<" ";
    }
    return 0;
}

int main(){
    int n;
    cin>>n;
    int a[10000];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int m; 
    cin>>m;
    int b[10000];
    for(int i=0;i<m;i++){
        cin>>b[i];
    }
    int i=0,j=0;
    while(n>1 && m>i){
        if(a[i]<=b[j]){
            cout<<a[i]<<" ";
            i++;
        }
        else{
            cout<<b[j]<<" ";
            j++;
        }
    }
    while(n>i){
        cout<<a[i]<<" ";
        i++;
    }
    while(m>j){
        cout<<b[j]<<" ";
        j++;
    }
    return 0;
}

int main(){
    int n,m;
    cin>>n>>m;
    vector<string> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=m;i<n;i++){
        cout<<a[i]<<" ";
    }
    for(int i=0;i<m;i++){
        cout<<a[i]<<" ";
    }
    return 0;
}

int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int current=a[0];
    int best=a[0];
    for(int i=1;i<n;i++){
        if(current+a[i]>a[i]){
            current+=a[i];
        }
        else{
            current =a[i];
        }
        if(current>best){
            best=current;
        }
    }
    cout<<best;
    return 0;
}

int main(){
    string command;
    deque<string> q;
    string a,b;
    while(cin>>command){
        if(command=="add_front"){
            cin>>a;
            q.push_front(a);
            cout<<"ok"<<endl;
        }
        else if(command=="add_back"){
            cin>>b;
            q.push_back(b);
            cout<<"ok"<<endl;
        }
        else if(command=="erase_front"){
            if(!q.empty()){
                cout<<q.front()<<endl;
                q.pop_front();
            }
            else{
                cout<<"error"<<endl;
            }
        }
        else if(command=="erase_back"){
            if(!q.empty()){
                cout<<q.back()<<endl;
                q.pop_back();
            }
            else{
                cout<<"error"<<endl;
            }
        }
        else if(command=="front"){
            if(!q.empty()){
                cout<<q.front()<<endl;
            }
            else{
                cout<<"error"<<endl;
            }
        }
        else if(command=="back"){
            if(!q.empty()){
                cout<<q.back()<<endl;
            }
            else{
                cout<<"error"<<endl;
            }
        }
        else if(command=="clear"){
            q.clear();
            cout<<"ok"<<endl;
        }
        else if(command=="exit"){
            cout<<"goodbye";
            break;
        }
    }
    return 0;
}
    int main(){
        deque<int> q;
        int command;
        while(cin>>command){
            if(command ==0){
                break;
            }
            else if(command ==1){
                int x,p;
                cin>>x>>p;
                q.insert(q.begin()+p,x);
            }
            else if(command==2){
                int p;
                cin>>p;
                q.erase(q.begin()+p);
            }
            else if(command==3){
                if(q.empty()){
                    cout<<"-1"<<endl;
                }
                else{
                    for(int i=0;i<q.size();i++){
                        cout<<q[i]<<" ";
                    }
                    cout<<endl;
                }
            }
            else if(command==4){
                int p1,p2;
                cin>>p1>>p2;
                int x=q[p1];
                q.erase(q.begin()+p1);
                q.insert(q.begin()+p2,x);
            }
            else if(command==5){
                reverse(q.begin(),q.end());
            }
            else if(command ==6){
                int x;
                cin>>x;
                for(int i=0;i<x;i++){
                    int w=q.front();
                    q.pop_front();
                    q.push_back(w);
                }
            }
            else if(command ==7){
                int x;
                cin>>x;
                for(int i=0;i<x;i++){
                    int a=q.back();
                    q.pop_back();
                    q.push_front(a);
                }
            }
        }
        return 0;
    }*/
int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a.begin(),a.end());
    vector<long long> prefix(n);
    prefix[0]=a[0];
    for(int i=1;i<n;i++){
        prefix[i]=prefix[i-1]+a[i];}
    int rounds;
    cin>>rounds;
    while(rounds--){
        int power;
        cin>>power;
        int count=upper_bound(a.begin(),a.end(),power)-a.begin();
        long long sum=0;
        if(count>0){
            sum=prefix[count-1];
            }
            cout<<count<<" "<<sum<<endl;
    }
    return 0;
}