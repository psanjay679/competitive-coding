#include <iostream>
#include <bitset>
#include <queue>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef tree<int,null_type,less<int>,rb_tree_tag,
            tree_order_statistics_node_update> indexed_set;

int main(int argc, char const *argv[])
{
	/* code */

	priority_queue<int, vector<int>, greater<int>> pq;

	for (auto i = 0; i < 10; i++){
		pq.push(i);
	}


	pq.push(1);
	cout << pq.top();

	cout << endl;
	return 0;
}
