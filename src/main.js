import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import catalogContainer from "./components/catalogContainer.vue"
import axios from 'axios';

var VueCookie = require('vue-cookie');
// Tell Vue to use the plugin
Vue.use(VueCookie);

console.log("dsfdfsdfsdfsdf")

Vue.use(Buefy)

new Vue({
	el: '#app',
	data() {
		return {
			data: {
				razon_social: "",
				cve_corta: "",
				observaciones: "",
				consecutivo: 0,
			},
			list: [],
		}
	},
	components: {
    	catalogContainer,
  	},
  	methods: {
  		submit: function(){
  			console.log("holiii")
  			console.log(this.data)
  			var csrftoken = this.$cookie.get('csrftoken');
  			axios.defaults.headers.common['cookiename'] = 'csrftoken';
  			axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
  			axios.defaults.headers.common['Access-Control-Allow-Origin'] = "*";
  			axios({
  			    method: 'post',
  			    url: 'http://localhost:8000/create/',
  			    data: JSON.stringify(this.data)
  			}).then(res => {
  				console.log(res.request.response)
  				this.getData()
  				this.data = {}
  			})
  			// axios.post('http://localhost:8000', data)
  			//     .then(res => console.log(res.request.response))

  		},

  		getData: function(){
  			axios.get(`http://localhost:8000/oficinas/`)
  			.then(response => {
  			  // JSON responses are automatically parsed.
  			  this.list = JSON.parse(response.data)
  			})
  			.catch(e => {
  			  this.errors.push(e)
  			})
  		}
  	},
  	created() {
  	   axios.get(`http://localhost:8000/oficinas/`)
  	   .then(response => {
  	     // JSON responses are automatically parsed.
  	     this.list = JSON.parse(response.data)
  	   })
  	   .catch(e => {
  	     this.errors.push(e)
  	   })
  	}
	// render: h => h(App)
})
