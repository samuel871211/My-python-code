function checkStraightLine(coordinates: number[][]): boolean {
  const [x1, y1] = coordinates[0];
  const [x2, y2] = coordinates[1];
  const standardSlope = x2 > x1 ? (x2 - x1) / (y2 - y1) : (x1 - x2) / (y1 - y2);
  for (let idx = 2; idx <= coordinates.length - 1; idx++) {
    const [x1, y1] = coordinates[idx - 1];
    const [x2, y2] = coordinates[idx];
    const curSlope = x2 > x1 ? (x2 - x1) / (y2 - y1) : (x1 - x2) / (y1 - y2);
    if (curSlope != standardSlope) return false;
  }
  return true;
};
