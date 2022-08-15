#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

 void parse(string s, string *out){
     for(int j = 0; j < s.length(); j += 3){
            *out += s[j];
        }
 }

int main(){
    int w;
    int h;
    cin >> w >> h; cin.ignore();
    int n = w/3+1;
    string T, B;
    int d [h-2][n];
    for (int i = 0; i < h; i++)
    {
        string s;
        getline(cin, s);
        cerr << s << endl;
        if (i == 0){ parse(s,&T);}
        else if(i < h-1){
            for(int j = 0; j < s.length()-1; j++){
                string ss = s.substr(j, 2);
                int k = (j)/3;
                d[i-1][k+1] = 0;
                if(ss.compare("|-") == 0){
                    d[i-1][k] = 1;
                }else if(ss.compare("-|") == 0){
                    d[i-1][k+1] = -1;
                } else if((ss.compare("| ") == 0) && (d[i-1][k] != -1)){
                    d[i-1][k] = 0;
                }
            }
        } else{ parse(s,&B);}
    }

    for(int i = 0; i < n; i++){
        int x = i;
        for(int j = 0; j < h-2; j++){
            x += d[j][x];
        }
        cout << T[i] << B[x] << endl;
    }
}