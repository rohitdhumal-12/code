#include <iostream>
#include <vector>
using namespace std;

void print_board(vector<vector<int>>& board, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 1) {
                cout << " Q ";
            } else {
                cout << " _ ";
            }
        }
        cout << endl;
    }
}

bool is_safe(vector<vector<int>>& board, int col, int row, int N) {
    // Check this row on the left side
    for (int i = 0; i < col; i++) {
        if (board[row][i] == 1) return false;
    }

    // Check upper diagonal on the left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) return false;
    }

    // Check lower diagonal on the left side
    for (int i = row, j = col; i < N && j >= 0; i++, j--) {
        if (board[i][j] == 1) return false;
    }

    return true;
}

bool helper(vector<vector<int>>& board, int col, int N) {
    if (col >= N) return true;

    for (int i = 0; i < N; i++) {
        if (is_safe(board, col, i, N)) {
            // Place the queen
            board[i][col] = 1;
            cout << "Placing queen at row " << i << ", column " << col << endl;
            print_board(board, N);
            cout << endl;

            // Recur to place the rest of the queens
            if (helper(board, col + 1, N)) return true;

            // Backtrack: Remove the queen and print the state
            board[i][col] = 0;
            cout << "Backtracking from row " << i << ", column " << col << endl;
            print_board(board, N);
            cout << endl;
        }
    }
    return false;
}

int main() {
    int N;
    cout << "Enter No of Queens: ";
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N, 0));

    if (helper(board, 0, N)) {
        cout << "Final Solution:" << endl;
        print_board(board, N);
    } else {
        cout << "No solution exists for " << N << " Queens" << endl;
    }

    return 0;
}
