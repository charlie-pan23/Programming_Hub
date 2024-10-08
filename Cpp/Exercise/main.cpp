// CPT101 Practical Exercise 1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{
	char message1[] = "Give me a first number: ";
	char message2[] = "\bGive me a second number: ";
	char message3[] = "\nThe numbers are equal!\n";
	char message4[] = "\nThe numbers are not equal!\n";
	char message5[] = "Type in any integer and press ENTER key to finish: ";
	char format[] = "%d";	// format string for the scanf function

	int first;
	int second;
	int end;

	__asm {
		lea		eax, message1
		push	eax
		call	printf; printing the first message
		add		esp, 4

		lea		eax, first
		push	eax
		lea		eax, format
		push	eax
		call	scanf_s; reading the first number
		add		esp, 8

		lea		eax, message2
		push	eax
		call	printf; printing the second message
		add		esp, 4

		lea		eax, second
		push	eax
		lea		eax, format
		push	eax
		call	scanf_s; reading the second number
		add		esp, 8

		mov		eax, first
		sub		eax, second; compare two numbers, jump to nequal if flag is not zero
		jnz		nequal

		equal:
			lea		eax, message3
			push	eax
			call	printf; printing the third message
			add		esp, 4
			jmp		finish

		nequal:
			lea		eax, message4
			push	eax
			call	printf; printing the fourth message
			add		esp, 4

		finish:
			lea		eax, message5
			push	eax
			call	printf; printing the fifth message
			add		esp, 4

			lea		eax, end
			push	eax
			lea		eax, format
			push	eax
			call	scanf_s; reading any integer to end program
			add		esp, 8
	}
	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started:
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
