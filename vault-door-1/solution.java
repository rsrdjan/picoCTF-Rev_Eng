import java.util.*;

class Solution {
        public static void main(String args[])
        {
                Solution solution = new Solution();
                char[] flag_missing = new char[32];
                flag_missing[0]  = 'd';
                flag_missing[29] = '3';
                flag_missing[4]  = 'r';
                flag_missing[2]  = '5';
                flag_missing[23] = 'r';
                flag_missing[3]  = 'c';
                flag_missing[17] = '4';
                flag_missing[1]  = '3';
                flag_missing[7]  = 'b';
                flag_missing[10] = '_';
                flag_missing[5]  = '4';
                flag_missing[9]  = '3';
                flag_missing[11] = 't';
                flag_missing[15] = 'c';
                flag_missing[8]  = 'l';
                flag_missing[12] = 'H';
                flag_missing[20] = 'c';
                flag_missing[14] = '_';
                flag_missing[6]  = 'm';
                flag_missing[24] = '5';
                flag_missing[18] = 'r';
                flag_missing[13] = '3';
                flag_missing[19] = '4';
                flag_missing[21] = 'T';
                flag_missing[16] = 'H';
                flag_missing[27] = 'f';
                flag_missing[30] = 'b';
                flag_missing[25] = '_';
                flag_missing[22] = '3';
                flag_missing[28] = '6';
                flag_missing[26] = 'f';
                flag_missing[31] = '0';

                System.out.print("picoCTF{");
                for (int i=0; i < 32; i++)
                {
                        System.out.print(flag_missing[i]);
                }
                System.out.print('}');
        }
