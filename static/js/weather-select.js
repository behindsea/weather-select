$(document).ready(function(){
$("#select").click(function() {
  city = $("#city").val();
  if (city != "") {
    $.post("/select",{city:city}, function(result) {
      $("#Weatherdata").html(result);
    });
    // $("#Weatherdata").html(result);
  } else {
    alert("城市名不能为空！");
  };
});

$("#history").click(function() {
  $.post("history", {}, function(result) {
    $("#Weatherdata").html(result);
  });

});

$("#help").click(function() {
  $.post("/help", {}, function(result) {
    $("#Weatherdata").html(result);
  });
});

$("#change").click(function() {
  city = $("#city").val();
  if (city != "") {
    $.post("change", {
      city: city
    }, function(result) {
      $("#Weatherdata").html(result);
    });
  } else {
    alert("输入数据不能为空！");
  };
});
});
