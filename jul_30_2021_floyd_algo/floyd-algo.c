#include <stdio.h>
#include <stdlib.h>

#define INFINITY  1000
#define MAX_NODES 5

//           5 Nodes.
//
//             3       5       4
//         1 ----- 2 ----- 4 ----- 5
//          \             /       /
//       10  \         6 /    15 /
//            \         /       /
//             \       /       /
//               -- 3 --------
//
#if 1
int dd[MAX_NODES][MAX_NODES] = {
    {0, 3, 10, INFINITY, INFINITY},
    {3, 0, INFINITY, 5, INFINITY},
    {10, INFINITY, 0, 6, 15},
    {INFINITY,5,6,0,4},
    {INFINITY, INFINITY, INFINITY, 4,0}
};
#endif

#if 0
int dd[MAX_NODES][MAX_NODES] = {
    {0, 3, 100, INFINITY, INFINITY},
    {3, 0, INFINITY, 5, INFINITY},
    {10, INFINITY, 0, 6, 15},
    {INFINITY,5,6,0,INFINITY},
    {INFINITY, INFINITY, INFINITY, 4,0}
};
#endif

int ss[MAX_NODES][MAX_NODES] = {
    {0,2,3,4,5},
    {1,0,3,4,5},
    {1,2,0,4,5},
    {1,2,3,0,5},
    {1,2,3,4,0}
};

void print_arrays()
{
    int i, j;
    printf( "SS:\n");
    for (i = 0; i < MAX_NODES; i++) {
        for (j = 0; j < MAX_NODES; j++) {
            printf("%5d", ss[i][j]);
        }
        printf( "\n");
    }
    printf( "DD:\n");
    for (i = 0; i < MAX_NODES; i++) {
        for (j = 0; j < MAX_NODES; j++) {
            if (dd[i][j]<INFINITY) printf("%5d", dd[i][j]);
            else printf("  INF");
        }
        printf( "\n");
    }
};

void floyd_algo()
{
    int i,j,k;
    for (k = 0; k < MAX_NODES; k++) {
        for (i = 0; i < MAX_NODES; i++) {
            if (i == k) continue;
            for (j = 0; j < MAX_NODES; j++) {
                if (i == j || j == k) continue;
                if (dd[k][i]+dd[k][j] < dd[j][i]) {
                    dd[j][i] = dd[k][i]+dd[k][j];
                    ss[j][i] = k+1;
                }
            }
        }
        print_arrays();

    }
}
// Driver Code
int main()
{
    int start = 1, finish = 5;
    print_arrays();
    floyd_algo();
    printf("Path from %d to %d in reverse", start, finish);
    while (1) {
        printf("%3d <", finish);
        if (finish == ss[start-1][finish-1]) break;
        finish = ss[start-1][finish-1];
    }
    printf("%4d\n", start);
    return 0;
}
 
