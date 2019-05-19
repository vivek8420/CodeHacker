/*
* author: savaliya_vivek
* question: Mayur and Max Sum
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
        freopen("mmsum_input.txt","r",stdin);
        freopen("MMSUM.txt","w",stdout);
    #endif // ONLINE_JUDGE

    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        ll a[n+1],dp[n+1];
        for(int i=1;i<=n;i++)
            cin>>a[i];
        dp[0]=0;
        dp[1]=max(0LL,a[1]);
        for(int i=2;i<=n;i++)
            dp[i]=max(dp[i-2]+a[i],dp[i-1]);
        cout<<dp[n]<<endl;
    }
}
