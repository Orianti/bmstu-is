#include "license.h"

int get_uuid_hash(unsigned char *hash)
{
	/*
	 * /sys/class/dmi/id/product_uuid file access requires superuser
	 * rights. This is not entirely correct, because the program may not
	 * require running as superuser in general.
	 */
	FILE *fp = popen("sudo cat /sys/class/dmi/id/product_uuid", "r");
	if (fp == NULL) {
		return EXIT_FAILURE;
	}

	char uuid[UUID_SIZE];
	if (fgets(uuid, UUID_SIZE + 1, fp) == NULL) {
		pclose(fp);
		return EXIT_FAILURE;
	}

	if (SHA256((const unsigned char *)uuid, UUID_SIZE, hash) == NULL) {
		pclose(fp);
		return EXIT_FAILURE;
	}

	pclose(fp);
	return EXIT_SUCCESS;
}

int create_license()
{
	unsigned char hash[SHA256_DIGEST_LENGTH];
	if (get_uuid_hash(hash) != 0) {
		return EXIT_FAILURE;
	}

	FILE *fd = fopen(LICENSE_PATH, "w");
		if (fd == NULL) {
			return EXIT_FAILURE;
		}
	for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
		fprintf(fd, "%02x", hash[i]);
	}

	fclose(fd);

	return EXIT_SUCCESS;
}

bool check_license()
{
	unsigned char hash[SHA256_DIGEST_LENGTH];
	if (get_uuid_hash(hash) != 0) {
		return false;
	}

	FILE *fd = fopen(LICENSE_PATH, "r");
	if (fd == NULL) {
		return false;
	}
	for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
		unsigned char c;
		fscanf(fd, "%02hhx", &c);
		if (hash[i] != c) {
			return false;
		}
	}

	return true;
}
