#include <stdio.h>
typedef struct fPoint_tag
{
    float x;
    float y;
    struct fPoint_tag *pNext;
} fPoint;

float sign (fPoint *p1, fPoint *p2, fPoint *p3)
{
    return (p1->x - p3->x) * (p2->y - p3->y) - (p2->x - p3->x) * (p1->y - p3->y);
}

float square (fPoint *p1, fPoint *p2, fPoint *p3)
{
    float ret;
    ret = p2->x*p3->y - p3->x*p2->y - p1->x*p3->y + p3->x*p1->y + p1->x*p2->y - p2->x*p1->y;
    if (ret < 0) ret = -ret;
    return ret;
}
// 
//    1   1   1
//    x1  x2  x3
//    y1  y2  y3
// 
//    (x2*y3 - x3*y2) - (x1*y3 - x3*y1) + (x1*y2 - x2*y1)
//
int PointInPoly (fPoint *pt, fPoint *v)
{
    float d1;
    int has_neg = 0, has_pos = 0, has_zeroes = 0;

    fPoint *pHead = v;
    float TotalS = 0;
    float PolyS = 0;

    v = v->pNext;
    for (;;)
    {
        PolyS += square(v, v->pNext, pHead);
        printf( "PolyS : %f \n", PolyS);
        v = v->pNext;
        if (v->pNext == pHead) break;
    }
    v = pHead;
    for (;;)
    {
        TotalS += square(pt, v, v->pNext);
        printf( "TotalS : %f PolyS : %f \n", TotalS, PolyS);
        v = v->pNext;
        if (v == pHead) break;
    } 
    if (PolyS == TotalS) {
        return 1;
    } else {
        return 0;
    }
}

int PointInPoly2 (fPoint *pt, fPoint *v)
{
    float d1;
    int has_neg = 0, has_pos = 0, has_zeroes = 0;

    fPoint *pHead = v;

    for (;;)
    {
        d1 = sign(pt, v, v->pNext);
        if (d1 < 0) has_neg = 1;
        if (d1 > 0) has_pos = 1;
        if (d1 == 0.0) has_zeroes = 1;
        if (has_zeroes) return 0;
        if (has_neg && has_pos) return 0;
        v = v->pNext;
        if (v == pHead) break;
    } 

    return 1;
}

 
int main () {
    fPoint pt, v1, v2, v3, v4;
    v1.x = 0.0;
    v1.y = 0.0;
    v1.pNext = &v2;

    v2.x = 0.0;
    v2.y = 1.0;
    v2.pNext = &v3;

    v3.x = 1.0;
    v3.y = 1.0;
    v3.pNext = &v4;

    v4.x = 1.0;
    v4.y = 0.0;
    v4.pNext = &v1;

    pt.x = 0.0;
    pt.y = 0.0;

    int ret = 0;

    ret = PointInPoly2(&pt, &v1);
 
   printf( "Point in polygon (sign) : %d\n", ret );
   ret = PointInPoly(&pt, &v1);
 
   printf( "Point in polygon : %d\n", ret );
 
   return 0;
}
