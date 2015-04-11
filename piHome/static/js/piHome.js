'use strict';

// declare modules
angular.module('Auth', []);
angular.module('Main', []);


angular.module('piHome', [
    'Auth',             // authentication and login module
    'Main',             // for main angular controllers etc
    'ui.router',         // ui-router
    'LocalStorageModule', // local-storage 
                       // for client side JWT - 'angular-jwt', 
    'lumx'           // for material design 
])


.config(['$stateProvider','$urlRouterProvider','$httpProvider', 
            function ($stateProvider, $urlRouterProvider,  $httpProvider) {

  $urlRouterProvider.otherwise("/");

   $stateProvider

      .state('login', {
            url:'/',
            controller: 'LoginController as LgnCtrl',
            templateUrl: '/views/login',
            data: {title: 'piHome · Login' }
        })

      .state('home', {
            url:'/home',
            data: { title: 'piHome · Home'},
            templateUrl: '/views/dash'
         });

}])