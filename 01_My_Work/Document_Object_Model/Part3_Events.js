var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");
console.log("Connected");

headOne.addEventListener("mouseover", function() {
  headOne.style.color = getRandomColor();
  headOne.textContent = "Mouse Currently Over";
})

headOne.addEventListener("mouseout", function() {
  headOne.textContent = "Hover Over Me!";
  headOne.style.color = 'black';
})

headTwo.addEventListener("click", function(){
  headTwo.textContent = 'CLICKED ON';
  headTwo.style.color = 'blue';
})

headThree.addEventListener('dblclick', function(){
  headThree.textContent = 'I WAS DOUBLE CLICKED';
  headThree.style.color = 'red';
})

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// function changeColor(thingy){
//   thingy.style.color = getRandomColor();
// }
