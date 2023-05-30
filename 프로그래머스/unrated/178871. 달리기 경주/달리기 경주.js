function solution(players, callings) {
  const indexMap = {};

  for (let i = 0; i < players.length; i++) {
    indexMap[players[i]] = i;
  }

  for (let i = 0; i < callings.length; i++) {
    const calling = callings[i];
    const curIdx = indexMap[calling];
    const prevIdx = curIdx - 1;

    if (prevIdx >= 0) {
      [players[curIdx],players[prevIdx]] = [players[prevIdx],players[curIdx]];
      indexMap[calling] = prevIdx;
      indexMap[players[curIdx]] = curIdx;
    }
  }

  return players;
}
