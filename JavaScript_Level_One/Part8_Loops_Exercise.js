/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var temp = 0;
console.log("While loop #1");
while(temp < 5){
  console.log("Hello"+temp);
  temp++;
}

// For Loop
console.log("For Loop #1");
for(temp = 0; temp < 5; temp++){
  console.log("Hello"+temp);
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var num = 1;
console.log("While loop #2");
while(num < 26){
   if ((num % 2) === 1) {
     console.log(num);
   }
   num++;
 }

// METHOD TWO
// For Loop
console.log("For Loop #2");
for (num = 1; num <= 25; num++) {
  if (num % 2 === 1) {
    console.log(num);
  }
}
