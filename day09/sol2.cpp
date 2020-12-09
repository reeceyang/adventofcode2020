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
    vector<unsigned ll> numbers;
    vector<unsigned ll> sum;
    unsigned long long current = 0;
    unsigned long long num = 32321523;
    unsigned long long ans = 0;
    bool done = false;
    while (getline(cin, line) && line != "") {
      if (!done) {
        unsigned long long thenum = stoull(line);
        numbers.PB(thenum);
        sum.PB(current + thenum);
        current += thenum;
        REP(i, 0, sum.size() - 2) {
          if (current - sum[i] == num) {
            done = true;
            ans = numbers[i] + thenum;
            break;
          }
        }
      }
    }

    cout << ans;
}
