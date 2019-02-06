// New module for creating slugs
// Truncates titles > 99 characters to be 90
// by cutting out the middine of the title
"use-strict";


this.ckan.module('preview-slug-new', function ($) {
  return {
    initialize: function(){
        console.log('New slug preview - fantastic', this.el);
    }
  };
});
