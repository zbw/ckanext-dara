//Hendrik Bunke
//ZBW - Leibniz Information Centre for Economics
//
//adding some usability and field functions to dara metadata forms

"use strict";


//calling functions for the first time, if we dont want those functions bind
//to $()
$(master_slave_input());
econws();

//$(econws());
//$(res_preselection());




function master_slave_input() {

  // conditional field based on input 
    $('.dara_master_slave').each(function () {
      var master = $(this).find('.dara_master').find(':input').first();
      var slave = $(this).find('.dara_slave');
      var value = master.prop('value');
      var slave_input = $(slave).find(':input').first();
      if(value === "") {
        slave.hide();
        slave_input.prop('disabled', true);
        slave_input.prop('required', false);
      }

      $(master).on("input change keyup paste", function () 
        {
          if(master.prop('value') !=="") {
            slave.fadeIn();
            slave_input.prop('disabled', false);
            slave_input.prop('required', true);
            }
          else {
           slave.fadeOut(); 
           slave_input.prop('disabled', true);
           slave_input.prop('required', false);

        }
      });
    });
}


function econws() {
   
   var objects = []; // XXX better keep all objects vom econws?
   var inputs = document.querySelectorAll( '.econws_input' );
   
   _.each(inputs, function(inp) {
        $(inp).on("input", function() {
            var val = $(inp).val();
            if(val.length < 2) return;
            var par = inp.parentElement;

            var update_fields = function (val) {
                var authorfields = $(inp).closest('.author'); // XXX optimize

                var firstname = $(authorfields).find('[data-author="firstname"]');
                var aid = $(authorfields).find('[data-author="authorID"]');
                var aid_type = $(authorfields).find('[data-author="authorID_Type"]');
                var author = _.find(_.flatten(objects, true), function (ob) { 
                    return ob.concept.value === val; 
                });
                var url = $(authorfields).find('[data-author="url"]');
                var authorname = author.prefName.value.split(", ");
                $(inp).val(authorname[0]);
                $(firstname).val(authorname[1]);
                $(aid).val(author.concept.value.replace('http://d-nb.info/gnd/', ''));
                $(aid_type).val('GND');
                $(url).val(author.concept.value);
                
                // fadeIn() necessary here?
                // $(authorfields).find('.dara_slave').fadeIn();
                $(aid_type).prop('disabled', false);
                $(aid_type).prop('required', true);

            };
            
            var wscall = function () {
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
                        objects.push(current_objects);
                        
                    },
                });
            };
            
            if(val.indexOf('http://d-nb.info/gnd/') != -1) {
                update_fields(val);
            }
            
            wscall();

        });

    });
}



//TODO might be optimized as standalone function?
$(function res_preselection() {
// fields based on preselection

    var master = $('#dara_res_preselection');
    var value = master.val();
    var blocks = [
        [$('#dara_data'), 'data'],
        [$('#dara_text'), 'text'],
        [$('#dara_code'), 'code'],
        [$('#dara_other'), 'other']
    ];


   //XXX using Underscore.js
    _.each(blocks, function(b) {
        var block = b[0];
        var text = b[1];
        block.hide();
        block.prop("disabled", true);
        if(value === text) {
            block.show();
            block.prop("disabled", false);
        }
    });


    master.on('change keyup', function ()
            {   //recursion, f*** yeah ;-)
                $(res_preselection()); }
            );
});


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


$(function fill_resource_name() {
    $('#field-image-upload').on('change click keypress', function() {
        var url = $('#field-image-url').val();
        $('#field-name').val(url);
        $('#field-name').focus();
        
        // needs to
        // be called four times (or so) to actually get the correct url value
        $(fill_resource_name()); 
    });
});



function dara_info(el, action, container) {
    var inp = $(container).find('[data-infotext]');
    $( el ).tooltip({
        items: ".ib",
        //content: function() {
        //    return $( this ).attr('data-infotext')
        //},
        content: function () {
            return $(inp).attr('data-infotext');
        },
        show: {delay: 0},
        position: {
            my: "center bottom-10",
            at: "center top",
            using: function( position, feedback ) {
                $( this ).css( position );
                $( "<div>" )
                   // .addClass( "arrow" )
                    .addClass( feedback.vertical )
                    .addClass( feedback.horizontal )
                    .appendTo( this );
            }
        }
    });

    $( el ).tooltip(action);
};


$(function infobutton () {

    var controls = $('.controls');
    controls.after('<div class="ib"><i class="icon-info-sign" /></div>');

    $('.ib').on('click', function() {
        dara_info($(this), 'open', $(this).prev());
    });
    $('.ib').on('mouseout', function () {
        dara_info($(this), 'destroy', $(this).prev());
    });
            
});
