#include iostream
#include string
#include vector
#include algorithm

using namespace std;

int main()
{
    int surface_n;  the number of points used to draw the surface of Mars.
    cin  surface_n; cin.ignore();
    int ly[surface_n];
    for (int i = 0; i  surface_n; i++) {
        int land_x;  X coordinate of a surface point. (0 to 6999)
        int land_y;  Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        cin  land_x  land_y; cin.ignore();
        ly[i] = land_y;
    }

    int i = 0;
    while(abs(ly[i+1] - ly[i]) != 0)
    {
        i++;
    }
    int land_y = ly[i];

     game loop
    while (1) {
        int x;
        int y;
        int h_speed;  the horizontal speed (in ms), can be negative.
        int v_speed;  the vertical speed (in ms), can be negative.
        int fuel;  the quantity of remaining fuel in liters.
        int rotate;  the rotation angle in degrees (-90 to 90).
        int power;  the thrust power (0 to 4).
        cin  x  y  h_speed  v_speed  fuel  rotate  power; cin.ignore();

         Write an action using cout. DON'T FORGET THE  endl
         To debug cerr  Debug messages...  endl;
        int p = 0;
        if((y - land_y)  1500)
        {
            if(v_speed  -10)
            {
                p += 3;
            }
        }
        else
        {
            p =4;
        }


         2 integers rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
        cout  0   p  endl;
    }
}