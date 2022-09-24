#include <bits/stdc++.h>
using namespace std;

int N, X, Y;
vector<vector<int>> graph;
stack<int> ans;
vector<bool> visited;

int dfs(int u);

int main() {
    cin >> N >> X >> Y;
    graph = vector<vector<int>>(N + 1, vector<int>());
    int u, v;
    for (int i = 0; i < N - 1; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    visited = vector<bool>(N + 1, false);
    visited[X] = true;
    dfs(X);

    while (!ans.empty()) {
        cout << ans.top();
        ans.pop();
        if (!ans.empty()) cout << ' ';
    }
    cout << endl;
    return 0;
}

int dfs(int u) {
    if (u == Y) {
        ans.push(u);
        return true;
    }
    for (int v : graph[u]) {
        if (visited[v]) continue;
        visited[v] = true;
        if (dfs(v)) {
            ans.push(u);
            return true;
        }
    }

    return false;
}
