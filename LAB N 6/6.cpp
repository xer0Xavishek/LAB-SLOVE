#include <bits/stdc++.h>
using namespace std;

vector<int> adj[26];
int indegree[26];
bool used[26];

bool buildGraph(const vector<string>& words) {
    int n = words.size();
    for (int i = 0; i < n - 1; ++i) {
        const string &a = words[i];
        const string &b = words[i + 1];
        int len = min(a.size(), b.size());
        bool found = false;

        for (int j = 0; j < len; ++j) {
            if (a[j] != b[j]) {
                int u = a[j] - 'a';
                int v = b[j] - 'a';
                adj[u].push_back(v);
                indegree[v]++;
                found = true;
                break;
            }
        }
        if (!found && a.size() > b.size()) {
            return false; 
        }
    }
    return true;
}
string topologicalSort() {
    priority_queue<int, vector<int>, greater<int>> pq;
    string result;

    for (int i = 0; i < 26; ++i) {
        if (used[i] && indegree[i] == 0) {
            pq.push(i);
        }
    }

    while (!pq.empty()) {
        int u = pq.top(); pq.pop();
        result += char(u + 'a');
        for (int v : adj[u]) {
            if (--indegree[v] == 0) {
                pq.push(v);
            }
        }
    }
    for (int i = 0; i < 26; ++i) {
        if (used[i] && indegree[i] > 0) return "-1";
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; ++i) {
        cin >> words[i];
        for (char c : words[i]) used[c - 'a'] = true;
    }

    if (!buildGraph(words)) {
        cout << -1 << '\n';
        return 0;
    }
    string ans = topologicalSort();
    cout << (ans == "-1" ? "-1" : ans) << '\n';

    return 0;
}
