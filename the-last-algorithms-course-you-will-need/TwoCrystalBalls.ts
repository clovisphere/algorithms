// Given two crystal balls that will break if dropped
// from high enough distance, determine the exact spot in which
// it will break in the most optimized way.

function twoCrystalBalls(breaks: boolean[]): number {
  const jumpLength = Math.floor(Math.sqrt(breaks.length));

  let i = jumpLength;
  for (; i < breaks.length; i += jumpLength) {
    if (breaks[i]) {
      break;
    }
  }

  i -= jumpLength;
  for (let j = i; j < i + jumpLength; ++j) {
    if (breaks[j]) {
      return j;
    }
  }
  return -1;
}
