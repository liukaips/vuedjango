import Vue from 'vue';
import App from './App';
import router from './router';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';    // 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题
import '../static/css/icon.css';
import "babel-polyfill";

Vue.use(ElementUI, { size: 'small' });
Vue.prototype.$axios = axios;

router.beforeEach((to, from, next) => {
  if (to.path == '/login') {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
  }
  let token = localStorage.getItem('token');
  console.log(token)
  console.log('token 1111111111111111111')
  if (!token && to.path != '/login' && to.path != '/register') {
    next({ path: '/login' })
  } else {
    next()
  }
})


new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
