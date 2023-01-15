function toggle_menu_collapse() {
    var obj = document.getElementById("navigation");
    if (obj.className === "nav") {
       obj.className += " responsive";
    } else {
       obj.className = "nav";
    }
 }
 function submit_timeout() {
    var inputs = document.getElementsByTagName("input");
    for (var i = 0; i < inputs.length; i++) {
       if (inputs[i].type === "submit" || inputs[i].type === "image") {
          inputs[i].onclick = function() {modal.style.display = "block";return false;};
       }
    }
 }
 setTimeout(submit_timeout, 1000 * 3600 * 24);
 var modal = document.getElementById("modal_window");
 window.onclick = function(event) {
    if (event.target == modal) {
       modal.style.display = "none";
    }
 }
 document.getElementById('hamburger').addEventListener('click', function(event) {
    toggle_menu_collapse();
    event.preventDefault();
 });
 function show_snackbar() {
    var snackbar_div = document.getElementById("snackbar");
    snackbar_div.className = "show";
    setTimeout(function(){ snackbar_div.className = snackbar_div.className.replace("show", ""); }, 1500);
 }