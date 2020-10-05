#include <stdio.h>
#include <stdlib.h>
#include <openssl/sha.h>

#define UUID_SIZE 35

#define LICENSE_PATH "license.key"

int get_uuid_hash(unsigned char *hash);
int create_license();
int check_license();