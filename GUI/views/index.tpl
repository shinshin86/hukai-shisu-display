<link href="{{url('static_file', filepath='style.css') }}"rel="stylesheet" type="text/css" />
<script type="text/javascript" src="{{url('static_file', filepath='Chart.min.js') }}" charset="utf-8"></script>
<script language="JavaScript">
function displayLineChart() {
var data = {
labels: [1, 2, 3, 4, 5, 6, 7],
datasets: [
{
label: "Temperature",
fillColor: "rgba(220,220,220,0.2)",
strokeColor: "rgba(220,220,220,1)",
pointColor: "rgba(220,220,220,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(220,220,220,1)",
data: [20, 25, 25, 27, 21, 13, {{html_today_temperature}}]
},
{
label: "Today Humidity",
fillColor: "rgba(151,187,205,0.2)",
strokeColor: "rgba(151,187,205,1)",
pointColor: "rgba(151,187,205,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(151,187,205,1)",
data: [70, 61, 61, 62, 63, 65, {{html_today_humidity}}]
},
{
label: "Hukai Shisu",
fillColor: "rgba(221,127,235,0.2)",
strokeColor: "rgba(221,127,205,1)",
pointColor: "rgba(151,137,205,1)",
pointStrokeColor: "#fff",
pointHighlightFill: "#fff",
pointHighlightStroke: "rgba(151,187,205,1)",
data: [50, 53, 54, 62, 54, 65, {{html_today_hukai_shisu_result}}]
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
<canvas id="lineChart" height="450" width="900"></canvas>
</div>

<h1>温度 : {{html_today_temperature}}</h1>
<h1>湿度 : {{html_today_humidity}}</h1>
<h1>本日の不快指数 : {{html_today_hukai_shisu_result}}</h1>
</body>