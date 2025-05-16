//
// Created by borgescaua on 11/8/24.
//

#ifndef HORARIO_H
#define HORARIO_H
#include <iomanip>

class Horario {
public:
    Horario();
    Horario(int, int, int);
    void setHorario(int, int, int);
    void setHora(int);
    void setMinuto(int);
    void setSegundo(int);
    int getHora();
    int getMinuto();
    int getSegundo();
    void imprime();
private:
    int hora;
    int minuto;
    int segundo;
};

inline Horario::Horario() {
    hora = 0;
    minuto = 0;
    segundo = 0;
}

inline Horario::Horario(int h, int m, int s) {
    setHorario(h, m, s);
}

inline void Horario::setHorario(int h, int m, int s) {
    setHora(h);
    setMinuto(m);
    setSegundo(s);
}

inline void Horario::setHora(int h) {
    hora = (h >= 0 && h < 24) ? h : 0;
}

inline void Horario::setMinuto(int m) {
    minuto = (m >= 0 && m < 60) ? m : 0;
}

inline void Horario::setSegundo(int s) {
    segundo = (s >= 0 && s < 60) ? s : 0;
}

inline int Horario::getHora() {
    return hora;
}

inline int Horario::getMinuto() {
    return minuto;
}

inline int Horario::getSegundo() {
    return segundo;
}

inline void Horario::imprime() {
    std::cout << std::setfill( '0' ) << std::setw( 2 ) << hora << ":"
            << std::setw( 2 ) << minuto << ":"
            << std::setw( 2 ) << segundo<<std::endl;
}




#endif //HORARIO_H
