#include <bits/stdc++.h>

#define N 10
#define SERIOUS 10
#define NONSERIOUS 5
#define CHECKUP 1

using namespace std;

string name[N];
int priority[N];
int r = -1, f = -1;

void enqueue(string data, int prior)
{
    if ((f == 0) && (r = N - 1))
        cout << "Queue Full" << endl;
    else
    {
        if(f==-1){
            //Queue is empty
            f=r=0;
            name[r] = data;
            priority[r] = prior;
        }
        else{

        }
    }
}

void dequeue()
{
    if(f==-1)
        cout<<"Empty Queue"<<endl;
    else{
        cout<<"Deleting Patient of name "<<name[f];
    }
}

void display()
{
    for(int i = 0; i<=r; i++){
         cout<<"Patients name is "<<name[i];
        switch (priority[i])
        {
            case 1:
                cout<<"\nPrioirty : 'Checkup' "<<endl;
            break;

            case 5:
                cout<<"\nPrioirty : 'Non-Serious' "<<endl;
            break;

            case 10:
                cout<<"\nPrioirty : 'Serious' "<<endl;
            break;

            default:
                cout<<"Priority not found!"<<endl;
            break;
        }
    }
}

int main()
{
    string data;
    bool on = true;
    int p, choice;
    cout << "[0] Exit" << endl;
    cout << "[1] Insert" << endl;
    cout << "[2] Remove" << endl;
    cout << "[3] Display" << endl;
    cout << "Enter your choice (0-3)";
    cin >> choice;
    do
    {
        switch (choice)
        {
        case 1:
            enqueue(data, p);
            break;

        case 2:
            enqueue(data, p);
            break;

        case 3:
            enqueue(data, p);
            break;

        case 0:
            on = false;
            break;

        default:
            cout << "Invalid choice!";
            break;
        }
    } while (on);
    return 0;
}