$(function() {
 /*   var icons = {
      header: "ui-icon-circle-arrow-e",
      activeHeader: "ui-icon-circle-arrow-s"
    };
    */

    var addAuthorDiv = $('#additional_authors');
    //var i = $('#additional_authors div.dara_author').size() + 1;
    //var i = 2
    var current_authors = $('#current_number_of_authors').text();
    var i = parseInt(current_authors) + 2

    
    // dara metadata forms
    $( "#dara_1" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      active : 0 
    });
    $( "#dara_2" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      active : 2 //2 gibts nicht, weswegen alle deactive sind
    });
    $( "#dara_3" ).accordion({
      collapsible: true,
      icons: { "header": "ui-icon-plus", "activeHeader": "ui-icon-minus" },
      active : 2 //2 gibts nicht, weswegen alle deactive sind
    });

       
    //add author field
    $('#add_author').live('click', function() {

      $('<div class="control-group dara_author">\
          <label class="control-label" for="field-dara_author_' + i +'">\
          Author '+ i +'</label>\
          <div class="controls ">\
            <input id="field-dara_author_'+ i +'" type="text" name="dara_author_' + i +'" \
              value="" placeholder="Author Name" /> \
              <a href="#" class="dara_red" id="remove_author">Remove</a>\
          </div></div>').appendTo(addAuthorDiv);
      i++;
      return false;
    });
 

    //remove author field
    $('#remove_author').live('click', function() { 
        if( i > 1 ) {
            $(this).parents('div.dara_author').remove();
            i--;
        }
        return false;
     });


});


$(function master_slave_input() {

  // conditional field based on input 
    $('.dara_master_slave').each(function () 
      {
      var master = $(this).find('.dara_master').find('input').first();
      var slave = $(this).find('.dara_slave');
      var value = master.attr('value');

      if(value == "") {
        slave.hide();
        }

      master.bind("change keyup paste", function () 
    // we cannot use the 'value' var here since it wont change after defining it
        {
          if(master.attr('value') !="") {
            slave.fadeIn();
          }
          else {
           slave.fadeOut(); 
        }
      });
    });

});

