$(function() {
$("#power").on( "click", power );

      function power() {
        location.href = '/power/'
       }

var value= $("powerValue").attr("value");
alert(value);
});