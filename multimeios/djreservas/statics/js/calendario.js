$(document).ready(function(){
    $(".form-reserva").click(function(e){
        if(e.target.className.indexOf("form-reserva") >= 0){
            var data = $(this).data("day");
            location.href = "/forms?data_reserva="+data;
        }
    })
})