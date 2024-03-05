function rowSumOddNumbers(n) {
  let currentNumber = n * (n - 1) + 1
  let numbersSum = 0
  
  for (let i = 0; i < n; i++) {
    numbersSum += currentNumber
    currentNumber += 2
  }
  
  return numbersSum
}