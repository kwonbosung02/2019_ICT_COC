import Vue from 'vue';
import Router from 'vue-router';
import Resister1 from '@/components/Resister1';
import Resister2 from '@/components/Resister2';
import Login from '@/components/Login';
import Main from '@/components/Main';
import Store from '@/components/Store';
import Reward from '@/components/Reward';
import Qrcode from '@/components/Qrcode';
import Trashcan from '@/components/Trashcan';
import Trashcan_main from '@/components/Trashcan_main';
import Trashcan_menu from '@/components/Trashcan_menu';
import Wifi from '@/components/Wifi';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Resister1',
      component: Resister1,
    },
    {
      path: '/resister1',
      name: 'Resister1',
      component: Resister1,
    },
    {
      path: '/resister2',
      name: 'Resister2',
      component: Resister2,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/main',
      name: 'Main',
      component: Main,
    },
    {
      path: '/store',
      name: 'Store',
      component: Store,
    },
    {
      path: '/reward/:id',
      name: 'Reward',
      component: Reward,
    },
    {
      path: '/qrcode',
      name: 'Qrcode',
      component: Qrcode,
    },
    {
      path: '/trashcan',
      name: 'Trashcan',
      component: Trashcan,
    },
    {
      path: '/trashcanmain',
      name: 'Trashcan_main',
      component: Trashcan_main,
    },
    {
      path: '/trashcanmenu',
      name: 'Trashcan_menu',
      component: Trashcan_menu,
    },
    {
      path: '/wifi',
      name: 'Wifi',
      component: Wifi,
    },
  ],
});
