$(document).ready(function () {
// Side nav for mobile view
  $(".button-collapse").sideNav();

// Clickable recipes dropdown menu for mobile side-nav
  $('.dropdown-trigger').dropdown();

// Hoverable recipes dropdown menu for desktop
  $('.dropdown-button').dropdown({
  inDuration: 400,
  outDuration: 225, 
  hover: true,
  });

// Image animation that scrolls through different images
  $('.carousel').carousel();
  setInterval(function () {
    $('.carousel').carousel('next');
  }, 3000);

// Clickable images to make full screen with message
  $('.materialboxed').materialbox();

// Tooltip messages for Success Stories
  $('.tooltipped').tooltip({delay: 50});

// Modal to appear when success story images are clicked
  $('.modal').modal();

// Copyright date updated every year
  $("#copyright").text(new Date().getFullYear());
});