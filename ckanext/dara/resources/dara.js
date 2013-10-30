/* 
Hendrik Bunke
ZBW - Leibniz Information Centre for Economics
2013-09-01

adds some usability to dara metadata forms

*/


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
      active : 2 // 2 is not a valid option so all levels are inactive
    });

});


$(function add_authors() {
  
  var addAuthorDiv = $('#additional_authors');
  var current_authors = $('#current_number_of_authors').text();
  var i = parseInt(current_authors) + 2   
  
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

