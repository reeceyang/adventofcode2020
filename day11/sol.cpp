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
    vector<string> grid;
    string buffer;
    REP(i, 1, 100) {
      buffer += ".";
    }
    grid.PB(buffer); // buffer the grid
    while (getline(cin, line) && line != "") {
      grid.PB("." + line + ".");
    }
    grid.PB(buffer);

    bool same = false;
    while (!same) {
      vector<string> new_grid;
      new_grid.PB(buffer);
      int total_occupied = 0;
      same = true;
      REP(i, 1, grid.size() - 2) {
        string new_line = "";
        REP(j, 1, 98) {
          int adjacent = 0;
          if (grid[i].at(j + 1) == '#') adjacent++;
          if (grid[i].at(j - 1) == '#') adjacent++;
          if (grid[i + 1].at(j) == '#') adjacent++;
          if (grid[i + 1].at(j + 1) == '#') adjacent++;
          if (grid[i + 1].at(j - 1) == '#') adjacent++;
          if (grid[i - 1].at(j) == '#') adjacent++;
          if (grid[i - 1].at(j + 1) == '#') adjacent++;
          if (grid[i - 1].at(j - 1) == '#') adjacent++;
          if (grid[i].at(j) == 'L' && adjacent == 0) {
            new_line += "#";
            total_occupied++;
          } else if (grid[i].at(j) == '#' && adjacent >= 4) {
            new_line += "L";
          } else {
            new_line += grid[i].at(j);
            if (grid[i].at(j) == '#') total_occupied++;
          }
        }
        if ("." + new_line + "." != grid[i]) {
          same = false;
        }
        //cout << "." + new_line + ".\n";
        new_grid.PB("." + new_line + ".");
      }
      new_grid.PB(buffer);
      grid = new_grid;
      if (same) {
        cout << total_occupied;
        break;
      }
    }
}
