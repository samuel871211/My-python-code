function romanToInt(s: string): number {
  let result = 0;
  const specialPatternToInt = {
    IV: 4,
    IX: 9,
    XL: 40,
    XC: 90,
    CD: 400,
    CM: 900
  };
  const regularPatternToInt: { [key: string]: number } = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  };
  for (const [specialPattern, int] of Object.entries(specialPatternToInt)) {
    if (s.match(specialPattern)) {
      s = s.replace(specialPattern, '');
      result += int;
    };
  };
  for (let idx = 0; idx < s.length; idx++) {
    result += regularPatternToInt[s[idx]];
  }
  return result;
};
