$('.open-modal').click(function(){
  $('.block-popup, .overlay').fadeIn();
})
$('.block-popup span').click(function(){
  $('.block-popup, .overlay').fadeOut();
})