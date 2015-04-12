'use strict';

angular.module('Auth')

.factory('AuthServ', ['$http','$state', function($http, $state){

var AuthServ = {

login : function (creds) {
 var req = {
        url: '/auth',
        skipAuthorization: true,
        method: 'POST',
        data: creds
         };
 
 return $http(req)
 			.success(function (response) {
  				console.log(response)
		       //set header to subsequent requests with the token
		       //$http.defaults.headers.common['Authorization'] = 'Bearer ' + newToken; // jshint ignore:line
		       //$state.go('dashboard');
      		})
 			.error( function (data){
       			console.log(data)
      		}); 
}
};

return AuthServ;

}]);