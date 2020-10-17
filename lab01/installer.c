#include <stdio.h>
#include <stdlib.h>

#include "license/license.h"

int main()
{
	printf("Installing..\n");
	if (create_license() != EXIT_SUCCESS) {
		fprintf(stderr, "Can't create a license file!\n");
		return EXIT_FAILURE;
	}

	printf("Installation completed successfully.\n");

	return EXIT_SUCCESS;
}
