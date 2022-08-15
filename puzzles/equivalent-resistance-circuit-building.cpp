#include iostream
#include string
#include vector
#include unordered_map

using namespace std;

double solve(unordered_mapstring, double R, vectorstring circuit) {
    double result = 0;
    if(circuit-size()  0)
    {
        string c = circuit-at(0);
        double value = 0;
        circuit-erase(circuit-begin());
        if(c.compare(() == 0){
            while(circuit-size()  0 && circuit-at(0).compare()) != 0)
                result += solve(R, circuit);
            circuit-erase(circuit-begin());
        }
        else if(c.compare([) == 0){
            while(circuit-size()  0 && circuit-at(0).compare(]))
                value += 1solve(R, circuit);
            result = 1(value);
            circuit-erase(circuit-begin());
        }
        else if(!(c.compare()) == 0  c.compare(]) == 0)){
            result = R[c];
        }
    }
    return (double)result;
}

int main(){
    int n;
    cin  n; cin.ignore();
    unordered_mapstring, double R;
    for (int i = 0; i  n; i++) {
        string name;
        double r;
        cin  name  r; cin.ignore();
        R[name] = r;
    }
    string circuit;
    getline(cin, circuit);
    vectorstring circ;
    string item = ;
    for(char c  circuit){
        if(c == ' '){
            circ.push_back(item);
            item = ;
        }
        else item += c;
    }
    circ.push_back(item);
    printf(%.1f, solve(R, &circ));
}