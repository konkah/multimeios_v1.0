$(document).ready(function(){
    $("#data_reserva").datetimepicker({
        format: "DD/MM/YYYY", 
        locale: "pt-BR",
        //minDate: moment(), 
        //maxDate: moment().add(1, "M"),
        daysOfWeekDisabled: [0,6],
        useCurrent: false 
    })

    $("#hora_inicio").datetimepicker({
        format: "HH:mm", 
        locale: "pt-BR",
        stepping:"30",
    })

    $("#hora_fim").datetimepicker({
        format: "HH:mm", 
        locale: "pt-BR",
        stepping:"30",
    })

})