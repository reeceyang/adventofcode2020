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
    vll adapters;
    adapters.PB(0);
    while (getline(cin, line) && line != "") {
      adapters.PB(stoi(line));
    }

    sort(adapters.begin(), adapters.end());

    vll arrangements;
    arrangements.PB(1);
    REP(i, 1, adapters.size() - 1) {
      int j = i - 1;
      ll total = 0;
      while (j >= 0 && adapters[i] - adapters[j] <= 3) {
        total += arrangements[j];
        j--;
      }
      arrangements.PB(total);
    }

    TRAV(i, arrangements) {
      cout << i << " ";
    }
}
