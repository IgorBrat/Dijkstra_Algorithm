# Dijkstra Algorithm - GAMES-RV 
Having the information about the net topology (client-router connections) find server placement,
which will minimise the biggest ping to client.

Server can be placed in every vertex that is not a client.

## Input data:
In file `gamesrv.in` which has **M+2** lines:

- first line: `N and M` - count of vertexes and edges;
- second line: `list of natural numbers` - vertexes which are the clients (vertexes are indexed from 1 to N);
- the next M lines each: `startvertex, endvertex, latency` - latency between two given vertexes.

## Output data:
In file `gamesrv.out` has the result ping.