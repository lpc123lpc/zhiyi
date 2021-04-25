<template>
    <div id="countryDataCharts" style="width: 600px;height:400px;"></div>
    <script src = '../../node_modules/echarts/dist/echarts.js'></script>
</template>

<script>

  export default {
    name: 'countryData'
  }
  const myChart = echarts.init(document.getElementById('main'))

  fetch('../static/json/charts/testData').then(function (response) {
    response.json().then(function (data) {
        myChart.setOption({
        title:{
            text:'国家总体数据'
        },
        tooltip:{},
        legend:{
            data:['接种人数','确诊人数','治愈人数','死亡人数']
        },
        xAxis:[{
            name:'日期',
            type:'category',
            data:data.time
        }],
        yAxis:[{
           type: 'value'
        }],
        series:[{
            name:'接种人数',
            type:'line',
            data:data.vaccined
            },
            {
                name:'确诊人数',
                type:'line',
                data: data.confirmed
            },
            {
                name:'治愈人数',
                type:'line',
                data:data.cured
            },
            {
                name:'死亡人数',
                type:'line',
                data:data.deceased
            }]
    })
    })
}).catch(function(err){
    alert(err.toString())
})
</script>

<style scoped>

</style>
