'use strict';

// declare modules
angular.module('Auth', []);
angular.module('Main', []);


angular.module('piHome', [
    'Auth',               // authentication and login module
    'Main',               // for main angular controllers etc
    'ui.router',          // ui-router
    'LocalStorageModule', // local-storage 
                          // for client side JWT - 'angular-jwt', 
    'lumx',               // for material design 
    'ngMaterial'
])


.run(['$rootScope', '$state', '$urlRouter', '$http', '$stateParams', function($rootScope, $state, $urlRouter, $http, $stateParams){

  console.log("HI");

}])

.config(['$stateProvider','$urlRouterProvider','$httpProvider', 
            function ($stateProvider, $urlRouterProvider,  $httpProvider) {

  $urlRouterProvider.otherwise("/login");

   $stateProvider

      .state('login', {
            url:'/login',
            templateUrl: '/views/login',
            data: {title: 'piHome · Login' }
        })

        .state('home', {
          url: '/home',
          data: {title: 'piHome · Home'
      
          },
           templateUrl: '/views/home'
          })
      .state('mgmt', {
          url: '/management',
          data: {title: 'piHome · Mnmnt'
            
          },
          templateUrl: '/views/mngmnt'
          })
      .state('stats', {
          url: '/stats',
          data: {title: 'piHome · Stats'
                
          },
          templateUrl: '/views/stats'
          })
      .state('control', {
          url: '/control',
          data: {title: 'piHome · Control'
                
          },
          templateUrl: '/views/control'                        
          })
}])