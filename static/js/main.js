$(function() {
$("#power").on( "click", power );

function power() {
    location.href = '/power/'
}

$("button[name ='color-button']").each(function( index ) {
  let red = $(this).attr('red');
  let green = $(this).attr('green');
  let blue = $(this).attr('blue');
  $(this).css("background-color", "rgb("+red+","+green+","+blue+")");
  $(this).click(function() {
    changeColorRequest(red,green,blue);
  });
});







function changeColorRequest(red,green,blue) {
    console.log(red+green+blue);
    $.post( "/color/", { red: red, green: green, blue: blue } );
}

});
