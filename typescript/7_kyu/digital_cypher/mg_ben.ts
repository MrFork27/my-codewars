export function encode(str: String, n: number): number[] {
  const key_list = getKeyList(n)
  const result: number[] = []
  str.split("").forEach((character, index) => {
    result.push(convertToASCII(character) + key_list[index % key_list.length])
  })
  return result
}

function getKeyList(n: number): number[] {
  const digit_string = `${n}`
  return digit_string.split("").map((character) => Number(character))
}

function convertToASCII(letter: string): number {
  return letter.charCodeAt(0)-("a".charCodeAt(0)-1)
}