function threeSum(nums: number[]): number[][] {
  nums = nums.sort((a, b) => a - b);
  const result: number[][] = [];
  for (let curIdx = 0; curIdx < nums.length - 2; curIdx++) {
    if (nums[curIdx] === nums[curIdx - 1]) continue;
    let startIdx = curIdx + 1;
    let endIdx = nums.length - 1;
    while (startIdx < endIdx) {
      const possibleAnswer = [nums[curIdx], nums[startIdx], nums[endIdx]];
      const sumOfPossibleAnswer = possibleAnswer.reduce((a, b) => a + b);
      if (sumOfPossibleAnswer > 0) endIdx -= 1;
      else if (sumOfPossibleAnswer < 0) startIdx += 1;
      else if (sumOfPossibleAnswer === 0) {
        if (result.length === 0) result.push(possibleAnswer);
        else {
          const [a,b,c] = result[result.length - 1];
          const [d,e,f] = possibleAnswer;
          if (!(a === d && b === e && c === f)) result.push(possibleAnswer);
        };
        endIdx -= 1;
        startIdx += 1;
      }
    }
  }
  return result;
};
