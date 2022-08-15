#include <iostream>
#include <string>
#include<string.h>
#include <vector>
#include <algorithm>

using namespace std;

void func(string a, string b, string f, string *out)
 {
     *out = "";
     bool test[a.length()];
     for(int j = 0; j < a.length(); j++)
     {
         if     (f.compare("AND") == 0){  test[j] = (a[j] == '-') && (b[j] == '-');}
         else if(f.compare("OR") == 0){   test[j] = (a[j] == '-') || (b[j] == '-');}
         else if(f.compare("XOR") == 0){  test[j] = ((a[j] == '-') && (b[j] == '_')) || ((a[j] == '_') && (b[j] == '-'));}
         else if(f.compare("NAND") == 0){ test[j] = !((a[j] == '-') && (b[j] == '-'));}
         else if(f.compare("NOR") == 0){  test[j] = !((a[j] == '-') || (b[j] == '-'));}
         else if(f.compare("NXOR") == 0){ test[j] = !(((a[j] == '-') && (b[j] == '_')) || ((a[j] == '_') && (b[j] == '-')));}

         if(test[j] == 1){ *out += '-';}
         else            { *out+= '_';}
     }
 }

int fd(string sl[],string s, int n)
{
    for(int i = 0; i < n; i++)
    {
        if (sl[i].compare(s) == 0) {return i;}
    }
}

int main()
{
    int n;
    cin >> n; cin.ignore();
    int m;
    cin >> m; cin.ignore();

    string name[n+m];
    string signal[n+m];

    string output;
    for (int i = 0; i < n; i++) {
        string input_name;
        string input_signal;
        cin >> input_name >> input_signal; cin.ignore();
        name[i] = input_name;
        signal[i] = input_signal;
    }
    for (int i = 0; i < m; i++) {
        string output_name;
        string type;
        string input_name_1;
        string input_name_2;
        cin >> output_name >> type >> input_name_1 >> input_name_2; cin.ignore();
        func(signal[fd(name, input_name_1, n)], signal[fd(name, input_name_2, n)], type, &output);
        cout << output_name << ' ' << output << endl;
    }
}