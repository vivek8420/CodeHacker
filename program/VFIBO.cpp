/*
* author: savaliya_vivek
* question: Vivek and Fibonaki
*/

#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define F first
#define S second
#define PI pair<ll,ll>
#define MAX 111111
#define MOD 1000000007
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)


ll mod(ll m)
{
    while(m<0)
        m+=MOD;
    return m%MOD;
}


void multiply(ll F[2][2], ll M[2][2])
{
  ll x =  mod(mod(F[0][0]*M[0][0]) + mod(F[0][1]*M[1][0]));
  ll y =  mod(mod(F[0][0]*M[0][1]) +mod( F[0][1]*M[1][1]));
  ll z =  mod(mod(F[1][0]*M[0][0]) + mod(F[1][1]*M[1][0]));
  ll w =  mod(mod(F[1][0]*M[0][1]) + mod(F[1][1]*M[1][1]));

  F[0][0] = x;
  F[0][1] = y;
  F[1][0] = z;
  F[1][1] = w;
}

void power(ll F[2][2], ll n)
{
  if( n == 0 || n == 1)
      return;
  ll M[2][2] = {{1,1},{1,0}};

  power(F, n/2);
  multiply(F, F);

  if (n%2 != 0)
     multiply(F, M);
}

ll fib(ll n)
{
  ll F[2][2] = {{1,1},{1,0}};
  if (n == 0)
    return 0;
  power(F, n-1);
  return F[0][0];
}

int main()
{
    boost;
    #ifndef ONLINE_JUDGE
        freopen("vfibo_input.txt","r",stdin);
        freopen("VFIBO.txt","w",stdout);
    #endif // ONLINE_JUDGE

    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        ll ans=fib(n);
        cout<<ans<<endl;
    }
}
