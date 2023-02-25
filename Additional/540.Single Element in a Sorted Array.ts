function singleNonDuplicate(nums: number[]): number {
  let idx = 0;
  for (const num of nums) {
    if (idx % 2 === 1 && num !== nums[idx - 1]) return nums[idx - 1];
    idx += 1;
  }
  return nums[nums.length - 1];
};
