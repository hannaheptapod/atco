#include <bits/stdc++.h>

#include <atcoder/all>
using namespace std;
using namespace atcoder;
using mint = modint1000000007;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;
typedef vector<vector<int>> vvi;
typedef vector<vector<long long>> vvl;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define INF ((1LL << 62) - (1LL << 31))
#define MINF ((1 << 30) - (1 << 15))
#define rep(i, s, n) for (int i = s; i < n; i++)
#define graph(name, h, w, init) \
    vector<vector<int>> name(h, vector<int>(w, init))
#define all(v) v.begin(), v.end()
#define fmod(n, m) (n % m + m) % m

/*全部llで宣言しろ!
負の数添え字チェックしろ!*/
int main(void) {
    int h, w;
    cin >> h >> w;
    vector<string> a1(w);
    rep(i, 0, h) {
        string s;
        cin >> s;
        rep(i, 0, w) a1[i] = a1[i] + s[i];
    }
    vector<string> a2(w);
    rep(i, 0, h) {
        string s;
        cin >> s;
        rep(i, 0, w) a2[i] = a2[i] + s[i];
    }
    sort(all(a1));
    sort(all(a2));
    rep(i, 0, w) if (a1[i] != a2[i]) {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
    return 0;
}
