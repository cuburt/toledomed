 /*
  **********************************************************
  * OPAQUE NAVBAR SCRIPT
  **********************************************************
  */

  // Toggle tranparent navbar when the user scrolls the page

  $(window).scroll(function() {
    if($(this).scrollTop() > 50)  /*height in pixels when the navbar becomes non opaque*/
    {
        $('.navbar').removeClass('navbar-inverse');
        $('.navbar').addClass('navbar-default');

    } else {
        $('.navbar').addClass('navbar-inverse');
        $('.navbar').removeClass('navbar-default');
    }
});

