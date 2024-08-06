export function decode(code: number[], n: number): string {
  const key_list = getKeyList(n)
  const ascii_string = code.map((element, index) => element - key_list[index % key_list.length] + "a".charCodeAt(0) - 1)
  return String.fromCharCode(...ascii_string)
}

function getKeyList(n: number): number[] {
  const digit_string = `${n}`
  return digit_string.split("").map((character) => Number(character))
}