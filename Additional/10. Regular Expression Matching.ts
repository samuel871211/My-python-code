function isMatch(s: string, p: string): boolean {
  const matchResult = s.match(p);
  if (!matchResult) return false;
  return matchResult[0] === s;
};
