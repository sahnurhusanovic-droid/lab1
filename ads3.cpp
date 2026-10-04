#include <iostream>
#include <deque>
#include <algorithm>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;
/*int main(){
    int n,k;
    cin>>n;
    int a[10000];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    cin>>k;
    int left=0;
    int right=n-1;
    bool found=false;
    while(left<=right){
        int mid=(left+right)/2;
        if(a[mid]==k){
            found=true;
            break;
        }
        else if(a[mid]<k){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    if(found){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    return 0;
}*/


/*int main(){
    int n,q;
    cin>>n>>q;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a.begin(),a.end());
    while(q--){
        int l1,r1,l2,r2;
        cin>>l1>>r1>>l2>>r2;
        if(l1>l2){
            swap(l1,l2);
            swap(r1,r2);
        }
        int ans=0;
        if(r1<l2){
            int count1=upper_bound(a.begin(),a.end(), r1)
            - lower_bound(a.begin(),a.end(),l1);
            int count2=upper_bound(a.begin(),a.end(),r2)
            - lower_bound(a.begin(),a.end(), l2);
            ans=count1+count2;
        }
        else{
            int left=lower_bound(a.begin(),a.end(),l1)-a.begin();
            int right= upper_bound(a.begin(),a.end(),max(r1,r2))-a.begin();
            ans=right-left;
        }
        cout<<ans<<endl;
    }
    return 0;
}*/


/*int main(){
    int n,m;
    cin>>n>>m;
    vector<int> pref(n);
    long long sum=0;
    for(int i=0;i<n;i++){
        long long a;
        cin>>a;
        sum+=a;
        pref[i]=sum;
    }
    while(m--){
        long long b;
        cin>>b;
        int pos=lower_bound(pref.begin(),pref.end(),b)-pref.begin();
        cout<<pos+1<<endl;
    }   
    return 0;
}*/


/*int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    sort(a.begin(),a.end());
    vector<int> prefix(n);
    prefix[0]=a[0];
    for(int i=1;i<n;i++){
        prefix[i]=prefix[i-1]+a[i];
    }
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
}*/


/*int main(){
    long long n, h;
    cin>>n>>h;
    vector<int> a(n);
    int maxbag=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        maxbag=max(maxbag,a[i]);
    }
    int left=1;
    int right=maxbag;
    int answer=maxbag;
    while(left<=right){
        int mid=left+(right-left)/2;
        long long hours=0;
        for(int i=0;i<n;i++){
            hours+=(a[i]+mid-1)/mid;
        }
        if(hours<=h){
            answer=mid;
            right=mid-1;
        }
        else{
            left=mid+1;
        }
    }
    cout<<answer<<endl;
    return 0;
}*/


/*int main(){
    int n,m;
    cin>>n>>m;
    vector<int> ropes(n);
    double right=0;
    double left=0;
    for(int i=0;i<n;i++){
        cin>>ropes[i];
        if(ropes[i]>right){
            right=ropes[i];
        }
    }
    for(int i=0;i<100;i++){
        double mid=(right+left)/2.0;
        long long pieces=0;
        for(int j=0;j<n;j++){
            pieces+=(long long)(ropes[j]/mid);
        }
        if(pieces>=m){
            left=mid;
        }
        else{
            right=mid;
        }
    }
    cout<<fixed<<setprecision(10)<<left<<endl;
    return 0;
}*/


/*int main(){
    int n;
    long long k;
    cin>>n>>k;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int left=0;
    long long sum=0;
    int ans=INT_MAX;
    for(int right=0;right<n;right++){
        sum+=a[right];
        while(sum>=k){
            ans=min(ans,right-left+1);
            sum-=a[left];
            left++;
        }
    }
    cout<<ans<<endl;
    return 0;
}*/


/*int main(){
    int n,k;
    cin>>n>>k;
    vector<long long> a(n);
    long long right=0,left=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        left=max(left,a[i]);
        right+=a[i];
    }
    while(left<right){
        long long mid=left+(right-left)/2;
        int bloks=1;
        long long sum=0;
        for(int i=0;i<n;i++){
            if(sum+a[i]>mid){
                bloks++;
                sum=a[i];
            }
            else{
                sum+=a[i];
            }
        }
        if(bloks<=k){
            right=mid;
        }
        else{
            left=mid+1;
        }
    }
    cout<<left<<endl;
    return 0;
}*/


/*int main(){
    int n,k;
    cin>>n>>k;
    vector<long long> need(n);
    for(int i=0;i<n;i++){
        int x1,y1,x2,y2;
        cin>>x1>>y1>>x2>>y2;
        need[i]=max(x2,y2);
    }
    sort(need.begin(),need.end());
    cout<<need[k-1];
    return 0;
}*/


/*int main(){
    int t;
    cin>>t;
    vector<int> x(t);
    for(int i=0;i<t;i++){
        cin>>x[i];
    }
    int n,m;
    cin>>n>>m;
    vector<vector<int>> a(n,vector<int> (m));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>a[i][j];
        }
    } 
    for(int k=0;k<t;k++){
        int left=0;
        int right=n*m-1;
        bool found=false;
        while(left<=right){
            int mid=left+(right-left)/2;
            int row=mid/m;
            int col;
            if(row%2==0){
                col=mid%m;
            }
            else{
                col=m-1-(mid%m);
            }
            if(a[row][col]==x[k]){
                cout<<row<<" "<<col<<endl;
                found=true;
                break;
            }
            if(a[row][col]>x[k]){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        if(!found){
            cout<<-1<<" "<<-1<<endl;
        }
    }
    return 0;
}*/


