#include<iostream>
#include<cstring>
using namespace std;
int plm[5][5], plw[5][5], stableset[5][5];
int mFree[5], wFree[5];
int wPrefersM1OverM(int w, int m, int m1, int N)
{
    for (int i = 0; i < N; i++)
    {
        if (plw[w][i] == m1)
            return 1;
        if (plw[w][i] == m)
            return 0;
    }
}
void stability(int N)
{
    int x, y;
    memset(stableset, 0, sizeof(stableset));
    memset(mFree, 0, sizeof(mFree));
    memset(wFree, 0, sizeof(wFree));
    int freeCount = N;
    while (freeCount > 0)
    {
        int m;
        for (m = 0; m < N; m++)
            if (mFree[m] == 0)
                break;
        for (int i = 0; i < N && mFree[m] == 0; i++)
        {
            int w = plm[m][i];
            if (wFree[w] == 0)
            {
                stableset[m][w] = 1;
                mFree[m] = 1;
                wFree[w] = 1;
                freeCount--;
            }

            else
            {
                int m1;
                for (int k = 0; k < N; k++)
                    if (stableset[k][w] == 1)
                    {
                        m1 = k;
                        break;
                    }
                if (wPrefersM1OverM(w, m, m1, N) == 0)
                {
                    stableset[m1][w] = 0;
                    stableset[m][w] = 1;
                    mFree[m] = 1;
                    mFree[m1] = 0;
                }
            }
        }
    }
    cout << "Woman   Man" << endl;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (stableset[i][j] == 1) {
                x = (j + 86);
                y = (i + 65);
                cout << " " << (char)x << "\t" << (char)y << endl;
            }
}
int main() {
    int m;
    char a, b;
    int x, y;
    cout << "enter number of men and women" << endl;
    cin >> m;
    cout << "enter preference list of men" << endl;
    for (int i = 0; i < m; i++) {
        cout << "enter preference of man" << i + 1 << endl;
        for (int j = 0; j < m; j++) {
            cin >> a;
            x = (int)a - 86;
            plm[i][j] = x;
        }
    }
    cout << "enter preference list of women" << endl;
    for (int i = 0; i < m; i++) {
        cout << "enter preference of woman" << i + 1 << endl;
        for (int j = 0; j < m; j++) {
            cin >> b;
            y = (int)b - 65;
            plw[i][j] = y;
        }
    }
    stability(m);
    return 0;

}
