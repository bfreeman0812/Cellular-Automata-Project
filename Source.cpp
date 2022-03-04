#include <iostream>
#include <string>
using namespace std;

int main()
{
    string realArray[50] = { " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "+", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " };
    string tempArray[50] = { " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "+", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " " };

    for (int i = 0; i < 50; i++) {
        for (int x = 0; x < 50; x++)
            cout << realArray[x];

        for (int position = 0; position < 50; position++) {

            string test = "";

            if (position == 0) {
                test += (realArray[0]);
                test += (realArray[1]);
                test += (realArray[49]);
            }
            else if (position == 49) {
                test += ((realArray[position]));
                test += (realArray[0]);
                test += (realArray[1]);
            }
            else if (position == 48) {
                test += realArray[position];
                test += realArray[49];
                test += realArray[0];
            }
            else{
                test += realArray[position];
                test += realArray[(position + 1)];
                test += realArray[(position + 2)];
            }

            

            
            int temppos;
            if (position == 49) {
                temppos = position;
                position = -1;
            }
                
                
            if (test == "+++")
                tempArray[position + 1] = " ";
            else if (test == "++ ")
                tempArray[position + 1] = " ";
            else if (test == "+ +")
                tempArray[position + 1] = " ";
            else if (test == "+  ")
                tempArray[position + 1] = "+";
            else if (test == " ++")
                tempArray[position + 1] = "+";
            else if (test == " + ")
                tempArray[position + 1] = "+";
            else if (test == "  +")
                tempArray[position + 1] = "+";
            else if (test == "   ")
                tempArray[position + 1] = " ";
            
            if (position == -1)
                position = temppos;
        }
        //cout << endl;
        //for (int x = 0; x < 50; x++)
          //  cout << tempArray[x];
        copy(tempArray, tempArray+50, realArray);
        cout << "\n";
    }
}

