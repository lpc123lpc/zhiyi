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
    getCountryName() {
        var json = require('../../static/json/map/world/world-mapping.json')
        var engName
        for (let i in json) {
            // console.log(i)
            if (json[i].cn == this.country) {
                engName = i
                if (i == 'China') engName = 'china'
                return [json[i].mapFileName, engName]
            }
        }
      }
  }
}