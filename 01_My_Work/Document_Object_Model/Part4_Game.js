var resBut = document.querySelector("#restartButton");
var gameTiles = document.querySelectorAll("td");
//var currValue = 0;

resBut.addEventListener("click", function(){
  for(tile in gameTiles){
    gameTiles[tile].textContent = "";
  }
})

for(let tile = 0; tile < gameTiles.length; tile++){
  gameTiles[tile].addEventListener("click", function(){
    if(gameTiles[tile].textContent === ""){gameTiles[tile].textContent = "X";}
    else if (gameTiles[tile].textContent === "X") {gameTiles[tile].textContent = "O";}
    else if (gameTiles[tile].textContent === "O") {gameTiles[tile].textContent = "";}
  })
}

/* Given solution

function changeMarker(){
  if(this.textContent === '') {this.textContent = 'X';}
  else if (this.textContent === 'X') {this.textContent ='O';}
  else {this.textContent = '';}
}

for (var i = 0; i < squares.length; i++){
  squares[i].addEventListener('click',changeMarker)
}

*/
