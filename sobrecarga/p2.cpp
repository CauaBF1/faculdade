#include <iostream>
using namespace std;
class p2d{
    private:
        double x;
        double y;
    public:
        p2d (int x = 0, int y = 0){
            this->x = x;
            this->y = y;
        }

        const int getX() const {
            return x;
        }

        const int getY() const{
            return y;
        }

        void setX(double x){
            this->x = x;
        }

        void setY(double y){
            this->y = y;
        }

        const p2d operator+(const p2d& a) const {
            return p2d(x + a.x, y + a.y);
        }

        const p2d operator+(double a) const {
            return p2d(a + x, a + y);
        } 

        friend const p2d operator+(double a, const p2d& b){
            return p2d(a + b.x, a + b.y);
        }
        
        const p2d operator++(int){
            x++;
            y++;
            return *this;
        }

        friend ostream& operator<<(ostream& saida, const p2d& num){
            saida << "(" << num.x << "," << num.y << ")" << endl;
            return saida;
         }

};

class p3d : public p2d {
    private:
        double z;
    public:
        p3d(double x = 0, double y = 0, double z = 0) : p2d(x,y){
            this->z = z;
        }
        friend ostream& operator<<(ostream& saida, const p3d& num){
            saida << "(" << num.getX() << "," << num.getY() << "," << num.z << ")" << endl;
            return saida;
        }
};

int main(){
    p2d a(1,2);
    p2d b(2,3);
    p2d c;
    cout << "a = " << a;
    cout << "b = " << b;
    c = a + b;
    cout << "c = a + b"<< c;
    p3d d(1,2,4);
    cout << "D = "<< d;

    p2d e;
    cout << "B = "<< b;
    cout << "e = b++";
    e = b++;
    cout << e;


    return 0;
}

















