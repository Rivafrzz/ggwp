#include <iostream>
#define MAX 5
using namespace std;

struct Antrian {
    int data[MAX];
    int head;
    int tail;
};

Antrian antre;

void create(){
    antre.head = antre.tail = -1;
}

bool isEmpty(){
    if(antre.tail == -1){
        return true;
    }
    else{
        return false;
    }
}

bool isFull(){
    if(antre.tail == MAX ){
            return true;
    }else {
        return false;
    }
}


void enqueue(int data){
    if(isFull()){
        cout<<"Antrian sudah penuh\n";
    }else{
        if(isEmpty()){

            antre.head = antre.tail = 0;
            antre.data[antre.tail] = data;
            antre.head++;
            antre.tail++;
        }else{

            antre.data[antre.tail] = data;
            antre.tail++;
            cout<<data<<" masuk kedalam antrian\n";
        }
    }

}



int dequeu(){
    if(isEmpty()){
        cout<<"Antrian kosong";
    }else{
        int e = antre.data[antre.head];
        for(int i=0;i<antre.tail;i++){
            antre.data[i] = antre.data[i+1];
        }
        antre.tail--;
        return e;
    }


}

void tampil(){
    cout<<"\nData antrian : \n";
    if(isEmpty()){
        cout<<"Antrian kosong\n";
    }else{
        for(int i = 0;i<MAX;i++){
            if(antre.data[i] == NULL){
                cout<<i+1<<". Data Kosong\n";
            }else{
                cout<<i+1<<". "<<antre.data[i]<<endl;
            }
        }
    }
    cout<<endl<<endl;
}


int main()
{
    int pilih,indata; //pilih program
    pilihprogram:
    cout<<"Pilih program\n";

    cout<<"1. Menambahkan data\n";
    cout<<"2. Menghapus data\n";
    cout<<"3. Menampilkan data\n";

    cout<<"\n Masukan Pilihan : \n";
    cin>>pilih;

    switch(pilih){
        case 1 : cout<<"Masuakan data : ";
                 cin>>indata;
                 enqueue(indata);goto pilihprogram;
        break;

        case 2 : cout<<"Hapus data : \n";
                 dequeu();goto pilihprogram;
        break;

        case 3 : cout<<"Tampilkan data : \n";
                 tampil();goto pilihprogram;
        break;

        default :cout<<"TIDAK ADA PILIHAN";
        break;
    }


    return
