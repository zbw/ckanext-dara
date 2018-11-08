var form = document.getElementById('resource-edit');
var button = document.getElementsByName('save')[0];

//Override form submission to do date validation
form.onsubmit = function(event){
    console.log('click');
    var start_date = document.getElementById('field-dara_temporalCoverageFormal');
    var end_date = document.getElementById('field-dara_temporalCoverageFormal_end');
    var valid = check_dates(start_date, end_date);
    start_date.setAttribute('required', '');
    end_date.setAttribute('required', '');

    console.log('valid::', valid);

    if (valid !== true){
        if (valid == 'start'){
            start_date.setAttribute('required', 'required');
        } else if (valid == 'end') {
            end_date.setAttribute('required', 'required');
        } else if (valid == 'order') {
            //start_date.setCustomValidity("The start date can't be after the end date.");
            end_date.setAttribute('required', 'required');
            end_date.setAttribute('min', start_date.value);
        } else {
            console.log('reset');
            start_date.setAttribute('required', '');
            end_date.setAttribute('required', '');
        }
        button.click();
        end_date.setAttribute('required', '');
        end_date.setAttribute('min', '');
        return false;
    } else {
        return true;
    }
}

function check_dates(start, end){
    console.log('checking');
    if (start.value.length > 0 && end.value.length == 0){
        return "end";
    }
    if (start.value.length == 0 && end.value.length > 0){
        return "start";
    }
    if (start.value > end.value){
        return "order";
    }

    return true;
}
