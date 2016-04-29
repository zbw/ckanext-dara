//Hendrik Bunke
//ZBW - Leibniz Information Centre for Economics
//
//adding some usability and field functions to dara metadata forms

"use strict";


$(master_slave_input()); // XXX refactor!



function master_slave_input() {

  // conditional field based on input 
    $('.dara_master_slave').each(function () {
      var master = $(this).find('.dara_master').find(':input').first();
      var slave = $(this).find('.dara_slave');
      var value = master.prop('value');
      var slave_input = $(slave).find(':input').first();
      if(value === "") {
        slave.hide();
        slave_input.prop('required', false);
        slave_input.val('');
      }

      $(master).on("input change keyup paste", function () 
        {
          if(master.prop('value') !=="") {
            slave.fadeIn();
            //slave_input.prop('disabled', false);
            slave_input.prop('required', true);
            }
          else {
           slave.fadeOut(); 
           //slave_input.prop('disabled', true);
           slave_input.prop('required', false);
           slave_input.val('');

        }
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
