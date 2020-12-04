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
    int valid = 0;
    bool newPassport = true;
    string passport = "";
    while (getline(cin, line)) {
      if (newPassport && line == "") {
        break;
      } else if (!newPassport && line == "") {
        if (passport.find("byr:") != string::npos &&
          passport.find("iyr:") != string::npos &&
          passport.find("eyr:") != string::npos &&
          passport.find("hgt:") != string::npos &&
          passport.find("hcl:") != string::npos &&
          passport.find("ecl:") != string::npos &&
          passport.find("pid:") != string::npos) {
          valid++;
        }
        passport = "";
        newPassport = true;
      } else {
        newPassport = false;
        passport += line + "\n";
      }
    }

    cout << valid;
}
