// Activate Next Step
var current_fs, next_fs, previous_fs;
var time, date, service_id, service_type_id; //
$(document).ready(function(event){



    $(".next").click(function(){


        current_fs = $(this).parents("fieldset");
	    next_fs = $(this).parents("fieldset").next();

	    $("#nav li").eq($("fieldset").index(next_fs)).addClass("active");
	    $("#nav li").eq($("fieldset").index(current_fs)).removeClass("active");

        current_fs.hide();
        next_fs.show();

    });

    $(".previous").click(function(){

        current_fs = $(this).parents("fieldset");
        previous_fs = $(this).parents("fieldset").prev();

        $("#nav li").eq($("fieldset").index(previous_fs)).addClass("active");
        $("#nav li").eq($("fieldset").index(current_fs)).removeClass("active");


        current_fs.hide();
        previous_fs.show();

    });
    $(".alert").hover(function(){
        $(this).toggleClass("alert-warning");
    });
    $("fieldset#step-1").find("div").find(".alert").click(function(){

        service_type_id = $(this).find("input").val();

        current_fs = $(this).parents("fieldset");
	    next_fs = $(this).parents("fieldset").next();

	    $("#nav li").eq($("fieldset").index(next_fs)).addClass("active");
	    $("#nav li").eq($("fieldset").index(current_fs)).removeClass("active");

        current_fs.hide();
        next_fs.show();

        if(service_type_id == 1)  /*height in pixels when the navbar becomes non opaque*/
    {
        next_fs.find("div").find("div.1").show();

    } else if(service_type_id == 2) {

        next_fs.find("div").find("div.2").show();
    } else {

        next_fs.find("div").find("div.30").show();
    }
        //next_fs.find("div").find("input").val(service_id);




    });
    $("fieldset#step-2").find("div").find(".alert").click(function(){


        service_id = $(this).find("input").val();

        current_fs = $(this).parents("fieldset");
	    next_fs = $(this).parents("fieldset").next();

	    $("#nav li").eq($("fieldset").index(next_fs)).addClass("active");
	    $("#nav li").eq($("fieldset").index(current_fs)).removeClass("active");

        current_fs.hide();
        next_fs.show();

        if(service_type_id == 1)  /*height in pixels when the navbar becomes non opaque*/
    {
        next_fs.find("div.1").show();

    } else if(service_type_id == 2) {

        next_fs.find("div.2").show();
    } else {

        next_fs.find("div.30").show();
    }
        //next_fs.find("div").find("input").val(service_id);




    });
    $("fieldset#step-3").find("div").find(".alert").click(function(){
        date = $(this).parents(".modal-body").find("input").val();
        time = $(this).find("input").val();


        current_fs = $(this).parents("fieldset");
	    next_fs = $(this).parents("fieldset").next();

	    $("#nav li").eq($("fieldset").index(next_fs)).addClass("active");
	    $("#nav li").eq($("fieldset").index(current_fs)).removeClass("active");

        current_fs.hide();
        next_fs.show();

        $("input").filter("#id_Requested_Date").val(date);
        $("input").filter("#id_Requested_Time").val(time);

    });






});


