#include iostream
#include string
#include cmath

using namespace std;

void distance(int ax,int ay, int speed, int bx[], int by[], int dx, int dy, int d, int outn)
{
    for(int i = 0; i  outn; i++){
        dx[i] = abs(bx[i] - ax);
        dy[i] = abs(by[i] - ay);
        d[i] = ceil((float)dx[i]speed) + ceil((float)dy[i]speed);
    }
}

int indexmin(int array[], int size)
{
    int index = 0;
    for(int i = 1; i  size; i++){
        if(array[i]  array[index])
            index = i;
    }
    return index;
}

int winner(int n, int h, int w,int map, int px[],int py[], int speed[], int outx[],int outy[], int outn)
{
    int dout[n];
    for(int s = 0; s  n; s++){
        int dx[outn], dy[outn], d[outn];
        distance(px[s], py[s], speed[s], outx, outy, dx, dy, d, outn);
        dout[s] = d[indexmin(d, outn)];
    }
    return indexmin(dout, n)+1;
}
int main()
{
    int n;
    cin  n; cin.ignore();
    int speed[n];
    for (int i = 0; i  n; i++) {
        cin  speed[i]; cin.ignore();
    }
    int h, w;
    cin  h; cin.ignore();
    cin  w; cin.ignore();
    int map;
    map = new int [h];
    for(int i = 0; i h; i++)
        map[i] = new int[n];
    int outx[n], outy[n], outn = 0;
    int px[n], py[n];
    for (int i = 0; i  h; i++) {
        string row;
        getline(cin, row);
        for(int j = 0; j  row.length(); j++){
            if(row[j] == '#'){
                outx[outn] = j;
                outy[outn] = i;
                outn++;
                map[i][j] = '#';
            } else{
                int k = row[j] - '0';
                if((1 = k) && (k = n)){
                    px[k-1] = j;
                    py[k-1] = i;
                }
            }
        }
    }

    cout  winner(n, h, w, map, px, py, speed, outx, outy, outn)  endl;
}