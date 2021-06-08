<template>
  <div style="width: 100%">
    <el-row type="flex" justify="center" style="margin-top: 10%;width: 100%">
      <el-form ref="form" :model="form" label-position="left" :rules="rules" style="width: 40%">
        <el-form-item label="目的地区" prop="region" style="width: 100%" label-width="20%">
          <el-cascader prop="region"
                       style="width: 80%"
                       placeholder="请输入/选择地名"
                       ref="cascader"
                       :options="this.data"
                       v-model="form.region"
                       filterable
                       clearable/>
        </el-form-item>
        <el-form-item label="出行时间" prop="time" style="width: 100%" label-width="20%">
          <el-date-picker style="width: 80%" prop="time"
                          v-model="form.time"
                          value-format="yyyy-MM-dd"
                          align="right"
                          type="date"
                          placeholder="选择日期"
                          :picker-options="pickerOptions">
          </el-date-picker>
        </el-form-item>
        <el-form-item style="width: 100%">
          <p style="text-align: center;width: 100%">
            <el-button type="primary" @click="onSubmit" >查询</el-button>
          </p>
        </el-form-item>
      </el-form>
    </el-row>
    <el-row>
      <div v-if="state===1" style="text-align: center">
        <div>出行建议</div>
        <div>{{this.result.str1}}</div>
        <div v-if="result.str2 !==''">{{this.result.str2}}</div>
        <div v-if="result.str3 !==''">{{this.result.str3}}</div>
        <div v-if="result.str4 !==''">{{this.result.str4}}</div>
        <div></div>
      </div>
    </el-row>
  </div>
</template>

<script>
import data from '../../../static/json/searchData.json'
export default {
  name: 'TravelAdviceCom',
  data () {
    return {
      form: {
        region: [],
        time: ''
      },
      rules: {
        region: {
          required: true, message: '请输入出行地区'
        },
        time: {
          required: true, message: '请输入出行时间'
        }
      },
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() < Date.now() || time.getTime() > Date.now() + 14 * 24 * 3600 * 1000
        }
      },
      data: '',
      searchRegion: '',
      state: '',
      result: ''
    }
  },
  mounted () {
    if (this.$route.query.data.length !== 0) {
      var temp = []
      for (var i = 0; i < this.$route.query.data.length; i++) {
        temp.push(parseInt(this.$route.query.data[i]))
      }
      this.form.region = temp
    }
    this.data = data
    this.state = 0
  },
  methods: {
    onSubmit () {
      var that = this
      // alert(this.form.region)
      if (this.form.region.length === 0) {
        // do nothing
      } else if (this.form.time.length === 0) {
        // do nothing
      } else {
        that.getSearch()
        alert(this.searchRegion)
        fetch('http://81.70.134.96:5000/travelAdvice', {method: 'POST',
          body: JSON.stringify({
            'region': that.searchRegion,
            'time': that.form.time
          }),
          headers: new Headers({
            'Content-Type': 'application/json'
          })
        }).then(function (response) {
          response.json().then((data) => {
            that.state = 1
            that.result = data
          })
        }).catch(function (err) {
          alert(err.toString())
        })
      }
    },
    handleSelect (val) {
      var regions = [] // 将级联地区名以'  '连接
      // console.log(val)
      // alert(this.$refs['cascader'].getCheckedNodes())
      alert(this.$refs['cascader'].getCheckedNodes()[0].pathLabels)
      var node = this.$refs['cascader'].panel.getNodeByValue(val)
      regions.push(node.label)
      while (node.parent != null) {
        node = node.parent
        regions.push(node.label)
      }
      let type = regions.pop()
      if (type === '国内') regions.push('中国')
      // 处理最后两个名字相同的情况
      regions = regions.reverse()
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.join('  ')
    },
    getSearch () {
      var regions = this.$refs['cascader'].getCheckedNodes()[0].pathLabels
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.join('  ')
    }
  }
}
</script>

<style scoped>

</style>
