#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int dx[8] = {2, 2, 1, 1, -2, -2, -1, -1};
int dy[8] = {1, -1, 2, -2, 1, -1, 2, -2};
static const int N = 100;
int tabla[N][N];
int n;
bool nasao;

struct Potez {int dx; int dy; int nastavaka;};
bool BoljiPotez(Potez& p1, Potez& p2) {return p1.nastavaka < p2.nastavaka;}

void trazi(int x, int y, int k)
{
    if (nasao) return;
    if (x < 0 || y < 0 || x >= n || y >= n) return;
    if (tabla[x][y] > 0) return;

    tabla[x][y] = k;
    if (k == n * n) { nasao = true; return; }

    Potez potezi[8];
    for(int potez1 = 0; potez1 < 8; potez1++)
    {
        potezi[potez1].nastavaka = 0;
        int x1=x+dx[potez1];
        int y1=y+dy[potez1];
        if (x1 >= 0 && y1 >= 0 && x1 < n && y1 < n && tabla[x1][y1] == 0)
        {
            for(int potez2 = 0; potez2 < 8; potez2++)
            {
                int x2 = x1 + dx[potez2];
                int y2 = y1 + dy[potez2];
                if (x2 >= 0 && y2 >= 0 && x2 < n && y2 < n && tabla[x2][y2] == 0)
                    potezi[potez1].nastavaka++;
            }
        }
    }

    for (int i = 0; i < 8; i++) {potezi[i].dx = dx[i]; potezi[i].dy = dy[i];}
    sort(potezi, potezi+8, BoljiPotez);
    for(int potez1 = 0; potez1 < 8; potez1++)
        trazi(x + potezi[potez1].dx, y + potezi[potez1].dy, k + 1);

    if (!nasao) tabla[x][y] = 0;
}

int main()
{
    n = 35;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            tabla[i][j] = 0;

    nasao = false;
    trazi(0, 0, 1);
    if (nasao)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++) cout << setw(4) << tabla[i][j] << " ";
            cout << endl;
        }
    }
    else cout << "Nemoguce" << endl;
    return 0;
}
