//Hendrik Bunke
//ZBW - Leibniz Information Centre for Economics
//
//adding some usability and field functions to dara metadata forms

"use strict";

//calling functions for the first time, if we dont want those functions bind
//to $()
//$(master_slave_input());
//$(res_preselection());


$(function master_slave_input() {

  // conditional field based on input 
    $('.dara_master_slave').each(function () {
      var master = $(this).find('.dara_master').find('input').first();
      var slave = $(this).find('.dara_slave');
      var value = master.prop('value');

      if(value === "") {
        slave.hide();
        }

      master.bind("change keyup paste", function () 
        {
          if(master.prop('value') !=="") {
            slave.fadeIn();
          }
          else {
           slave.fadeOut(); 
        }
      });
    });

});


// need to bind this to jquery $ because for some reason otherwise underscore's
// _ won't be in scope
$(function res_preselection() {
// conditional fields based on input 

    var master = $('#dara_res_preselection');
    var value = master.val();
    var blocks = [
        [$('#dara_data'), 'data'],
        [$('#dara_text'), 'text'],
        [$('#dara_code'), 'code'],
        [$('#dara_other'), 'other']
    ];


   //XXX using underscore.js
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
            {   //recursion, fuck yeah ;-)
                $(res_preselection()); }
            );
});


$(function add_authors() {
  
  var authorContainer = $('#authors');
   
  $('#add_author').on('click', function() {
    
    $('.hidden_authorfield').clone().prop('class', 'author').appendTo(authorContainer);
    $(master_slave_input());
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

















