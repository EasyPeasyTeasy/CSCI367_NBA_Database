const names = [];
function selected() {
  var checkedBoxes = document.querySelectorAll('input[name=check1]:checked');

  if (checkedBoxes.length == 3) {
    var cbutton = document.getElementById('compared');
    cbutton.style.visibility = "visible";
    
    for (var i = 0; i < checkedBoxes.length; i++) {
      if (checkedBoxes[i].checked) {
          var row = checkedBoxes[i].parentNode.parentNode;
          names.push(row.cells[1].innerHTML);
          
      }
    }
  }
  else {
    var cbutton = document.getElementById('compared');
    cbutton.style.visibility = "hidden";
  }
  console.log(checkedBoxes)
}

function sendtoCompare() {
  var checkedBoxes = document.querySelectorAll('input[name=check1]:checked');
  var teams = [];
  var players = [];
  for (var i = 0; i < checkedBoxes.length; i++) {
    var values = checkedBoxes[i].value.split(",");
    players.push(values[0]);
    teams.push(values[1]);
  }
  console.log(players);
  console.log(teams);

  var url = "/compare?name1=" + players[0] + "&name2="+ players[1] + "&name3=" + players[2] + "&team1=" + teams[0]+ "&team2=" + teams[1]+ "&team3=" + teams[2];
  location.href = url;
}

