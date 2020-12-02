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
    while (getline(cin, line) && line != "") {
        int i = 0;
        int min = 0;
        while (line.at(i) != '-') {
            min = min * 10 + (line.at(i) - '0');
            i++;
        }
        i++;
        int max = 0;
        while (line.at(i) != ' ') {
            max = max * 10 + (line.at(i) - '0');
            i++;
        }
        i++;
        char c = line.at(i);
        i += 3;
        char c1 = line.at(i + min - 1);
        char c2 = line.at(i + max - 1);
        if ((c1 == c && c2 != c) || (c1 != c && c2 == c)) {
            valid++;
            //cout << "valid\n";
        }
        //cout << min << " " << max << " " << found << "\n";
    }

    cout << valid;
}
