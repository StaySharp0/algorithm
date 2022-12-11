# Backtracking

모든 경우의 수를 전부 고려하는 알고리즘 상태공간을 트리로 나타낼 수 있을 때 적합한 방식이다. 일종의 트리 탐색 알고리즘이라고 봐도 된다. 방식에 따라서 깊이우선탐색(Depth First Search, DFS)과 너비우선탐색(Breadth First Search, BFS), 최선 우선 탐색(Best First Search/HeuristicSearch)이 있다. 모든 경우의 수를 고려해야 하는 문제라면, DFS가 낫다. BFS로도 구현이 물론 가능하지만, BFS로 구현했다간 큐의 크기가 . 심지어 속도도 똑같다. 따라서 경우의 수 구하기는 일반적으로 DFS가 편리하다. 대다수의 문제들은DFS를 써도 일단 답은 나온다.
-- 출처: 나무위키 --

조건에 맞지 않다면 바로 중단
