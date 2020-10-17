#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>

#define UUID_SIZE 35

#define LICENSE_PATH "build/license.key"

int create_license();
bool check_license();
