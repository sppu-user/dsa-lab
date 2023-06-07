#include<iostream>
#include<string>

#define N 20
#define SERIOUS 10
#define NONSERIOUS 5
#define CHECKUP 1

using namespace std;
string q[N];
int pr[N];
int r=-1,f=-1;

void enqueue(string data, int p)//inserting the data in queue 
{
    int i;
    if ((f==0)&&(r==N-1))//checks the queue is full or not
    {
        cout<<"Queue is full!";
    }
    else
    {
        if (f==-1)//checks if queue is empty
        {
            f=r=0;
            q[r]=data;
            pr[r]=p;
        }
        else if (r==N-1)//check if there are some elements
        {
            for (i = f; i <= r; i++)
            {
                q[i-f] = q[i];
                pr[i-f] = pr[i];
                r=r-f;
                f=0;
                for (i = r; i > f; i--)
                {
                    if (p>pr[i])
                    {
                        q[i+1] = q[i];
                        pr[i+1] = pr[i];
                    }
                    else break;
                    q[i+1] = data;
                    pr[i+1] = p;
                    r++;
                }
            }
        }
        else
        {
            for (i = r; i >= f; i--)
            {
                if (p>pr[i])
                {
                    q[i+1] = q[i];
                    pr[i+1] = pr[i];
                }
                else break;
            }
            
            q[i+1] = data;
            pr[i+1] = p;
            r++;
        }
            
    }
}
    
void print()//print data of queue
{
    int i;
    for (i = f; i <= r; i++)
    {
        cout<<"Patients name is: "<<q[i];
        switch (pr[i])
        {
            case 1:
                cout<<"\nPrioirty is 'Checkup' "<<endl;
            break;

            case 5:
                cout<<"\nPrioirty is 'Non-Serious' "<<endl;
            break;

            case 10:
                cout<<"\nPrioirty is 'Serious' "<<endl;
            break;

            default:
                cout<<"Priority not found!"<<endl;
            break;
        }
    }
}

void dequeue()//remove the data fom fomnt end
{
    if (f==-1)
    {
        cout<<"Queue is empty!"<<endl;
    }
    else
    {
        cout<<"deleted element = "<<q[f]<<endl;
        cout<<"Its Priority = "<<pr[f]<<endl;
        if (f==r) f = r = -1;
        else f++;
    }
}


int main()
{
    string data;
    int opt,n,i,p;
    cout<<"Enter your choice: "<<endl;
    do
    {
        cout<<"Press '1' to insert data "<<endl<<"Press '2' to show the data "<<endl<<"Press '3' for delete the data "<<endl<<"Press '0' for exit!"<<endl;
        cin>>opt;
        switch (opt)
        {
            case 1:
                cout<<"Enter the number of patients:\n ";
                cin>>n;
                i=0;
                while(i<n)
                {
                    cout<<"Enter name of the patient: "<<endl;
                    cin>>data;
                    back:
                        cout<<"Enter your priorities (0: serious, 1:Non-serious, 2:general checkup) : ";
                        cin>>p;
                        switch (p)
                        {
                            case 0:
                                enqueue(data,SERIOUS);
                            break;

                            case 1:
                                enqueue(data,NONSERIOUS);
                            break;

                            case 2:
                                enqueue(data,CHECKUP);
                            break;
                        default:
                            goto back;
                            //break;
                        }
                    i++;
                }
            break;
            
            case 2:
                print();
            break;

            case 3:
                dequeue();
            break;

            case 0:
                cout<<"Exit!"<<endl;
            break;
            default:
                cout<<"Enter valid choice!"<<endl;
            break;
        }    
    } while (opt!=0);
    return 0;
}
