
# makefile was partially generated by the pymkfile.py script
CC=gcc
PYLIB=/opt/local/Library/Frameworks/Python.framework/Versions/3.2/lib/python3.2/config-3.2m/libpython3.2.a
PYINC=-I-I/opt/local/Library/Frameworks/Python.framework/Versions/3.2/include -I/opt/local/Library/Frameworks/Python.framework/Versions/3.2/include -I/opt/local/Library/Frameworks/Python.framework/Versions/3.2/include/python3.2m -I/opt/local/Library/Frameworks/Python.framework/Versions/3.2/include/python3.2m -I/usr/local/include
LIBS=-L/opt/local/Library/Frameworks/Python.framework/Versions/3.2/lib  -ldl  -framework CoreFoundation -lpbc -lgmp
OPTS=-DBUILD_PAIR -DBUILD_PBC -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes
PROGRAMS=test
OBJECTS=charm_embed_api.o test.o
all: $(PROGRAMS)

test: ${OBJECTS}
	${CC} ${OBJECTS} $(LIBS) $(PYLIB) -o test

charm_embed_api.o: charm_embed_api.c
	${CC} charm_embed_api.c -c $(PYINC) $(OPTS)

test.o: test.c
	${CC} test.c -c $(PYINC) $(OPTS)


clean:
	rm -f $(PROGRAMS) *.o *.pyc core
