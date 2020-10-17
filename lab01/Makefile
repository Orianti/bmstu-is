EXECS = program.out installer.out

BUILD_DIR = build

CC = gcc
CFLAGS = -Wall -Wextra -MMD
LDFLAGS =
LDLIBS = -lcrypto

SRCS = license/license.c # program.c and installer.c implide

OBJS = $(SRCS:%.c=$(BUILD_DIR)/%.o)
DEPS = $(OBJS:.o=.d)

TARGETS = $(addprefix $(BUILD_DIR)/,$(EXECS))

.PHONY: all
all: $(TARGETS)

$(TARGETS): %.out: %.o $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@ $(LDLIBS)

-include $(DEPS)

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) -c $(CFLAGS) $< -o $@

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
