
    function generateData(count, yrange) {
        var i = 0;
        var series = [];
        while (i < count) {
            var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

            series.push(y);
            i++;
        }
        return series;
    }

    var data = [{
            name: 'Enero',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Febrero',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Marzo',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Abril',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Mayo',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Junio',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Julio',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        },
        {
            name: 'Agosto',
            data: generateData(15, {
                min: 0,
                max: 90
            })
        }
    ]

    data.reverse()


    var options = {
        chart: {
            height: 350,
            type: 'heatmap'
        },
        dataLabels: {
            enabled: false
        },
        plotOptions: {
            heatmap: {
                colorScale: {
                    inverse: true
                }
            }
        },
        colors: ["#F3B415", "#F27036", "#663F59", "#6A6E94", "#4E88B4", "#00A7C6", "#18D8D8", '#A9D794',
            '#46AF78', '#A93F55', '#8C5E58', '#2176FF', '#33A1FD', '#7A918D', '#BAFF29'
        ],
        series: data,
        xaxis: {
            type: 'category',
            categories: ['Aguacate', 'Alamillo', 'Alamo', 'Bricho', 'Canario', 'Caiba', 'Ciruelo', 'Cítrico', 'Durazno', 'Encino', 'Fresno', 'Guayabo', 'Jacaranda', 'Manzano', 'Orquideana','Olivo', 'Pera', 'Pino', 'Tulipan',
                 'Yuca'
            ]
        },

        title: {
            text: 'Color Scales flipped Vertically'
        },

    }

    var chart = new ApexCharts(
        document.querySelector("#chart"),
        options
    );

    chart.render();
