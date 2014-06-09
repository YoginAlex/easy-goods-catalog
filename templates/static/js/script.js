'use strict';

var app = angular.module('MyApp', ['ngResource', 'ngRoute']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

app.config(function($locationProvider, $routeProvider) {
    $routeProvider
        .when('/goods_type/:goods_type_id', {
            controller: 'MainContentController',
            templateUrl: 'static/html/item_list.html',
        })
        .when('/item/:item_id', {
            controller: 'ItemContentController',
            templateUrl: 'static/html/item.html',
        });
        // .when('oneitem/:item_id/photos', {
        //     controller: 'PhotoContentController',
        //     templateUrl: 'static/html/photo.html',
        // });

    // $locationProvider.html5Mode(true);    
});

app.controller('MainContentController', function($scope, $routeParams, $http){
    $scope.params = $routeParams;    

    var get_url = 'api/goods_type/' + $scope.params.goods_type_id
    $http.get(get_url).success(function(data) {
        $scope.items = data;
    });
});

app.controller('ItemContentController', function($scope, $routeParams, $http){
    $scope.params = $routeParams;    

    var get_url = 'api/oneitem/' + $scope.params.item_id
    $http.get(get_url).success(function(data) {
        $scope.item = data;
    });
});

app.controller('TypesCtrl', function($scope, $http) {
    $http.get('api/type_list').success(function(data) {
        $scope.types = data;
    });
});
