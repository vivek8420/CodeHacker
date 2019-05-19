/*
* author: savaliya_vivek
* question: Tom and Jerry
*/

#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define F first
#define S second
#define PI pair<ll,ll>
#define MAX 111111
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)

vector<int>graph[MAX];
bool visit[MAX];

void dfs(int u)
{
    visit[u]=true;
    for(int v:graph[u])
    {
        if(!visit[v])
            dfs(v);
    }
}
void flush(int n)
{
    for(int i=0;i<=n;i++)
    {
        graph[i].clear();
        visit[i]=false;
    }
}

int main()
{
    boost;
    #ifndef ONLINE_JUDGE
        freopen("taj_input.txt","r",stdin);
        freopen("TAJ.txt","w",stdout);
    #endif // ONLINE_JUDGE

    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        int a,b,u,v;
        cin>>a>>b;
        while(m--)
        {
            cin>>u>>v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        dfs(a);

        if(visit[b])
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
        flush(n);
    }
}
