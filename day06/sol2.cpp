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
    int total = 0;
    bool newGroup = true;
    set<char> group;
    while (getline(cin, line)) {
      if (newGroup && line == "") {
        break;
      } else if (!newGroup && line == "") {
        total += group.size();
        group.erase(group.begin(), group.end());
        newGroup = true;
      } else if (newGroup) {
        newGroup = false; // start of a new group
        REP(i, 0, line.length() - 1) {
          group.insert(line.at(i));
        }
      } else {
        set<char> foundGroup; // other member of the group
        REP(i, 0, line.length() - 1) {
          if (group.find(line.at(i)) != group.end()) {
            foundGroup.insert(line.at(i));
          }
        }
        group = foundGroup;
      }
    }

    cout << total;
}
