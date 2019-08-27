#include <iostream>
#include <iomanip>
using namespace std;

int dx[8] = {2, 2, 1, 1, -2, -2, -1, -1};
int dy[8] = {1, -1, 2, -2, 1, -1, 2, -2};
static const int N = 100;
int tabla[N][N];
int n;
bool nasao;

void trazi(int x, int y, int k)
{
    if (nasao) return;
    if (x < 0 || y < 0 || x >= n || y >= n) return;
    if (tabla[x][y] > 0) return;

    tabla[x][y] = k;
    if (k == n * n) { nasao = true; return; }

    for(int potez = 0; potez < 8; potez++)
        trazi(x + dx[potez], y + dy[potez], k + 1);

    if (!nasao) tabla[x][y] = 0;
}

int main()
{
    n = 6;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            tabla[i][j] = 0;

    nasao = false;
    trazi(0, 0, 1);
    if (!nasao) { cout << "Nemoguce" << endl; return 0; }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++) cout << setw(6) << tabla[i][j] << " ";
        cout << endl;
    }
    return 0;
}
