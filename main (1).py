#include <iostream>
using namespace std;
 
// Macro to check if a year
// is a leap year
#define ISLP(y) ((y % 400 == 0) ||\
(y % 100 != 0) && (y % 4 == 0))
        
// Driver Code
int main()
{
    int year = 2020;
    cout << ISLP(year) << "\n";
    return 0;
}