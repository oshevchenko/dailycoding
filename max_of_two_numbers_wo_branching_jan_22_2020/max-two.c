#include <stdio.h>
int absbit32(int x, int y)
{
    int sub = x - y;
    printf( "sub : 0x%04X\n", sub );
    int mask = (sub >> 31);
    printf( "mask : 0x%04X\n", mask );
    return (sub ^ mask) - mask;        
 }
 
int max(int x, int y)
{
    int abs = absbit32(x, y);
    printf( "abs : %d\n", abs );
    return (x + y + abs) / 2;        
 }
  
int min(int x, int y)
{
    int abs = absbit32(x, y);        
    return (x + y - abs) / 2;
}
  
// Driver Code
int main()
{
    printf( "3 > -3 : %d\n", (3 ^ 0xFFFFFFFF) - 0xFFFFFFFF );
    printf( "max(2, 3) : %d\n", max(33, 2) );
    printf( "max(2, -3) : %d\n", max(2, 3) );
    printf( "max(-2, -3) : %d\n", max(-2, -3) );
 
    return 0;
}
 
