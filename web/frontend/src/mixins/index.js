export const mixin = {
    methods: {
        getWorldNameMap() {
            var json = require('../../static/json/map/world/world-mapping.json')
            var nameMap = {}
            for (let i in json) {
                // console.log(i)
                nameMap[i] = json[i].cn
            }
            // console.log(nameMap)
            return nameMap
        },
        // return [fileName, englishName]
        getCountryName(country) {
          var json = require('../../static/json/map/world/world-mapping.json')
          var engName
          for (let i in json) {
              // console.log(i)
              if (json[i].cn === country) {
                  engName = i
                  if (i === 'China') engName = 'china'
                  return [json[i].mapFileName, engName]
              }
          }
        },
        getChinaProvinceFileName(province) {
            var json = require('../../static/json/map/china-province/china-province-mapping.json')
            return json[province]
        },
        getProvinceNameMap(province) {
            var json = require('../../static/json/map/china-province/city-map.json')
            return json[province]
        },
        judgeDataExist(data) {
            if (JSON.stringify(data) === '{}') {
                this.$confirm('对不起，暂未收录该地区数据', '提示', {
                    confirmButtonText: '返回',
                    showCancelButton: false,
                    // type: 'warning'
                }).then(() => {
                    this.$router.go(-1)
                })
                .catch(action => {
                    if (action === 'cancel') {
                        this.$router.go(-1)
                    }
                });
            }
        },
        getSelected(list) {
            var ret = {}
            for (let i in list) {
              ret[list[i]] = false
            }
            var val = Math.min(10, list.length)
            for (let i=0; i<val; i++) {
              ret[list[i]] = true
            }
            // console.log(ret)
            return ret
        },
        getMapColor(i) {
            // ['#0c32ae', '#3d60cb', '#64bae5', '#89e3f5',
            //         '#d4effd']
            // ['#8fc815', '#94cb48', '#c9e55b', '#ccf5a6', '#e7fdca']
            // ['#15c806', '#51de3c', '#4feb58',
            //                     '#8fff5f', '#88e57c', '#90f598', '#cefdcc']
            if (i === 2) return ['#067011', '#29b93e', '#3dcb3f', '#7ff58f',
                                '#a5f5ab','#dcfdd6']
            else return ['#70161D', '#b22d23', '#d65248', '#e57d6f',
                        '#f5af96', '#FDEBCF']
        }
    }
}
