CC=gcc
CFLAGS=-I.
DEPS =
OBJ = point-poly.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

point-poly: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
