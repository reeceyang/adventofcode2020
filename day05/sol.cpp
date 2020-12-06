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
    int maxId = 0;
    bool found[1024];
    REP(i, 0, 1023) {
      found[i] = false;
    }
    while (getline(cin, line) && line != "") {
      int pow2 = 64;
      int row = 0;
      REP(i, 0, 6) {
        if (line.at(i) == 'B') {
          row += pow2;
        }
        pow2 /= 2;
      }
      int col = 0;
      pow2 = 4;
      REP(i, 7, 9) {
        if (line.at(i) == 'R') {
          col += pow2;
        }
        pow2 /= 2;
      }
      int id = row * 8 + col;
      found[id] = true;
      if (id > maxId) {
        maxId = id;
      }
    }
    REP(i, 0, 1023) {
      if (!found[i]) {
        if (found[i - 1] && found[i + 1]) {
          cout << i;
          break;
        }
      }
    }
}
