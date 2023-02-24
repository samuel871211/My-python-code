function reverse(x: number): number {
  const maxNumber = 2147483647;
  const minNumber = -2147483648;
  const positiveX = Math.abs(x);
  const reversedX =  x < 0 
    ? parseInt([...positiveX.toString()].reverse().join("")) * -1
    : parseInt([...positiveX.toString()].reverse().join(""));
  const result = reversedX > maxNumber || reversedX < minNumber ? 0 : reversedX;
  return result;
};
