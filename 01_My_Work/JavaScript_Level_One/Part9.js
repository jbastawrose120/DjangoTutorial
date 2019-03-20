var fName = prompt("Hello and Welcome. Please enter your First Name: ");
var lName = prompt("Please enter your Last Name: ");
var age = prompt("Please enter your age: ");
var height = prompt("Please enter your height in cm: ");
var petName = prompt("Please enter your pet's name: ");

// console.log("debug info");
// console.log("fName = " + fName);
// console.log("lName = " + lName);
// console.log("age = " + age);
// console.log("height = " + height);
// console.log("petName = " + petName);


if(fName[0] === lName[0]){
//  console.log(1);
  if(age > 20 && age < 30){
//    console.log(2);
    if(height >= 170){
  //    console.log(3);
      if(petName.substr(petName.length-1) === "y"){
        console.log("Secret Message!");
      }
    }
  }
}
