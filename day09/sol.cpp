#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int,int> pi;
typedef vector<pi> vpi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = a; i <= b; i++)
#define TRAV(a, x) for (auto& a : x)

void setIO(string name) {
    ios_base::sync_with_stdio(0); cin.tie(0);
    freopen((name+".in").c_str(),"r",stdin);
    freopen((name+".out").c_str(),"w",stdout);
}

void setIO() {
    ios_base::sync_with_stdio(0); cin.tie(0);
}

int main() {
    setIO();

    string line;
    deque<unsigned ll> d;
    set<unsigned ll> sums;
    unsigned long long num = 0;
    bool done = false;
    REP(i, 1, 25) {
      getline(cin, line);
      d.PB(stoll(line));
    }
    while (getline(cin, line) && line != "") {
      // search for sum
      bool found = false;
      REP(i, 0, 24) {
        REP(j, i, 24) {
          if (d[i] + d[j] == stoull(line)) {
            found = true;
            break;
          }
        }
        if (found) break;
      }
      if (!found && !done) {
        num = stoull(line);
        done = true;
      }
      d.pop_front();
      d.PB(stoull(line));
    }

    cout << num;
}
