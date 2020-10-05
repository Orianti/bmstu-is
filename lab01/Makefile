CC=gcc
CFLAGS=-Wall -Wextra

# define any directories containing header files other than /usr/include
INCLUDES=

# define library paths in addition to /usr/lib
LFLAGS=

# define any libraries to link into executable
LIBS=-lcrypto

INSTALLER_SRCS=installer.c license/license.c
INSTALLER_OBJS=$(INSTALLER_SRCS:.c=.o)
PROGRAM_SRCS=program.c license/license.c
PROGRAM_OBJS=$(PROGRAM_SRCS:.c=.o)

all:	installer program
       
installer: $(INSTALLER_OBJS) 
	$(CC) -o installer $(INSTALLER_OBJS) $(LFLAGS) $(LIBS)

program: $(PROGRAM_OBJS)
	$(CC) -o program $(PROGRAM_OBJS) $(LFLAGS) $(LIBS)

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

clean:
	$(RM) *.o *~ installer program 
