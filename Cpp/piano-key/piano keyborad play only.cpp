#include <conio.h>
#include <iostream>
#include <windows.h>
#include <stdio.h>

#define M1 Beep(523,200);
#define M2 Beep(587,200);
#define M3 Beep(659,200);
#define M4 Beep(698,200);
#define M5 Beep(784,200);
#define M6 Beep(880,200);
#define M7 Beep(980,200);
//µÍÒô
#define L1 Beep(262,200);
#define L2 Beep(294,200);
#define L3 Beep(330,200);
#define L4 Beep(349,200);
#define L5 Beep(392,200);
#define L6 Beep(440,200);
#define L7 Beep(493,200);
//¸ßÒô
#define N1 Beep(532,200);
#define N2 Beep(588,200);
#define N3 Beep(660,200);
#define N4 Beep(698,200);
#define N5 Beep(784,200);
#define N6 Beep(880,200);
#define N7 Beep(988,200);
//°ëÏÒÒô
#define H1 Beep(1046,200);
#define H2 Beep(1175,200);
#define H3 Beep(1319,200);
#define H4 Beep(1397,200);
#define H5 Beep(1568,200);
#define H6 Beep(1760,200);
#define H7 Beep(1976,200);
#define N 1000      //ÇúÆ×µÄÒô½Ú

using namespace std;

int music[N];
int mcount = 0;

void play();        //Ñİ×à


//Ñİ×à
void play() {
	char ch;
	while (1) {
		if (kbhit()) {

			ch = getch();
			switch (ch) {
				case '1':
					H1;
					break;
				case '2':
					H2;
					break;
				case '3':
					H3;
					break;
				case '4':
					H4;
					break;
				case '5':
					H5;
					break;
				case '6':
					H6;
					break;
				case '7':
					H7;
					break;
				case 'q':
					N1;
					break;
				case 'w':
					N2;
					break;
				case 'e':
					N3;
					break;
				case 'r':
					N4;
					break;
				case 't':
					N5;
					break;
				case 'y':
					N6;
					break;
				case 'u':
					N7;
					break;
				case 'a':
					M1;
					break;
				case 's':
					M2;
					break;
				case 'd':
					M3;
					break;
				case 'f':
					M4;
					break;
				case 'g':
					M5;
					break;
				case 'h':
					M6;
					break;
				case 'j':
					M7;
					break;
				case 'z':
					L1;
					break;
				case 'x':
					L2;
					break;
				case 'c':
					L3;
					break;
				case 'v':
					L4;
					break;
				case 'b':
					L5;
					break;
				case 'n':
					L6;
					break;
				case 'm':
					L7;
					break;
				case '\033':
					return;
			}
		}
	}
}

int main() {
	play();
}
