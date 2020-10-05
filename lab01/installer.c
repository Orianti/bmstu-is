#include <stdio.h>

#include "license/license.h"

int main()
{
    printf("Installing..\n");
    if (create_license() != 0) {
        fprintf(stderr, "Can't create a license file!\n");
        return -1;
    }

    printf("Installation completed successfully.\n");

    return 0;
}
