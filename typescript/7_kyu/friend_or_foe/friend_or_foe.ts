export function friend(friends: string[]): string[] { 
  return friends.filter(name => name.length === 4)
}