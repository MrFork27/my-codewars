function checkExam(array1, array2) {
  var score = 0
  array2.forEach((element, index) => {
    if(element != ""){
      if(element == array1[index]){
        score+=4
      }else{
        score-=1
      }
    }
  });
  return score = score < 0 ? 0 : score;
}