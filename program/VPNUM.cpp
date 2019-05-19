
/*
* author: savaliya_vivek
* question: Vivek and Prime Numbers
*/

#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define F first
#define S second
#define PI pair<ll,ll>
#define MAX 111111
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)


int main()
{
    boost;
    #ifndef ONLINE_JUDGE
        freopen("vpnum_input.txt","r",stdin);
        freopen("VPNUM.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        if(n==1)
        {
            cout<<"Not Prime"<<endl;
            continue;
        }
        int f=0;
        for(int i=2;i<=sqrt(n);i++)
        {
            if(n%i==0)
            {
                f=1;
                break;
            }
        }

        if(f==1)
            cout<<"Not Prime"<<endl;
        else
            cout<<"Prime"<<endl;
    }
}
