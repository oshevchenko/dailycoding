CC=gcc
CFLAGS=-I.
DEPS =
OBJ = point-poly.o


$(shell mkdir -p build)

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

point-poly: $(OBJ)
	$(CC) -o build/$@ $^ $(CFLAGS)
