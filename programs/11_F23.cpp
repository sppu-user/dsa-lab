#include<iostream>
#include<string>

using namespace std;


class student{
        public:
                int rollno;
                string name;
                char dob[10];

                bool operator==(const student &s){
                        return rollno = s.rollno;
                }
                
                bool operator<(const student &s){
                        return rollno < s.rollno;
                }
                friend ostream& operator<<(ostream &out, const student &);
                friend istream& operator>>(istream &in, const student &);
};

istream &operator>>(istream &in, student &s){
        cout<<"Enter the name:";
        in>>s.name;
        cout<<"Enter the roll no:";
        in>>s.rollno;
        cout<<"Enter the dob:";
        in>>s.dob;
        return in;
}

ostream &operator<<(ostream &out, const student &s){
        out<<s.rollno<<endl<<s.name<<endl<<s.dob;
        return out;
}

student read(){
        int n;
        student s;
        student arr[10];
        cout<<"ENter no of students:";
        cin>>n;
        for(int i=0; i<n;i++){
                cin>>s;
                arr[i]=s;
        }
}


int main()
{

        return 0;
}