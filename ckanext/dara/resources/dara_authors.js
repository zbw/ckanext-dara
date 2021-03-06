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
// -    check for purity
//
// -    better implement as ckan.module?
//      http://docs.ckan.org/en/latest/theming/javascript.html



(function () {
// store/cache all results from econws
var ws_objects = [];
var dl_names = document.getElementById('gnd_author_names');
var dl_affil = document.getElementById('gnd_author_affiliations');
ws_names_init();
ws_affil_init();


function ws_names_init () {
    var inputs = document.querySelectorAll( '.econws_input' );

    _.each(inputs, function (inp) {
        inp.oninput = function() {
            var val = inp.value;
            if(_.isUndefined(val)) return;
            if(val.length < 2) return;
            if(val.indexOf(' [gnd:]') != -1) {
                var val_split = val.split(' [gnd:]');
                var ws_id = val_split[val_split.length -1];
                update_fields(inp, ws_id);
                return
            }
            ws_names_call(val);
        }
    });
}


function ws_affil_init () {
    var inputs = document.querySelectorAll( '.econws_affil' );
    _.each(inputs, function (inp) {
        inp.oninput = function() {
            var val = inp.value;
            if(_.isUndefined(val)) return;
            if(val.length < 2) return;
            ws_affil_call(val);
        }
    });
}


function ws_names_call(val) {
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
            var current_objects = data.results.bindings;
            _.each(current_objects, function(obj){
                var option = document.createElement('option');
                var text = obj.prefLabel.value;
                option.text = text.substring(0,150);
                option.value = text + ' [gnd:]' + obj.concept.value;
                if(! is_in_datalist(dl_names, option.value)) {
                    dl_names.appendChild(option);
                };
            });

            ws_objects.push(current_objects);
        },
    });

    return
}


function ws_affil_call(val) {
    $.ajax({
        url: "http://zbw.eu/beta/econ-ws/suggest2",
        dataType: "json",
        async: true,
        data: {
            query: val,
            dataset: 'econ_corp',
            limit: 15
        },
        success: function ( data ){
            var current_objects = data.results.bindings;
            _.each(current_objects, function(obj){
                var option = document.createElement('option');
                option.value = option.text = obj.prefLabel.value;
                if(! is_in_datalist(dl_affil, option.value)) {
                    dl_affil.appendChild(option);
                };
            });
        },

    });

    return
}


function update_fields (inp, val) {
    // TODO remove jquery

    var authorfields = $(inp).closest('fieldset.author');  // XXX

    var firstname = $(authorfields).find('[data-author="firstname"]');
    var aid = $(authorfields).find('[data-author="authorID"]');
    var aid_type = $(authorfields).find('[data-author="authorID_Type"]');
    var author = _.find(_.flatten(ws_objects, true), function (ob) {
        return ob.concept.value === val;
    });
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
        $(master_slave_input());  // XXX bad!  dara.js
        ws_names_init();  // TODO: add eventlistener with function
        ws_affil_init();
        return false;
    });

    //remove author fieldset
    $(authorContainer).on('click', '.remove_author', function() {
        $(this).parents('fieldset.author').remove();
        return false;
    });

});


function is_in_datalist(datalist, option_value) {
    var datalist_options = datalist.querySelectorAll('option');
    var v = _.any(datalist_options, function(dlopt){ 
        return dlopt.value === option_value });
    return v
}



}) ();
