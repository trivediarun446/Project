#include<iostream>

using namespace std ; 


void Frame(int ln , int b )
{
     for( int i = 0 ; i < b ; i++ )
     {
        for( int j = 0 ; j < ln ; j++)
        {
            if( i == 0 || i == b-1)
            {
                cout << "* " ; 
            }
            else{
                if( j == 0 || j == ln-1)
                {
                    cout << "*" ;
                }
                else{
                    cout << "  " ; 
                }
            }
        }
        cout << endl ; 
     }
}

int main ()
{
    int ln ; int b ;  
    cout << "Enter the length of frame " << endl ; 
    cin >> ln ;
    cout << "Enter the breath of frame" << endl ; 
    cin >> b ;  
    
    Frame(ln , b) ; 

}