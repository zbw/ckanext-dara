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
      var master = $(this).find('.dara_master').find('input').first();
      var slave = $(this).find('.dara_slave');
      var value = master.prop('value');

      if(value === "") {
        slave.hide();
        }

      $(master).on("input change keyup paste", function () 
        {
          if(master.prop('value') !=="") {
            slave.fadeIn();
          }
          else {
           slave.fadeOut(); 
        }
      });
    });
}


function econws() {
   var objects = [];
   var inputs = document.getElementsByClassName( 'econws_input' );
   
   _.each(inputs, function(inp) {
        $(inp).on("input keypress paste mouseenter focus", function(e) {
            var val = $(this).val();
            if(val === "") return;
            var par = inp.parentElement;
            
            var update_fields = function (val) {
                var authorfields = $(par.parentElement.parentElement); // XXX optimize
                var firstname = $(authorfields).find('[data-author="firstname"]');
                var aid = $(authorfields).find('[data-author="authorID"]');
                var aid_type = $(authorfields).find('[data-author="authorID_Type"]');
                var author = _.find(_.flatten(objects, true), function (ob) { 
                    return ob.concept.value === val; 
                });
                var authorname = author.prefName.value.split(", ");
                $(inp).val(authorname[0]);
                $(firstname).val(authorname[1]);
                $(aid).val(author.concept.value.replace('http://d-nb.info/gnd/', ''));
                $(aid_type).val('GND');
                
                // not really necessary to fadeIn here
                //$(authorfields).find('.dara_slave').fadeIn();
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
                        $('datalist').remove();
                        var current_objects = data.results.bindings;
                        var datal = document.createElement('datalist');
                        par.appendChild(datal);
                        var datalist = par.getElementsByTagName('datalist')[0];
                        datalist.setAttribute('id', 'names');

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

    

/* obsolete for now
 *
$(function metadata_level() {

    $( "#dara_1" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      active : 0 
    });

    $( "#dara_2" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      active : 2 // 2 is not a valid option so all levels are inactive
    });

    $( "#dara_3" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      heightStyle: "content",
      active : 2 // 2 is not a valid option so all levels are inactive
    });

});
*/

//XXX obsolete for now
//$(function publication() {
//  var publication = $('#dara_Publication');
//  var pubs = $('#pubs').text();
//  var active = parseInt(pubs);

//  $(publication).accordion({
//    collapsible: true,
//    heightStyle: "content",
//    icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
//    active : active
//  });
//});


//XXX obsolete for now
//$(function resource() {
//  var resource = $('#dara_Resource');

//  $(resource).accordion({
//    collapsible: true,
//    heightStyle: "content",
//    icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
//    active : 2
//  });
//
//});











