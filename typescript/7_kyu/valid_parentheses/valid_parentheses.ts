export function validParentheses(parenStr: string): boolean {
  const heap: string[] = []
  console.log(parenStr.split(""))
  try {
    parenStr.split("").forEach((character) => {
      if (character === "("){
        heap.push(character)
      } else if (character === ")"){
        if (heap.pop() === undefined){
          throw new Error()
        }
      }
    })
  } catch (error) {
    return false
  }
  
  return heap.length === 0
}
