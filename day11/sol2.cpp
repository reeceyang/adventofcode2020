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

vector<string> grid;

bool look(int i, int j, int dx, int dy) {
  int x = i + dx, y = j + dy;
  //cout << "1\n";
  while (x >= 0 && x < grid.size() && y >= 0 && y < 100) {
    if (grid[x].at(y) == '#') {
      return true;
    } else if (grid[x].at(y) == 'L') {
      return false;
    }
    x += dx;
    y += dy;
    //cout << "got here1\n";
  }
  //cout << "got here\n";
  return false;
}

int main() {
    //setIO();

    string line;

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
          if (look(i, j, 0, 0 + 1)) adjacent++;
          if (look(i, j, 0, 0 - 1)) adjacent++;
          if (look(i, j, 0 + 1, 0)) adjacent++;
          if (look(i, j, 0 + 1, 0 + 1)) adjacent++;
          if (look(i, j, 0 + 1, 0 - 1)) adjacent++;
          if (look(i, j, 0 - 1, 0)) adjacent++;
          if (look(i, j, 0 - 1, 0 + 1)) adjacent++;
          if (look(i, j, 0 - 1, 0 - 1)) adjacent++;
          if (grid[i].at(j) == 'L' && adjacent == 0) {
            new_line += "#";
            total_occupied++;
          } else if (grid[i].at(j) == '#' && adjacent >= 5) {
            new_line += "L";
          } else {
            new_line += grid[i].at(j);
            if (grid[i].at(j) == '#') total_occupied++;
          }
        }
        if ("." + new_line + "." != grid[i]) {
          same = false;
        }
        cout << "." + new_line + ".\n";
        new_grid.PB("." + new_line + ".");
      }
      new_grid.PB(buffer);
      grid = new_grid;
      cout << "=====\n";
      if (same) {
        cout << total_occupied;
        break;
      }
    }
}
