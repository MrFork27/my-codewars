function oddOrEven(array) {
  return array.length === 0 || 
    array.reduce((prevItem, currentItem) => prevItem + currentItem) % 2 === 0 ?
    'even' :
    'odd'
}