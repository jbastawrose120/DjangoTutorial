// var initWeight = prompt("Input the number in lbs to be converted: ");
// var convertedWeight = initWeight * 0.454;
// alert(initWeight + " lbs converted to kgs is: " + convertedWeight);
// console.log("Conversion Completed");


var hot = false;
var temp = 100;
while (temp > -10){
if (temp > 80){
  console.log("Hot Outside!");
  temp -= 10;
}else if (temp <=80 && temp >= 50) {
  console.log("Average temp outside");
  temp -= 10;
}else if (temp < 50 && temp >= 32) {
  console.log("Kinda Cold");
  temp -= 10;
}else{
  console.log("Brrrrr");
  temp -= 10;
}

}
