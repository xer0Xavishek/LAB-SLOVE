#include <bits/stdc++.h>
using namespace std;

int main(){

    ios::sync_with_stdio(false);

    cin.tie(nullptr);

    int N, M, S, D;

    cin >> N >> M >> S >> D;

    vector<vector<int>> adj(N+1);

    vector<int> u(M), v(M);

    for(int i = 0; i < M; i++) cin >> u[i];

    for(int i = 0; i < M; i++) cin >> v[i];

    for(int i = 0; i < M; i++){

        adj[u[i]].push_back(v[i]);

        adj[v[i]].push_back(u[i]);

    }

    for(int i = 1; i <= N; i++){

        sort(adj[i].begin(), adj[i].end());

    }

    vector<int> dist(N+1, -1), par(N+1, -1);

    queue<int> q;

    dist[S] = 0;

    q.push(S);


    while(!q.empty()){
          
        int u = q.front(); q.pop();

        if(u == D) break;  

        for(int w : adj[u]){

            if(dist[w] == -1){

                dist[w] = dist[u] + 1;

                par[w]  = u;

                q.push(w);

            }
        }
    }

    if(dist[D] == -1){

        cout << -1 << "\n";

    } else {

        cout << dist[D] << "\n";

        vector<int> path;

        for(int cur = D; cur != -1; cur = par[cur]){

            path.push_back(cur);

        }
        reverse(path.begin(), path.end());

        for(int x : path){

            cout << x << " ";

        }
        
        cout << "\n";

    }

    return 0;
}
