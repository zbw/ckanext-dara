"use strict";


var ws_objects = []
econws();

function econws() {
   var inputs = document.querySelectorAll( '.econws_input' );
   _.each(inputs, function(inp) {
        inp.oninput = function() {
            var val = inp.value;
            if(val.length < 2) return;
    
            if(val.indexOf('http://d-nb.info/gnd/') != -1) {
                update_fields(inp, val);
                return
            }
            
            wscall(val);

        }
    });
}


function update_fields (inp, val) {
    // TODO remove jquery

    var authorfields = $(inp).closest('fieldset.author');  
    var firstname = $(authorfields).find('[data-author="firstname"]');
    var aid = $(authorfields).find('[data-author="authorID"]');
    var aid_type = $(authorfields).find('[data-author="authorID_Type"]');
    var author = _.find(_.flatten(ws_objects, true), function (ob) { 
        return ob.concept.value === val; 
    });
    var url = $(authorfields).find('[data-author="url"]');
    var authorname = author.prefName.value.split(", ");
    
    inp.value=authorname[0];
    $(firstname).val(authorname[1]);
    $(aid).val(author.concept.value.replace('http://d-nb.info/gnd/', ''));
    $(aid_type).val('GND');
    $(url).val(author.concept.value);
    
    $(aid_type).prop('disabled', false);
    $(aid_type).prop('required', true);

    return;
}


function wscall(val) {
    $.ajax({
        url: "http://zbw.eu/beta/econ-ws/suggest2",
        dataType: "json",
        async: true,
        data: {
            query: val,
            dataset: 'econ_pers',
            limit: 15
        },
        success: function ( data ){
            var datalist = document.querySelector('#gnd_author_names');
            var options = datalist.querySelectorAll('option');
            _.each(options, function(option) {
                datalist.removeChild(option);
            });
            
            var current_objects = data.results.bindings;
            
            _.each(current_objects, function(obj){
                var option = document.createElement('option');
                option.value = obj.concept.value;
                option.text = obj.prefLabel.value;
                datalist.appendChild(option);
            });
            ws_objects.push(current_objects);
            
        },
        
    });
    
    return
}


$(function add_authors() {
  
  var authorContainer = $('#authors');
   
  $('#add_author').on('click', function() {
    
    $('.hidden_authorfield')
        .clone(true, true)
        .prop('class', 'author')
        .removeProp('disabled')
        .appendTo(authorContainer)
    $(master_slave_input());
    econws();
    return false;
  });

  //remove author fieldset
  $(authorContainer).on('click', '.remove_author', function() { 
      $(this).parents('fieldset.author').remove();
    return false;
  });
    
});

