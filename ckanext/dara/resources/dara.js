$(function() {
 /*   var icons = {
      header: "ui-icon-circle-arrow-e",
      activeHeader: "ui-icon-circle-arrow-s"
    };
    */
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
});
