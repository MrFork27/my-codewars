export function hexHash(code: string): number {
  const hexChars = convertHexCharsFromCode(code);
  const sumHexChars = getSumHexChars(hexChars);

  return sumHexChars;
}

const convertHexCharsFromCode = (code: string): string[] => {
  const codeCharts = code.split("");

  return codeCharts.map((chart) => chart.charCodeAt(0).toString(16));
};

const getSumHexChars = (hexChars: string[]): number => {
  let sum = 0;
  hexChars.forEach((element) => {
    sum += computeSumCharNumbers(Array.from(element.replace(/\D/g, "")));
  });
  return sum;
};

const computeSumCharNumbers = (numbersString: string[]): number => {
  let sum = 0;
  numbersString.forEach((element) => {
    sum += parseInt(element);
  });
  return sum;
};
