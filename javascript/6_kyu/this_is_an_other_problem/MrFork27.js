class NamedOne {
  #firstName
  #lastName
  #fullName
  
  constructor(firstName, lastName) {
    this.#firstName = firstName
    this.#lastName = lastName
    this.#fullName = firstName + ' ' + lastName
  }
  
  get firstName() {
    return this.#firstName
  }
  
  set firstName(firstName) {
    this.#firstName = firstName
    this.#fullName = firstName + ' ' + this.#lastName
  }
  
  get lastName() {
    return this.#lastName
  }
  
  set lastName(lastName) {
    this.#lastName = lastName
    this.#fullName = this.firstName + ' ' + lastName
  }
  
  get fullName() {
    return this.#fullName
  }
  
  set fullName(fullName) {
    const names = fullName.split(' ')
    
    if (names.length === 2) {
      this.firstName = names[0]
      this.lastName = names[1]
    }
  }
}