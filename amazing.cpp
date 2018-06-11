#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    bool transport(int **MT, int **M, int m, int n);

    int m, n;
    cout << "Please enter m and n: ";
    cin >> m >> n;

    int A[m][n], B[n][m];
    int i, j;
    cout << "Please enter matrix A" << endl;
    for (i = 0; i < m; i++)
    {
        cout << "please the element of line " << i + 1 << ":";
        for (j = 0; j < n; j++)
            cin >> A[i][j];
    }

    cout << "the transport B is" << endl;
    if (transport((int **)B, (int **)A, m, n))
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < m; j++)
                cout << B[i][j] << " ";
            cout << endl;
        }
    }

    return a.exec();
}
bool transport(int **MT, int **M, int m, int n)
{
    if (m == 0 || n == 0)
        return false;
    int i, j;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            *((int *)MT + m * j + i) = *((int *)M + n * i + j);
        }
    }
    return true;
}
