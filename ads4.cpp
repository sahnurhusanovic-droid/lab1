#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

                                    /*A
struct Node{
    int value;
    int left;
    int right;
};
int main(){
    int N,M;
    cin>>N>>M;
    vector<Node> tree;
    tree.reserve(N);
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<=tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    for(int i=0;i<M;i++){
        string path;
        cin>>path;
        int cur=0;
        bool exists=true;
        for(char direction : path){
            if(direction=='L'){
                cur=tree[cur].left;
            }
            else{
                cur=tree[cur].right;
            }
            if(cur==-1){
                exists=false;
                break;
            }
        }
        if(exists){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}*/


/*                                    B
struct Node{
    int value;
    int left;
    int right;
};
int countsubtree(vector<Node>& tree, int cur){
    if(cur==-1){
        return 0;
    }
    return 1+countsubtree(tree,tree[cur].left)+countsubtree(tree,tree[cur].right);
}
int main(){
    int N;
    cin>>N;
    vector<Node> tree;
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    int X;
    cin>>X;
    int cur=0;
    while(X!=tree[cur].value){
        if(X<tree[cur].value){
            cur=tree[cur].left;
        }
        else{
            cur=tree[cur].right;
        }
    }
    cout<<countsubtree(tree,cur)<<endl;
    return 0;
}*/


/*                                    C
struct Node{
    int value;
    int left;
    int right;
};
int preorder(vector<Node>& tree, int cur){
    if(cur==-1){
        return 0;
    }
    cout<<tree[cur].value<<" ";
    return 1+preorder(tree,tree[cur].left)+preorder(tree,tree[cur].right);
}
int main(){
    int n;
    cin>>n;
    vector<Node> tree;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    int X;
    cin>>X;
    int cur=0;
    while(X!=tree[cur].value){
        if(X<tree[cur].value){
            cur=tree[cur].left;
        }
        else{
            cur=tree[cur].right;
        }
    }
    preorder(tree,cur);
    return 0;
}*/


/*                                    D
struct Node{
    int value;
    int left;
    int right;
    int level;
};
int main(){
    int n;
    cin>>n;
    vector<Node> tree;
    vector<int> sum(n,0);
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1,0});
            sum[0]+=x;
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        int level=tree[cur].level+1;
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1,level});
                        if(level>=(int)sum.size()){
                            sum.push_back(0);
                        }
                        sum[level]+=x;
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        int level=tree[cur].level+1;
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1,level});
                        if(level>=(int)sum.size()){
                            sum.push_back(0);
                        }
                        sum[level]+=x;
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    int levels=0;
    for(int i=0;i<n;i++){
        if(sum[i] != 0){
            levels++;
        }
    }
    cout<<levels<<endl;

    for(int i=0;i<levels;i++){
        cout<<sum[i]<<" ";
    }
    return 0;
}*/


/*                                    E
struct Node{
    int left=0;
    int right=0;
};
int main(){
    int n;
    cin>>n;
    vector<Node> tree(n+1);
    for(int i=0;i<n-1;i++){
        int x,y,z;
        cin>>x>>y>>z;
        if(z==0){
            tree[x].left=y;
        }
        else{
            tree[x].right=y;
        }
    }
    queue<int> q;
    q.push(1);
    int ans=0;
    while(!q.empty()){
        int sz=q.size();
        if(sz>ans){
            ans=sz;
        }
        for(int i=0;i<sz;i++){
            int v=q.front();
            q.pop();
            if(tree[v].left!=0){
                q.push(tree[v].left);
            }
            if(tree[v].right!=0){
                q.push(tree[v].right);
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}*/


/*                                    F
struct Node{
    int value;
    int left;
    int right;
};
int main(){
    int N;
    cin>>N;
    vector<Node> tree;
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    int ans=0;
    for(int i=0;i<tree.size();i++){
        if(tree[i].left!=-1 && tree[i].right!=-1){
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}*/


/*                                    G
struct Node{
    int value;
    int left;
    int right;
};
int ans=0;
int height(vector<Node>& tree, int cur){
    if(cur==-1){
        return 0;
    }
    int L=height(tree,tree[cur].left);
    int R=height(tree,tree[cur].right);
    ans=max(ans,L+R+1);
    return 1+max(L,R);
}
int main(){
    int N;
    cin>>N;
    vector<Node> tree;
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(tree.empty()){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x==tree[cur].value){
                    break;
                }
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    height(tree,0);
    cout<<ans<<endl;
    return 0;
}*/


/*                                    H
struct Node{
    int value;
    int left;
    int right;
};
int main(){
    int N;
    cin>>N;
    vector<Node> tree;
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    vector<int> st;
    int cur=0;
    int sum=0;
    while(cur!=-1 || !st.empty()){
        while(cur!=-1){
            st.push_back(cur);
            cur=tree[cur].right;
        }
        cur=st.back();
        st.pop_back();
        sum+=tree[cur].value;
        cout<<sum<<" ";
        cur=tree[cur].left;
    }
    return 0;
}*/


/*                                    I
struct Node{
    int value;
    int left;
    int right;
};
int main(){
    int N;
    cin>>N;
    vector<Node> tree;
    for(int i=0;i<N;i++){
        int x;
        cin>>x;
        if(i==0){
            tree.push_back({x,-1,-1});
        }
        else{
            int cur=0;
            while(true){
                if(x<tree[cur].value){
                    if(tree[cur].left==-1){
                        tree[cur].left=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].left;
                }
                else{
                    if(tree[cur].right==-1){
                        tree[cur].right=tree.size();
                        tree.push_back({x,-1,-1});
                        break;
                    }
                    cur=tree[cur].right;
                }
            }
        }
    }
    int cur=0;
    int ans=0;
    for(int i=0;i<tree.size();i++){
        if(tree[i].left==-1 && tree[i].right==-1){
            ans++;
        }
    }
    cout<<ans;
    return 0;
}*/


/*                                    J
int main(){
    int n,m;
    cin>>n>>m;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    if(m>n){
        cout<<-1<<endl;
        return 0;
    }
    sort(a.begin(),a.end());
    cout<<a[m-1]<<endl;
    return 0;
}*/