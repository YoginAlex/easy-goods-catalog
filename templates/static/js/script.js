'use strict';

var app = angular.module('MyApp', ['ngRoute']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

app.config(function($locationProvider, $routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'MainContentController',
            templateUrl: 'static/html/item_list.html',
        })
        .when('/goods_type/:goods_type_id', {
            controller: 'GoodsListContentController',
            templateUrl: 'static/html/item_list.html',
        })
        .when('/item/:item_id', {
            controller: 'ItemContentController',
            templateUrl: 'static/html/item.html',
        })
        .otherwise({
            retirectTo: '/'
        });
    // $locationProvider.html5Mode(true);    
});

app.controller('TypesCtrl', function($scope, $http, $location) {
    $http.get('api/type_list').success(function(data) {
        $scope.types = data;
    });

    $scope.typeClass = function(type){
        if ($location.path() == '/goods_type/'+type.id) {
            return 'active';            
        }
        else {
            return '';
        }
    };
});

app.controller('MainContentController', function($scope, $http){
    $http.get('api/main_list').success(function(data) {
        $scope.items = data;
    });
});

app.controller('GoodsListContentController', function($scope, $routeParams, $http){
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
