CC=gcc
CFLAGS=-I.
DEPS =
OBJ = max-two.o


$(shell mkdir -p build)

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

max-two: $(OBJ)
	$(CC) -o build/$@ $^ $(CFLAGS)
