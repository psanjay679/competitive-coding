#include <iostream>
#include <bitset>
#include <queue>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,
            tree_order_statistics_node_update> indexed_set;


int main(){
    indexed_set s;

    s.insert(2);
    s.insert(4);
    s.insert(8);
    s.insert(9);

    auto x = s.find_by_order(1);
    cout << *x << endl;

    auto y = s.order_of_key(8);
    cout << y << endl;

    auto z = s.order_of_key(3);

    cout << z << endl;

    return 0;
}
