/*
Cauã Borges Faria (834437)
Nicolas Magno Messias da Silva(834054)
Lucas Rogrigues da Silva (834724)
*/

#include <iostream>
using namespace std;
class PONTO2D{
    private:
        double x;
        double y;
    public:
        PONTO2D (int x = 0, int y = 0){
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

        const PONTO2D operator*(const PONTO2D& a) const {
            return PONTO2D(x * a.x, y * a.y);
        }

        const PONTO2D operator*(double a) const {
            return PONTO2D(a * x, a * y);
        } 

        friend const PONTO2D operator*(double a, const PONTO2D& b){
            return PONTO2D(a * b.x, a * b.y);
        }
        
        const PONTO2D operator++(){
          ++x;
          ++y;
          return *this;  
      }

        friend ostream& operator<<(ostream& saida, const PONTO2D& num){
            saida << "(" << num.x << "," << num.y << ")" << endl;
            return saida;
         }

};

class PONTO3D : public PONTO2D {
    private:
        double z;
    public:
        PONTO3D(double x = 0, double y = 0, double z = 0) : PONTO2D(x,y){
            this->z = z;
        }
        friend ostream& operator<<(ostream& saida, const PONTO3D& num){
            saida << "(" << num.getX() << "," << num.getY() << "," << num.z << ")" << endl;
            return saida;
        }
};

int main(){
    PONTO2D a(1,2);
    PONTO2D b(2,3);
    PONTO2D c, z, y;
    cout << "a = " << a;
    cout << "b = " << b;
    c = a * b;
    cout << "c = a * b = "<< c;
    z = 2 * a;
    cout << "z = 2 * a = " << z;
    y = a * 2;
    cout << "y = a * 2 = " << y;
    PONTO3D d(1,2,4);
    cout << "D = "<< d;

    PONTO2D e;
    cout << "B = "<< b;
    cout << "e = ++b = ";
    e = ++b;
    cout << e;


    return 0;
}

















