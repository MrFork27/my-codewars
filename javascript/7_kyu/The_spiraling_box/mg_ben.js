function initializeMatrix(m, n){
  const output = new Array(n);
  for(let i = 0; i < output.length; i++){
    output[i] = new Array(m);
  }
  return output;
}

function fillMatrix(matrix){
  let m = matrix.length;
  let n = matrix[0].length;
  for(let i=0; i < m/2.0; i++){
    for(let j=0; j < n/2.0; j++){
      let i_inv = m-1 - i;
      let j_inv = n-1 - j;
      let value = Math.min(i, j)+1;
      matrix[i][j] = value;
      matrix[i][j_inv] = value;
      matrix[i_inv][j_inv] = value;
      matrix[i_inv][j] = value;
    }
  }
  return matrix;
}
function createBox(m, n) {
  return fillMatrix(initializeMatrix(m, n));
}