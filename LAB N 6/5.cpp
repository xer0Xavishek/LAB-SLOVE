#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> adj[MAXN];

pair<int, int> bfs(int start, int n) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(start);
    dist[start] = 0;

    int farthe = start;

    while (!q.empty()) {
        int node = q.front(); q.pop();
        for (int v : adj[node]) {
            if (dist[v] == -1) {
                dist[v] = dist[node] + 1;
                q.push(v);
                if (dist[v] > dist[farthe]) {
                    farthe = v;
                }
            }
        }
    }

    return {farthe, dist[farthe]};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int A = bfs(1, n).first;

    auto [B, diameter] = bfs(A, n);

    cout << diameter << '\n';
    cout << A << ' ' << B << '\n';

    return 0;
}
