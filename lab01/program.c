#include <stdio.h>

#include "license/license.h"

int main()
{
    printf("Checking license..\n");
    if (check_license() != EXIT_SUCCESS) {
        fprintf(stderr, "Can't find a license file!\n");
        return -1;
    }

    printf("Program started successfully.\n");

    return 0;
}
