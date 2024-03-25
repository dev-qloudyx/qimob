
function openNav() {
    let sidebar = document.getElementById("mySidenav");
    let footer = document.getElementById("footer");
    let arrow = document.getElementById("arrow")
    
    if (sidebar.style.left === "-125px") {
        sidebar.style.left = "0";
        footer.style.left = "0px";
        arrow.style.rotate = "180deg";
        
    } 
    else if (sidebar.style.left === "0px") {
        sidebar.style.left = "-125px";
        footer.style.left = "-200px";
        arrow.style.rotate = "0deg";
    }
    else {
        sidebar.style.left = "0";
        footer.style.left = "0px";
        arrow.style.rotate = "180deg";
        
    }
}


let closeButton = document.getElementById('close');
let popup = document.getElementById('popup');
let overlay = document.getElementById('overlay');

function pop() {
  if(popup.style.display === 'none'){
    popup.style.display = 'block'; 
    overlay.style.display = 'block';
    console.log('hello')
  }
  else{
    popup.style.display = 'none';
    overlay.style.display = 'none';
    console.log('helloooo')
  }
    
}

function close() {
  if(overlay.style.display != 'none'){
    overlay.style.display = 'none';
    console.log('helloooo')
  }
 
}
  

closeButton.addEventListener('click', close);


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });

}


 