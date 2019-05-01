#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

typedef unsigned long long int ui;
typedef pair<ui, ui> pr;


int main(){
    priority_queue<pr> pq;
    unordered_map<ui, ui> ump;

    ui n, m;
    cin >> n >> m;
    ui d;
    for (ui i = 1; i <= n; i++){
        cin >> d;
        if (ump.find(d) == ump.end()){
            ump.insert(make_pair(d, 1));
        }
        else{
            ump[d] += 1;
        }

        pq.push(make_pair(ump[d], d));

        pr ghost = pq.top();
        cout << ghost.second << " " << ghost.first << endl;
    }

    return 0;
}
