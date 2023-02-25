function maxArea(height: number[]): number {
  let curStartIdx = 0;
  let curEndIdx = height.length - 1;
  let result = 0;
  
  while (curStartIdx < curEndIdx) {
    const minHeight = Math.min(height[curStartIdx], height[curEndIdx]);
    const width = curEndIdx - curStartIdx;
    result = Math.max(result, minHeight * width);
    if (height[curEndIdx] < height[curStartIdx]) curEndIdx -= 1
    else curStartIdx += 1;
  }

  return result;
};
