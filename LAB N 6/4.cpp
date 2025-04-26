#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> tree[MAXN];
int subtree_size[MAXN];

// DFS to compute subtree sizes
void dfs(int node, int parent) {
    subtree_size[node] = 1;  // count itself
    for (int child : tree[node]) {
        if (child != parent) {
            dfs(child, node);
            subtree_size[node] += subtree_size[child];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, r;
    cin >> n >> r;

    // Read edges
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    // Precompute subtree sizes
    dfs(r, 0);

    int q;
    cin >> q;
    while (q--) {
        int x;
        cin >> x;
        cout << subtree_size[x] << '\n';
    }

    return 0;
}
