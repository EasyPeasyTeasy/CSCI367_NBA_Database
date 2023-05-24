






const InputVal = document.getElementById('search');//input box
const results = document.getElementById('results');//reults box
const toggleArrow = document.getElementsByClassName("toggleSort");
const selectBox = document.getElementById('exampleSelect1');
const clearInput = document.getElementById('clearInput');
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


const people = [
  { name: 'jim', job: 'sales', age: 27, id: 1 },
  { name: 'dwight', job: '<em>"asstistant regional manager"</em>', age: 38, id: 2 },
  { name: 'kevin', job: 'accounting', age: 40, id: 3 },
  { name: 'oscar', job: 'accounting', age: 29, id: 4 },
  { name: 'stan', job: 'accounting', age: 44, id: 5 },
  { name: 'creed', job: 'quality control', age: 52, id: 6 },
  { name: 'stanley', job: 'sales', age: 39, id: 7 },
  { name: 'nardoggs', job: 'former manager', age: 28, id: 8 }
];



if (selectBox.addEventListener) {
  selectBox.addEventListener('input', () => {
    RealChange();
  }, false);
} else if (InputVal.attachEvent) {  
  selectBox.attachEvent('onpropertychange', () => {
    RealChange();
  });
}


(buildSelect = () => {
  var buildKeys = Object.keys(people[0]).map((keys) => {
    
    selectBox.insertAdjacentHTML('beforeend', '<option target="' + keys + '">' + keys + '</option>');
  });
})();




if (InputVal.addEventListener) {
  InputVal.addEventListener('input', () => {
    RealChange();
  }, false);
} else if (InputVal.attachEvent) {  
  InputVal.attachEvent('onpropertychange', () => {
    RealChange();
  });
}





  (RealChange = () => {
    
    
    
  const SelectedSearchVal = selectBox.value;
  const v = InputVal.value; 
    
  
  InputVal.setAttribute("placeholder", "Search NBA Players by " + SelectedSearchVal +" ");
    
  results.innerHTML="";
   
   
    
    const t = people.filter((x) => {
      
     let searchKey = x[SelectedSearchVal];
      
     if (typeof searchKey === 'string' || searchKey instanceof String) {
       
      return  searchKey.includes(v);
       
     } else {
      
       return  searchKey.toString().includes(v);
       
     }
      
    });
      if(t.length < 1) {
          results.insertAdjacentHTML('afterbegin', 'No Results');
  }
    t.map((str, count) => {
      count = count +1;
     
results.insertAdjacentHTML('beforeend', '<tr class="' + `${(count % 2  == 0 ? "" : "bg-light")}` + ' "><th scope="row">' + str.id +'</th><td>' +  str.name + '</td><td>' + str.job + '</td><td>' + str.age + '</td><tr>');
      
    });
    
    if(InputVal.value !== "") {
        clearInput.setAttribute("style", "display:block; ");                      
    } else {
        clearInput.setAttribute("style", "display:none; "); 
    }
    
    
  })();





const sortCol = function() {
  
  results.innerHTML="";
  
  let attribute = this.getAttribute("toggle");
  let parent = this.parentElement;
  let parentAttribute = parent.getAttribute('target');
  
  
  const s = people.sort((a, b) => {
    
    
    let Akey = a[parentAttribute];
    let Bkey = b[parentAttribute];
    
    
    if (typeof Akey === 'string' || Akey instanceof String) {
      var nameA = Akey.toUpperCase(); // ignore upper and lowercase
      var nameB = Bkey.toUpperCase(); // ignore upper and lowercase
      if (nameA < nameB) { return -1; }
      if (nameA > nameB) { return 1; }
      return 0;
    } else {
      
       return Akey - Bkey;
    }
    
  });
  
    
    if(attribute == 'false' ) {
      
      this.setAttribute("toggle", "true");
      this.classList.remove('fa-arrow-down');
      this.classList.add('fa-arrow-up');
      
      
      s.map((str, count) => {
        count = count +1;//counter
        
        
        results.insertAdjacentHTML('beforeend', '<tr class="' + `${(count % 2  == 0 ? "" : "bg-light")}` + ' "><th scope="row">' + str.id +'</th><td>' +  str.name + '</td><td>' + str.job + '</td><td>' + str.age + '</td><tr>');
        
      });//s.map
      
    }  else {
      
      this.setAttribute("toggle", "false");
      this.classList.remove('fa-arrow-up');
      this.classList.add('fa-arrow-down');

      s.reverse().map((str, count) => {
        count = count +1;
        
        results.insertAdjacentHTML('beforeend', '<tr class="' + `${(count % 2  == 0 ? "" : "bg-light")}` + ' "><th scope="row">' + str.id +'</th><td>' +  str.name + '</td><td>' + str.job + '</td><td>' + str.age + '</td><tr>');
      
      }); 
      
    }
  
}



const getsortClass =  Array.from(toggleArrow).map((element) => {
   element.addEventListener('click', sortCol);
});






const reset = () => {
  InputVal.value = "";
  RealChange();
}
clearInput.addEventListener('click', reset);



