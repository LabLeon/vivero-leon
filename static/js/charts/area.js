
var options = {
  chart: {
    height: 350,
    type: 'area',
    stacked: true,
    events: {
      selection: function(chart, e) {
        console.log(new Date(e.xaxis.min) )
      }
    },

  },
  colors: ['#4caf50'],
  dataLabels: {
      enabled: false
  },
  stroke: {
    curve: 'smooth'
  },

  series: [
    {
      name: 'Donaciones',
      data: generateDayWiseTimeSeries(new Date('Jan 2019 GMT').getTime(), 100, {
        min: 20,
        max: 45
      })
    }
  ],
  fill: {
    type: 'gradient',
    gradient: {
      opacityFrom: 0.6,
      opacityTo: 0.8,
    }
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left'
  },
  xaxis: {
    type: 'datetime'
  },
}

var chart = new ApexCharts(
  document.querySelector("#chart"),
  options
);

chart.render();

/*
  // this function will generate output in this format
  // data = [
      [timestamp, 23],
      [timestamp, 33],
      [timestamp, 12]
      ...
  ]
  */
function generateDayWiseTimeSeries(baseval, count, yrange) {
  var i = 0;
  var series = [];
  while (i < count) {
    var x = baseval;
    var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

    series.push([x, y]);
    baseval += 86400000;
    i++;
  }
  return series;
}
