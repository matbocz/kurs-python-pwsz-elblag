#include<stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h> 

bool is_lower(char txt[]) {
	for (int i = 0; i < strlen(txt); i++) {
		if (txt[i] >= 65 && txt[i] <= 90) {
			return false;
		}
	}

	return true;
}

int main()
{
	char txt[] = "lorem ipsum";
	clock_t t1, t2, t3, t4;

	// Test 10
	t1 = clock();
	for (int i = 0; i < 10; i++) {
		is_lower(txt);
	}
	t1 = clock() - t1;

	// Test 1000
	t2 = clock();
	for (int i = 0; i < 1000; i++) {
		is_lower(txt);
	}
	t2 = clock() - t2;

	// Test 100 000
	t3 = clock();
	for (int i = 0; i < 100000; i++) {
		is_lower(txt);
	}
	t3 = clock() - t3;

	// Test 10 000 000
	t4 = clock();
	for (int i = 0; i < 10000000; i++) {
		is_lower(txt);
	}
	t4 = clock() - t4;

	printf("Time(10): %f \n", ((double)t1) / CLOCKS_PER_SEC);
	printf("Time(1000): %f \n", ((double)t2) / CLOCKS_PER_SEC);
	printf("Time(100 000): %f \n", ((double)t3) / CLOCKS_PER_SEC);
	printf("Time(10 000 000): %f \n", ((double)t4) / CLOCKS_PER_SEC);
}