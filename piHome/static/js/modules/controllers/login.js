'use strict';

angular.module('Auth')

.controller('LoginCtrl',
    ['$scope', 'AuthServ',
    function ($scope, AuthServ) {


    $scope.creds = {
                    username: '',
                    password: '' }

    $scope.login = function(creds) {AuthServ.login(creds)};
  
    
    }])