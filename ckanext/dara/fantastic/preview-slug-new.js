// New module for creating slugs
// Truncates titles > 99 characters to be 90
// by cutting out the middine of the title.
// The code originaed in `plugins/jquery.slug-preview.js`
// and `modules/sllug-preview.js`
"use-strict";


this.ckan.module('preview-slug-new', function ($) {
  return {
    options: {
      prefix: '',
      placeholder: '<slug>',
      i18n: {
        url:  _('URL'),
        edit: _('Edit')
      }
    },

    initialize: function () {
      var sandbox = this.sandbox;
      var options = this.options;
      var el = this.el;
      console.log(el);
      console.dir(el);
      var _ = sandbox.translate;

      var slug = el.slug();
      var parent = slug.parents('.control-group');
      var preview;

      if (!(parent.length)) {
        return;
      }

      // Leave the slug field visible
      if (!parent.hasClass('error')) {
        preview = slugPreview({
          prefix: options.prefix,
          placeholder: options.placeholder,
          i18n: {
            'URL': this.i18n('url'),
            'Edit': this.i18n('edit')
          }
        }, parent);

        // If the user manually enters text into the input we cancel the slug
        // listeners so that we don't clobber the slug when the title next changes.
        slug.keypress(function () {
          if (event.charCode) {
            sandbox.publish('slug-preview-modified', preview[0]);
          }
        });

        sandbox.publish('slug-preview-created', preview[0]);

        // Horrible hack to make sure that IE7 rerenders the subsequent
        // DOM children correctly now that we've render the slug preview element
        // We should drop this horrible hack ASAP
        if (jQuery('html').hasClass('ie7')) {
          jQuery('.btn').on('click', preview, function(){
            jQuery('.controls').ie7redraw();
          });
          preview.hide();
          setTimeout(function() {
            preview.show();
            jQuery('.controls').ie7redraw();
          }, 10);
        }
      }

      // Watch for updates to the target field and update the hidden slug field
      // triggering the "change" event manually.
      sandbox.subscribe('slug-target-changed', function (value) {
        slug.val(value).trigger('change');
      });
    }
  };
});

var escape = $.url.escape;
function slugPreview(options, parent) {
  options = $.extend(true, slugPreview.defaults, options || {});

  var collected = parent.map(function () {
    var element = $(parent);
    var field = element.find('input');
    var preview = $(options.template);
    var value = preview.find('.slug-preview-value');
    var required = $('<div>').append($('.control-required', element).clone()).html();

    function setValue() {
      var val = escape(field.val()) || options.placeholder;
      if (val.length > 99){
        val = val.slice(0,45) + val.slice(-45);
      }
      value.text(val);
    }

    preview.find('strong').html(required + ' ' + options.i18n['URL'] + ':');
    preview.find('.slug-preview-prefix').text(options.prefix);
    preview.find('button').text(options.i18n['Edit']).click(function (event) {
      event.preventDefault();
      element.show();
      preview.hide();
    });

    setValue();
    field.on('change', setValue);

    element.after(preview).hide();

    return preview[0];
  });

  // Append the new elements to the current jQuery stack so that the caller
  // can modify the elements. Then restore the originals by calling .end().
  return parent.pushStack(collected);
}

slugPreview.defaults = {
  prefix: '',
  placeholder: '',
  i18n: {
    'URL': 'URL',
    'Edit': 'Edit'
  },
  template: [
    '<div class="slug-preview">',
    '<strong></strong>',
    '<span class="slug-preview-prefix"></span><span class="slug-preview-value"></span>',
    '<button class="btn btn-mini"></button>',
    '</div>'
  ].join('\n')
};
