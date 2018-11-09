/***********************************************
 *                                             *
 * Show and hide author field in resource form *
 *                                             *
 ***********************************************/

var toggleOn = document.getElementById('author_toggle_on');
var toggleOff = document.getElementById('author_toggle_off');
var author_section = document.getElementById('resource_authors_section');
var button_section = document.getElementById('add_authors_selection');
var message = document.getElementById('message');

toggleOn.addEventListener('click', function(event){
    author_section.style.display = 'block';
    message.innerHTML = "Remove authors";
    toggleOn.style.display = "none";
    toggleOff.style.display = "inline";
});


toggleOff.addEventListener('click', function(event){
    author_section.style.display = 'none';
    message.innerHTML = "Add authors, if different from the previous page";
    toggleOff.style.display = "none";
    toggleOn.style.display = "inline";
    clearAuthors();
});

function clearAuthors(){
    var targets = document.getElementsByName('dara_authors');
    for (i=0; i<targets.length; i++){
        console.log(targets[i].value);
        targets[i].value = "";
        console.log(targets[i].value);
    }
}
