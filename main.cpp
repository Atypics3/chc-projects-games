#include <iostream>
using namespace std;

int main() {
  // multiples of 3: 3, 6, 9, 12, ... --> print "Fizz"
  // multiples of 5: 5,10,15,20,... --> print "buzz"
  // for both: 15,60... --> "fizzbuzz"
  for (int i = 1; i < 100; i++) {
    if ((i % 3 == 0) && (i % 5 == 0)) //if it's a multiple of 3 and 5
      cout << "fizzbuzz" << endl;
    
    else if (i % 3 == 0) //if it's a multiple of 3
      cout << "fizz" << endl;
    
    else if (i % 5 == 0) // if it's a multiple of 5
      cout << "buzz" << endl;
      
    
    
    else //if it isn't a multiple of 3,5, or both, then print out regular number
      cout << i << endl;
  }

  return 0;
}