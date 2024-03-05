function isIsogram(str){
  const strIgnoreCase = str.toLowerCase()
  const lettersSaved = []
  
  for (let i = 0; i < strIgnoreCase.length; i++) {
    const letter = strIgnoreCase[i]
    
    if (lettersSaved.includes(letter)) {
      return false
    }
    
    lettersSaved.push(letter)
  }
  
  return true
}