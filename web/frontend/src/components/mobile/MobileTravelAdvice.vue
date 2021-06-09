<template>
  <div>
    <div>
      <van-field
        v-model="fieldValue"
        is-link
        readonly
        placeholder="请选择出行地区"
        @click="show = true"
      />
      <van-popup v-model="show" position="bottom">
        <van-cascader
          v-model="form.region"
          title="请选择出行地区"
          :options="data"
          :field-names="{ text: 'label'}"
          active-color="#8cc4ff"
          @close="show = false"
          @finish="onFinish"
        />
      </van-popup>
    </div>
    <div>
      <van-field
        v-model="timeValue"
        is-link
        readonly
        placeholder="请选择出行时间"
        @click="showTime = true"
      />
      <van-popup v-model="showTime" position="bottom">
        <van-datetime-picker v-model="pickValue"
                             type="date"
                             :min-date = minDate
                             :max-date = maxDate
                             @cancel="showTime = false"
                             @confirm="onConfirm"
                             >
        </van-datetime-picker>
      </van-popup>
    </div>
    <van-button color="#8cc4ff" plain block @click="onSubmit" class="button-item" id="button-item-id-1">查询</van-button>
    <div v-if="state === 1" style="padding: 20px">
      <div style="margin-top: 30px;font-size: 22px;color: #409eff;text-align: center">出行建议</div>
      <div style="margin-top: 20px">{{result.str1}}</div>
      <div v-if="result.mid.length !== 0" style="margin-top: 30px">
        <div style="font-size: 22px;color: #f56723;text-align: center">中风险地区</div>
        <div style="margin-top: 10px">{{result.mid}}</div>
      </div>
      <div v-if="result.high.length !== 0" style="margin-top: 30px">
          <div style="font-size: 22px;color: red;text-align: center">高风险地区</div>
          <div style="margin-top: 10px">
            <van-list>
              <van-cell v-for="(item,index) in result.high" :key="index" :title="item"></van-cell>
            </van-list>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import data from '../../../static/json/searchData'

export default {
  name: 'MobileTravelAdvice',
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
      minDate: new Date(new Date().getTime() + 24 * 3600 * 1000),
      maxDate: new Date(new Date().getTime() + 15 * 24 * 3600 * 1000),
      data: '',
      searchRegion: '',
      show: false,
      fieldValue: '',
      cascaderValue: '',
      showTime: false,
      timeValue: '',
      pickValue: new Date(),
      state: '',
      result: {
        str1: '',
        mid: [],
        high: []
      }
    }
  },
  mounted () {
    this.set_button_length()
    this.data = data
    var temp = this.$route.params.region
    alert(temp)
    if (temp === '/"') {
      // do nothing
    }
    else if (temp.indexOf('  ') !== -1) {
      var regions = temp.split('  ')
      if (regions[0] === '中国') {
        regions[0] = '国内'
      } else {
      }
      this.fieldValue = regions.join('/')
    }
    else {
      this.fieldValue = temp
    }
    this.state = 0
  },
  methods: {
    onSubmit () {
      var that = this
      // alert(this.form.region)
      if (this.fieldValue === '') {
        // do nothing
      } else if (this.timeValue === '') {
        // do nothing
      } else {
        that.getSearch()
        fetch('http://81.70.134.96:5000/travelAdvice', {method: 'POST',
          body: JSON.stringify({
            'region': that.searchRegion,
            'time': that.timeValue
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
    /* handleSelect (val) {
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
    }, */
    getSearch () {
      var regions = this.fieldValue.split('/')
      if (regions[0] === '国内') regions[0] = '中国'
      else regions = regions.slice(1)
      // 处理最后两个名字相同的情况
      if (regions.length > 1 && regions[regions.length - 1] === regions[regions.length - 2]) {
        regions.pop()
      }
      this.searchRegion = regions.join('  ')
    },
    onFinish ({ selectedOptions }) {
      this.show = false
      this.fieldValue = selectedOptions.map((option) => option.label).join('/')
      // console.log(this.state.fieldValue)
      // console.log(this.selectData)
      // console.log(this.searchRegion)
    },
    onConfirm () {
      var year = this.pickValue.getFullYear()
      var month = this.pickValue.getMonth()
      var date = this.pickValue.getDate()
      this.timeValue = year +
        '-' +
        (month + 1 >= 10 ? month + 1 : '0' + (month + 1)) +
        '-' +
        (date < 10 ? '0' + date : date)
      this.showTime = false
    },
    set_button_length () {
      const button1 = document.getElementById('button-item-id-1')
      button1.style.setProperty('width', window.screen.width / 10 * 9 + 'px')
      button1.style.setProperty('margin-left', window.screen.width / 20 + 'px')
    }
  }
}
</script>

<style scoped>
.button-item {
  margin-top: 10px;
  margin-bottom: 10px;
  font-size: medium;
  letter-spacing: 2px;
}
</style>
