function highAndLow(numbers){
  const numbersArray = numbers.split(' ').map(item => Number(item))
  
  return `${Math.max(...numbersArray)} ${Math.min(...numbersArray)}`
}