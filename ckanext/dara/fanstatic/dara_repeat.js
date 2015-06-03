/* Module for working with multiple field inputs. This will create
 * a new field when the user clicks the 'add field' button.
 *
 * https://github.com/okfn/ckanext-lcrnz/blob/master/ckanext/lcrnz/fanstatic/lcrnz-repeating.js
 *
 */
this.ckan.module('ckanext-dara', function (jQuery, _) {
  return {
    options: {
      /* The selector used for each custom field wrapper */
      fieldSelector: '.repeat'
    },

    /* Initializes the module and attaches custom event listeners. This
     * is called internally by ckan.module.initialize().
     *
     * Returns nothing.
     */
    initialize: function () {
      console.log("I've been initialized for element: %o", this.el);
      
      if (!jQuery('html').hasClass('ie7')) {
        jQuery.proxyAll(this, /_on/);

        // Create 'plus field' checkbox and add to first input container.
        var firstFieldContainer = this.el.find(this.options.fieldSelector + ':first .controls');
        console.log(firstFieldContainer);
        var checkbox = $('<label class="checkbox btn btn-success icon-plus" for="add-field"><input type="checkbox" id="add-field" /></label>');
        checkbox.on('change', ':checkbox', this._onChange);
        $(firstFieldContainer).append(checkbox);
      }
    },

    /* Create a new field and appends it to the list. This currently works by
     * cloning and erasing an existing input rather than using a template.
     * In future using a template might be more appropriate.
     *
     * element - Another custom field element to wrap.
     *
     * Returns nothing.
     */
    newField: function (element) {
      newEl = this.cloneField(element);
      this.el.append(newEl);
    },

    /* Clone the provided element, wipe its content and increment its
     * `for`, `id` and `name` fields (if possible).
     *
     * current - A custom field to clone.
     *
     * Returns a newly created custom field element.
     */
    cloneField: function (current) {
      return this.resetField(jQuery(current).clone());
    },

    /* Wipe the contents of the field provided and increment its `name`, `id`
     * and `for` attributes. Also remove 'add' checkbox if necessary.
     *
     * field - A custom field to wipe.
     *
     * Returns the wiped element.
     */
    resetField: function (field) {
      function increment(index, string) {
        return (string || '').replace(/\d+/, function (int) { return 1 + parseInt(int, 10); });
      }

      var input = field.find(':input');
      input.val('').attr('id', increment).attr('name', increment);

      var label = field.find('label');
      label.text(increment).attr('for', increment);

      field.find('.checkbox').remove();

      return field;
    },

    /* Event handler called when the add checkbox is changed */
    _onChange: function (event) {
      var lastFieldContainer = this.el.find(this.options.fieldSelector + ':last');
      this.newField(lastFieldContainer);
    }
  };
});

