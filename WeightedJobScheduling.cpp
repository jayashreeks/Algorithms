#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Job
{
    int start, finish, profit;
};

struct weightedJob
{
    vector<Job> job;
    int value;
};

bool jobComparator(Job s1, Job s2)
{
    return (s1.finish < s2.finish);
}

int binsearch(Job jobs[], int index)
{
    // Initialize 'lo' and 'hi' for Binary Search 
    int lo = 0, hi = index - 1;

    // Perform binary Search iteratively 
    while (lo <= hi)
    {
        int mid = (lo + hi) / 2;
        if (jobs[mid].finish <= jobs[index].start)
        {
            if (jobs[mid + 1].finish <= jobs[index].start)
                lo = mid + 1;
            else
                return mid;
        }
        else
            hi = mid - 1;
    }

    return -1;
}
void WIS(Job arr[], int n)
{
    sort(arr, arr + n, jobComparator);

    weightedJob DP[n];

    DP[0].value = arr[0].profit;
    DP[0].job.push_back(arr[0]);

    for (int i = 1; i < n; i++)
    {
        int inclProf = arr[i].profit;
        int l = binsearch(arr, i);
        if (l != -1)
            inclProf += DP[l].value;

        if (inclProf > DP[i - 1].value)
        {
            DP[i].value = inclProf;
            DP[i].job = DP[l].job;
            DP[i].job.push_back(arr[i]);

        }
        else
            // excluding the current job 
            DP[i] = DP[i - 1];
    }
    cout << "Optimal Jobs for maximum profits are\n";
    for (int i = 0; i < DP[n - 1].job.size(); i++)
    {
        Job j = DP[n - 1].job[i];
        cout << "(" << j.start << ", " << j.finish << ", " << j.profit << ")" << endl;
    }
    cout << "\nTotal Optimal profit is " << DP[n - 1].value;
}

int main()
{
    Job arr[] = { {1, 2, 100}, {2, 5, 200}, {3,6, 300},
        {4,8, 400},{5,9,500},{6,10,100} };
    int n = sizeof(arr) / sizeof(arr[0]);

    WIS(arr, n);

    return 0;
}