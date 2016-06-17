$(document).ready(function(){
   // setInterval(updateClock(), 1000);
   setInterval(function () { $('#clock').text(Date()) }, 1000)
});
