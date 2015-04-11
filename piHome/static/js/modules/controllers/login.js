'use strict';

angular.module('Auth')

.controller('LoginCtrl',
    ['$scope', 
    function ($scope) {
    var LgnCtrl = this;


    LgnCtrl.credentials = {
                    username: '',
                    password: '' }

  
    
    }])