'use strict';

angular.module('Main')


.controller('MainCtrl', ["$scope","$state",'$rootScope',  function($scope, $state, $rootScope){

		$rootScope.$on('$stateChangeSuccess', 
					  function(event, toState, toParams, fromState, fromParams) {
      						$scope.data = { pageTitle: toState.data.title };
                      });

 		$scope.isActive = function(state) {
        		return state === $state.$current.name;
    			}

}])


