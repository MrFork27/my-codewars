function divisors(integer) {
  const integerDivisors = []
  
  for(let i = 2; i < integer; i++) {
    if (integer % i === 0) {
      integerDivisors.push(i)
    }
  }
  
  return integerDivisors.length === 0 ? `${integer} is prime` : integerDivisors
};