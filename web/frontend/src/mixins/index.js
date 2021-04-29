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
    }
  }
}