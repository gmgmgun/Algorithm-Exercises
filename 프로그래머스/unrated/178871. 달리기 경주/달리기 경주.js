function solution(players, callings) {
  const indexMap = {};

  for (let i = 0; i < players.length; i++) {
    indexMap[players[i]] = i;
  }

  for (let i = 0; i < callings.length; i++) {
    const calling = callings[i];
    const currentIndex = indexMap[calling];
    const newIndex = currentIndex - 1;

    if (newIndex >= 0) {
      const temp = players[newIndex];
      players[newIndex] = players[currentIndex];
      players[currentIndex] = temp;
      indexMap[calling] = newIndex;
      indexMap[players[currentIndex]] = currentIndex;
    }
  }

  return players;
}



