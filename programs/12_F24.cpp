#include<iostream>
#include<fstream>

using namespace std;

class employe{
    private:
        int code;
        char name[20];
        float salary;
    public:
        void read();
        void display();
        int getEmpCode(){
            return code;
        }
        int getSalary(){
            return salary;
        }
        void updateSalary(float s){
            salary = s;
        }
};

void employe::read(){
    
    cout<<"Enter Employee code:";
    cin>>code;
    
    cout<<"Enter Name:";
    cin>>name;
    
    cout<<"Enter salary:";
    cin>>salary;
}

void employe::display(){
    cout << code << " " << name << "\t" << salary << endl;
}


fstream file;

void appendToFile(){
    employe e;
    e.read();

    file.open("Emp.dat", ios::binary | ios::app);
    if(!file){
        cout<<"File not created";
        return;
    }

    file.write((char*)&e, sizeof(e));
    file.close();
}

void displayAll(){
    employe e;

    file.open("Emp.dat", ios::binary | ios::in);
    if(!file){
        return;
    }
    while(file){
        if(file.read((char*)&e, sizeof(e))){
            e.display();
        }
    }
}

int main(){

    remove("Emp.dat");

    displayAll();

    return 0;
}