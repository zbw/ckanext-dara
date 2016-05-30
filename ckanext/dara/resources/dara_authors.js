"use strict";


// TODO:
// -    inp.oninput etc. als eigene Funktion, um sie in add_authors() separat
//      als eventListener aufrufen zu können. So wie es jetzt ist, werden dann
//      alle input Elemente noch mal gebunden
//
// -    jQuery in update_fields() loswerden. Es gibt inzwischen ein JS-natives
//      .closest(), aber das ist noch zu neu
//
// -    rewrite inp.oninput as addEventLister function
//
// -    instead of clear_datalist() check for duplicates in datalist and only
//      append (in ws_call()) when value is not already existent OR find some
//      kind of unique() method for datalist
//
// -    check for purity
//
// -    better implement as ckan.module?
//      http://docs.ckan.org/en/latest/theming/javascript.html



(function () {
// store/cache all results from econws
var ws_objects = [];
var datalist = document.getElementById('gnd_author_names');
ws_init();

function ws_init () {
    //clear_datalist();
    var inputs = document.querySelectorAll( '.econws_input' );
    _.each(inputs, function (inp) {
        inp.oninput = function() {

            var val = inp.value;
            if(val.length < 2) return;
            //var split_val = val.split(' [gnd:]');
            //var sv = split_val[split_val.length-1];

            if(val.indexOf(' [gnd:]') != -1) {
                var val_split = val.split(' [gnd:]');
                var ws_id = val_split[val_split.length -1];
                update_fields(inp, ws_id);
                return
            }

            wscall(val);
        }
    });
}


function update_fields (inp, val) {
    // TODO remove jquery

    var authorfields = $(inp).closest('fieldset.author');  // XXX

    var firstname = $(authorfields).find('[data-author="firstname"]');
    var aid = $(authorfields).find('[data-author="authorID"]');
    var aid_type = $(authorfields).find('[data-author="authorID_Type"]');
    var aid_type_uri = $(authorfields).find('[data-author="authorID_URI"]');
    var author = _.find(_.flatten(ws_objects, true), function (ob) {
        return ob.concept.value === val;
    });
    var url = $(authorfields).find('[data-author="url"]');
    var authorname = author.prefName.value.split(", ");

    inp.value=authorname[0];
    var slave = $(authorfields).find('.dara_slave');
    $(aid_type)
        //.removeProp('disabled')
        .prop('required', true)
        .val('GND');
    $(slave).show();

    $(firstname).val(authorname[1]);
    $(aid).val(author.concept.value.replace('http://d-nb.info/gnd/', ''));
    $(url).val(author.concept.value, '');
    //$(aid_type_uri).val(author.concept.value);
    $(aid_type_uri).val('http://d-nb.info/gnd');

    return
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
            clear_datalist();
            var current_objects = data.results.bindings;

            _.each(current_objects, function(obj){
                var option = document.createElement('option');
               // option.value = obj.concept.value; // XXX remove
               // option.text = obj.prefLabel.value; // XXX append obj.concept.value
                var text = obj.prefLabel.value;
                option.text = text.substring(0,150);
                option.value = text + ' [gnd:]' + obj.concept.value;
                datalist.appendChild(option);
            });

            /* this does not work, since datalist is no hmtl.collection anymore
             * afterwards
            XXX find a way to uniq datalist
            datalist = _.unique(datalist.children, function(option) {
                // use gnd id for comparison
                var val_split = option.value.split(' [gnd:]');
                var ws_id = val_split[val_split.length -1];
                return ws_id;
            });
            */

            ws_objects.push(current_objects);

        },

    });

    return
}


// might be obsolete?
function clear_datalist () {
    var options = datalist.querySelectorAll('option');

    _.each(options, function(option) {
        datalist.removeChild(option);
    });
}


$(function add_authors() {

    var authorContainer = $('#authors');

    $('#add_author').on('click', function() {

        $('.hidden_authorfield')
            .clone(true, true)
            .prop('class', 'author')
            .removeProp('disabled')
            .appendTo(authorContainer)
        $(master_slave_input());  // XXX bad!  dara.js
        ws_init();  // TODO: add eventlistener with function
        return false;
    });

    //remove author fieldset
    $(authorContainer).on('click', '.remove_author', function() {
        $(this).parents('fieldset.author').remove();
        return false;
    });

});




}) ();
