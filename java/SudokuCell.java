/**
 * In this kata you should implement an algorithm, that takes as a parameter index of small cell and 
 * return the index of bigger square, where this small cell is located.

For example:
0 -> 0
1 -> 0
2 -> 0

3 -> 1
4 -> 1
5 -> 1

73 -> 6
76 -> 7
79 -> 8
*/
public class SudokuCell {

    public static void main(String[] args) {
        System.out.println(SudokuCell.getSquare(40));
    }
    // Solution of other user: 
    
    // public static int getSquare(int n) {
    //     int line = n/27; // si es 9*9 tengo 27 lineas, 3 por cada cuadro de 3*3
    //     int rest = n-line*27;
    //     System.out.println(line);
    //     System.out.println(rest%9);
    //     return line*3 + rest % 9 / 3;
    // }
    public static int getSquare(int cellIndex) {
        int cellIndexDiv = cellIndex / 9;
        int cellIndexMod = cellIndex % 9; 

        if (cellIndexMod < 3) {
            if (cellIndexDiv == 0 || cellIndexDiv == 1 || cellIndexDiv == 2) {
                return 0;
            }
            if (cellIndexDiv == 3 || cellIndexDiv == 4 || cellIndexDiv == 5) {
                return 3;
            }
            if (cellIndexDiv == 6 || cellIndexDiv == 7 || cellIndexDiv == 8) {
                return 6;
            }
        }

        if (cellIndexMod > 2 && cellIndexMod < 6) {
            if (cellIndexDiv == 0 || cellIndexDiv == 1 || cellIndexDiv == 2) {
                return 1;
            }

            if (cellIndexDiv == 3 || cellIndexDiv == 4 || cellIndexDiv == 5) {
                return 4;
            }

            if (cellIndexDiv == 6 || cellIndexDiv == 7 || cellIndexDiv == 8) {
                return 7;
            }
        }

        if (cellIndexMod > 5) {
            if (cellIndexDiv == 0 || cellIndexDiv == 1 || cellIndexDiv == 2) {
                return 2;
            }

            if (cellIndexDiv == 3 || cellIndexDiv == 4 || cellIndexDiv == 5) {
                return 5;
            }

            if (cellIndexDiv == 6 || cellIndexDiv == 7 || cellIndexDiv == 8) {
                return 8;
            }
        }

        return 0;
    }
}