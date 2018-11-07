var form = document.getElementById('resource-edit');
var button = document.getElementsByName('save')[0];

//Override form submission to do date validation
form.onsubmit = function(event){
    var start_date = document.getElementById('field-dara_temporalCoverageFormal');
    var end_date = document.getElementById('field-dara_temporalCoverageFormal_end');
    var valid = check_dates(start_date, end_date);
    
    if (valid !== true){
        if (valid == 'start'){
            start_date.setAttribute('required', 'required');
        } else {
            end_date.setAttribute('required', 'required');
        }
        button.click();
        return false;
    } else {
        return true;
    }
}

function check_dates(start, end){
    if (start.value.length > 0 && end.value.length == 0){
        return "end";
    }
    if (start.value.length == 0 && end.value.length > 0){
        return "start";
    }
    return true;
}
