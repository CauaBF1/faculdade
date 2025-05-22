//%%writefile soluc3.c
#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>


#define MAX_READERS 5

sem_t catraca, db, readerLimit; // semaforos para controle de entrada, local de acesso, limite de leitores 
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // proteger variavel readers
int readers = 0;
int consecutiveReaders = 0;
int waitingWriters = 0;
pthread_mutex_t countMutex = PTHREAD_MUTEX_INITIALIZER;

void *reader(void *arg) {
    long id = (long)arg;
    while (1) {
        // Verificação atômica se deve esperar por escritores
        pthread_mutex_lock(&countMutex);
        while (waitingWriters > 0 && consecutiveReaders >= MAX_READERS) {
            pthread_mutex_unlock(&countMutex);
            usleep(10000); // Pequena pausa para evitar busy waiting
            pthread_mutex_lock(&countMutex);
        }
        pthread_mutex_unlock(&countMutex);

        sem_wait(&readerLimit); // Garante limite de leitores

        sem_wait(&catraca);
        sem_post(&catraca);

        pthread_mutex_lock(&mutex);
        readers++;
        if (readers == 1) {
            sem_wait(&db);
        }
        pthread_mutex_lock(&countMutex);
        consecutiveReaders++;
        pthread_mutex_unlock(&countMutex);
        pthread_mutex_unlock(&mutex);


        printf("[Leitor %ld] Lendo... (Leitores ativos: %d | Leituras consecutivas: %d)\n",
               id, readers, consecutiveReaders);

        usleep(50000);

        pthread_mutex_lock(&mutex);
        readers--;
        printf("[Leitor %ld] Saiu. (Leitores ativos restantes: %d)\n", id, readers);
        if (readers == 0) {
            sem_post(&db);
        }
        pthread_mutex_unlock(&mutex);

        sem_post(&readerLimit);
    }
    return NULL;
}

void *writer(void *arg) {
    long id = (long)arg;
    while (1) {
        pthread_mutex_lock(&countMutex);
        waitingWriters++;
        pthread_mutex_unlock(&countMutex);

        sem_wait(&catraca);
        sem_wait(&db);
        sem_post(&catraca);

        printf("[Escritor %ld] Escrevendo... (Sala travada para leitores)\n", id);

        usleep(150000);

        printf("[Escritor %ld] Saiu. (Sala liberada para leitores)\n", id);
        sem_post(&db);

        pthread_mutex_lock(&countMutex);
        waitingWriters--;
        consecutiveReaders = 0; // Reset do contador
        pthread_mutex_unlock(&countMutex);

        // Pequena pausa para permitir entrada de leitores
        usleep(10000);
    }
    return NULL;
}

int main() {
    pthread_t r[7], w[3];
    
    sem_init(&catraca, 0, 1);
    sem_init(&db, 0, 1);
    sem_init(&readerLimit, 0, MAX_READERS); // Semáforo contador

    for (long i = 0; i < 7; i++)
        pthread_create(&r[i], NULL, reader, (void *)(i+1));
    for (long i = 0; i < 3; i++)
        pthread_create(&w[i], NULL, writer, (void *)(i+1));

    for (int i = 0; i < 7; i++) pthread_join(r[i], NULL);
    for (int i = 0; i < 3; i++) pthread_join(w[i], NULL);

    sem_destroy(&catraca);
    sem_destroy(&db);
    pthread_mutex_destroy(&mutex);
    sem_destroy(&readerLimit);
    pthread_mutex_destroy(&countMutex);

    return 0;
}
