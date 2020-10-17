#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "license/license.h"

int main()
{
	printf("Checking license..\n");
	if (check_license() == false) {
		fprintf(stderr, "Error! License file is missing or damaged.\n");
		return EXIT_FAILURE;
	}

	printf("Program started successfully.\n");

	return EXIT_SUCCESS;
}
