<link href="{{url('static_file', filepath='style.css') }}"rel="stylesheet" type="text/css" />
<script type="text/javascript" src="{{url('static_file', filepath='Chart.min.js') }}" charset="utf-8"></script>
<script language="JavaScript">
function displayLineChart() {
var data = {
labels: [1, 2, 3, 4, 5, 6, 7],
datasets: [
{
label: "Temperature",
fillColor: "rgba(80,180,230,0.2)",
strokeColor: "rgba(80,180,230,1)",
pointColor: "rgba(80,180,230,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(220,220,220,1)",
           data: [{{ago_tempe_0}},{{ago_tempe_1}},{{ago_tempe_2}}, {{ago_tempe_3}}, {{ago_tempe_4}}, {{ago_tempe_5}}, {{html_today_temperature}}]
},
{
label: "Today Humidity",
fillColor: "rgba(251,167,205,0.2)",
strokeColor: "rgba(251,167,205,0.5)",
pointColor: "rgba(151,107,205,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(151,187,205,1)",
data: [{{ago_humid_0}},{{ago_humid_1}},{{ago_humid_2}}, {{ago_humid_3}}, {{ago_humid_4}}, {{ago_humid_5}},  {{html_today_humidity}}]
},
{
label: "Hukai Shisu",
fillColor: "rgba(151,197,215,0.2)",
strokeColor: "rgba(151,197,215,0.8)",
pointColor: "rgba(151,197,215,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(151,187,205,1)",
data: [{{ago_hukai_0}},{{ago_hukai_1}},{{ago_hukai_2}}, {{ago_hukai_3}}, {{ago_hukai_4}}, {{ago_hukai_5}}, {{html_today_hukai_shisu_result}}]
}
]
};
var ctx = document.getElementById("lineChart").getContext("2d");
var options = { };
var lineChart = new Chart(ctx).Line(data, options);
}
</script>
<body onload="displayLineChart();">
<div class="box">
<canvas id="lineChart" height="400" width="900"></canvas>
</div>

<div class="today">本日の温度 : {{html_today_temperature}}</div>
<div class="today">本日の湿度 : {{html_today_humidity}}</div>
<div class="today">本日の不快指数 : {{html_today_hukai_shisu_result}}</div>
</body>