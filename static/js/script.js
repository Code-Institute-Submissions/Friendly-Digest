// Hoverable recipes dropdown menu for desktop
$('.dropdown-button').dropdown({
  inDuration: 400,
  outDuration: 225, 
  hover: true,
  }
);

// Side nav for mobile view
$(".button-collapse").sideNav();

// Clickable recipes dropdown menu for mobile side-nav
$(document).ready(function(){
  $('.dropdown-trigger').dropdown();
});

// Copyright date updated every year
$("#copyright").text(new Date().getFullYear());