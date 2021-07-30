CC=gcc
CFLAGS=-I.
DEPS =
OBJ = floyd-algo.o


$(shell mkdir -p build)

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

floyd-algo: $(OBJ)
	$(CC) -o build/$@ $^ $(CFLAGS)
