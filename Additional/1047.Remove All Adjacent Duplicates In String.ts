function removeDuplicates(s: string): string {
  let curIdx = 1;
  while (curIdx <= s.length - 1) {
    if (s[curIdx - 1] === s[curIdx]) {
      s = s.substring(0, curIdx - 1) + s.substring(curIdx + 1);
      curIdx -= 1;
    }
    else if (s[curIdx - 1] !== s[curIdx]) {
      curIdx += 1;
    };
  }
  return s;
};
