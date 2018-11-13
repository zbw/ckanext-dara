/***********************************************
 *                                             *
 * Show and hide author field in resource form *
 *                                             *
 ***********************************************/

var targets = document.getElementsByName('dara_authors');
var populated = false;
for (var i=0; i<targets.length; i++){
    if (targets[i].value != ""){
        populated = true;
        break;
    }
}

var toggleOn = document.getElementById('author_toggle_on');
var toggleOff = document.getElementById('author_toggle_off');
var author_section = document.getElementById('resource_authors_section');
var button_section = document.getElementById('add_authors_selection');
var message = document.getElementById('message');

if (populated){
    author_section.style.display = 'block';
    message.innerHTML = "Remove authors";
    toggleOn.style.display = "none";
    toggleOff.style.display = "inline";
}

toggleOn.addEventListener('click', function(event){
    author_section.style.display = 'block';
    message.innerHTML = "Remove authors";
    toggleOn.style.display = "none";
    toggleOff.style.display = "inline";
});


toggleOff.addEventListener('click', function(event){
    author_section.style.display = 'none';
    message.innerHTML = "Creator (if the creator is not the author(s), please click to edit this field)";
    toggleOff.style.display = "none";
    toggleOn.style.display = "inline";
    clearAuthors();
});

function clearAuthors(){
    var targets = document.getElementsByName('dara_authors');
    var removal_buttons = document.getElementsByClassName('remove_author');
    for (var i=0; i<targets.length; i++){
        targets[i].value = "";
    }
    if (removal_buttons.length > 1){ 
        for (var i=removal_buttons.length-1; i>0; i--){
            removal_buttons[i].click();
        }
    }
}
