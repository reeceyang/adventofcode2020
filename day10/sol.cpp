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
    vi adapters;
    while (getline(cin, line) && line != "") {
      adapters.PB(stoi(line));
    }

    sort(adapters.begin(), adapters.end());

    int ones = 1, threes = 1;
    REP(i, 1, adapters.size() - 1) {
      if (adapters[i] - adapters[i - 1] == 1) ones++;
      if (adapters[i] - adapters[i - 1] == 3) threes++;
    }
    cout << ones << " " << threes << " " << ones * threes;
}
