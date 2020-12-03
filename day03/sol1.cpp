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
    int trees = 0;
    int xpos = 0;
    int row = 0;
    while (getline(cin, line) && line != "") {
      if (row % 2 == 1) { // skipping rows
        row++;
        continue;
      }
      if (line.at(xpos) == '#') {
        trees++;
      }
      xpos = (xpos + 1) % line.length(); // change for different slopes
      row++;
    }

    cout << trees;
}
