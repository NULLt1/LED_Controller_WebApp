$(function() {
$("#power").on( "click", power );

      function power() {
        location.href = '/power/'
       }

var value= $("powerValue").val;
alert(value);
});