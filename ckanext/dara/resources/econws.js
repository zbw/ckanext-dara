//http://codepen.io/jplhomer/pen/pvkKs/

'use strict';
var MOVIE_SEARCH = {
  rtApiKey: '',
  rtApiEndpoint: '',
  delay: 0,
  timer: 0,
  input: {},
  list: {},
  init: function() {
    // Define elements
    this.input = $('[data-movie-search]');
    this.list = $('[data-movie-list]');
    
    // Set delay
    this.delay = 300; // 300 milliseconds
    
    // Set Rotten Tomatoes data
    this.rtApiKey = 'jpe83dcf7beyxqn6gxwm2cwa';
 //   this.rtApiEndpoint = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json';
    this.rtApiEndpoint = 'http://zbw.eu/beta/econ-ws/suggest2'


    // Add event listeners
    this.input.on('keyup', this.setTimer.bind(this));
  },
  
  setTimer: function() {
    if ( this.timer ) {
      clearTimeout(this.timer);
    }
    
    this.timer = setTimeout( this.processQuery.bind(this), this.delay );
  },
  
  processQuery: function() {
    var query = this.input.val();
    
    if ( ! query ) {
      return false;
    }
    
    $.ajax({
      dataType: 'jsonp',
      url: this.rtApiEndpoint,
      data: {
        apikey: this.rtApiKey,
        q: query
      },
      success: this.updateMovieList.bind(this)
    });
  },
  
  updateMovieList: function( response ) {
    if ( 'object' === typeof( response.results ) ) {
      var movies = response.results;
      
      // Clear the list
      this.list.html('');

      $.each( movies, function(idx, movie) {
        this.list.append('<option>' + movie.title + '</option>');
      }.bind(this));
    }
  }
};

$(document).ready(function() {
 console.log('Yes, its here'); 
 MOVIE_SEARCH.init();
  
});
