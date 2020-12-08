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
  //freopen((name+".out").c_str(),"w",stdout);
}

void setIO() {
  ios_base::sync_with_stdio(0); cin.tie(0);
}

struct BAG {
  vector<string> bags;
  int canContain;
};

int main() {
  setIO("7");

  string line;
  int total = 0;
  map<string, BAG> bags;
  while (getline(cin, line) && line != "") {
    cout << line << "\n";
    auto iss = istringstream{line};
    BAG b;
    vector<string> tokens;
    auto str = string{};
    while (iss >> str) {
      tokens.PB(str);
      cout << str << " ";
    }
    cout << "\n";
    string color = tokens[0] + " " + tokens[1];
    vector<string> bBags;
    string current;
    REP(i, 2, tokens.size()) {
      if (i % 3 == 0) {
        continue; // skip all the numbers for now
      }
      if (i % 3 == 1) {
        current = tokens[i];
      } else {
        current += tokens[i];
        bBags.PB(current);
        current = "";
      }
    }
    b.canContain = 0; // we don't know yet
    b.bags = bBags;
    bags[color] = b;
  }

  cout << total;
}
