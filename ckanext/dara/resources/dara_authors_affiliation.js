"use strict";



(function () {
var datalist = document.getElementById('gnd_author_affiliations');
ws_affil_init();


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
                if(! is_in_datalist(option.value)) {
                    datalist.appendChild(option);
                };
            });
        },

    });

    return
}


function is_in_datalist(option_value) {
    var datalist_options = datalist.querySelectorAll('option');
    var v = _.any(datalist_options, function(dlopt){ 
        return dlopt.value === option_value });
    return v
}


}) ();
