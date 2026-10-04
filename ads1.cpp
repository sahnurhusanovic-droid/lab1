#include <iostream>
#include <string>
#include <stack>
#include <deque>
#include <algorithm>
using namespace std;
/*                                      A

int main(){
    long long a,b;
    cin>>a>>b;
    while(b!=0){
        long long c=b;
        b=a%b;
        a=c;
    }
    cout<<a;
    return 0;
}
                                        B

 long long d(long long a, long long n, long long m){
    a%=m;
    long long result =1;
    if(m==1){
        return 0;
    }
    while(n>0){
        if(n%2==1){
            result=(result*a)%m;
        }
        a=(a*a)%m;
        n/=2;
    }
    return result;
}
int main(){
    int a,n,m;
    cin>>a>>n>>m;
    cout<<d(a,n,m)<<endl;
    return 0;
}
                                        C

int main(){
    int a;
    cin>>a;
    if(a<2){
        cout<<"NO";
        return 0;
    }
    for(long long i=2;i*i<=a;i++){
        if(a%i==0){
            cout<<"NO";
            return 0;
        }
    }
    cout<<"YES";
    return 0;
}
                                        D

bool isprime(long long n){
    if(n<2){
        return false;
    }
    for(long long i=2;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
int main(){
    long long n;
    cin>>n;
    int count=0;
    long long number=2;
    while(count<n){
        if(isprime(number)){
            count++;
        }
        if(count==n){
            cout<<number;
            break;
        }
        number++;
    }
    return 0;
}
                                    E

int main(){
    int a;
    cin>>a;
    for(int i=2;i*i<=a;i++){
        while(a%i==0){
            cout<<i<<" ";
            a/=i;
        }   
    }
    if(a>1){
        cout<<a;
    }
    return 0;
}
                                        F
string process(string s){
    stack<char> st;
    for(int i=0;i<s.length();i++){
        char c=s[i];
        if(c=='#'){
            if(!st.empty()){
                st.pop();
            }
        }
        else{
            st.push(c);
        }
    }
    string result;
    while(!st.empty()){
        result+=st.top();
        st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
int main(){
    string a, b;
    cin>>a>>b;
    if(process(a)==process(b)){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
    return 0;
}
                                        G

int main(){
    string s;
    cin>>s;
    stack<char> st;
    for(int i=0;i<s.length();i++){
        char c=s[i];
        if(!st.empty() && st.top()==c){
            st.pop();
        }
        else{
            st.push(c);
        }
    }
    if(st.empty()){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
return 0; }

                                        H

int main(){
    int n;
    cin>>n;
    stack<int> st;
    for(int i=0;i<n;i++){
        int age;
        cin>>age;
        while(!st.empty() && st.top()>=age){
            st.pop();
        }
        if(st.empty()){
            cout<<"-1"<<" ";
        }
        else{
            cout<<st.top()<<" ";
        }
        st.push(age);
    }
    return 0;
}

                                        I

int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        deque<int> deck;
        for(int i=n;i>=1;i--){
            deck.push_front(i);
            int moves=i%deck.size();
            for(int j=0;j<moves;j++){
                int last=deck.back();
                deck.pop_back();
                deck.push_front(last);
            }
        }
        for(int i=0;i<deck.size();i++){
            cout<<deck[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}

                                        J*/


int main(){
    deque<int> nu;
    deque<int> bu;
    int card;
    for(int i=0;i<5;i++){
        cin>>card;
        nu.push_back(card);
    }
    for(int i=0;i<5;i++){
        cin>>card;
        bu.push_back(card);
    }
    int moves=0;
    while(!nu.empty() && !bu.empty()){
        int n=nu.front();
        int b=bu.front();
        nu.pop_back();
        bu.pop_back();
        moves++;
        bool buwins;
            if(b==0 && n==9){
                buwins=true;
            }
            else if(b==9 && n==0){
                buwins=false;
            }
            else if(b>n){
                buwins=true;
            }
            else{
                buwins=false;
            }
            if(buwins){
                bu.push_back(b);
                bu.push_back(n);
            }
            else{
                nu.push_back(b);
                nu.push_back(n);
            }
        }
        if(bu.empty()){
            cout<<"Nursik "<<moves;
        }
        else{
            cout<<"Boris "<<moves;
        }
        return 0;
}