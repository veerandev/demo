var app = angular.module("messageApp", ['ui.router']);
app.config(function($interpolateProvider, $stateProvider, $urlRouterProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    $stateProvider
    .state('home', {
        url:'/home',
        templateUrl: 'static/home.html',
        controller : "MainController"
    })

    .state('message', {
        url:'/message/:id',
        templateUrl: '/static/message.html',
        controller : "DetailsController"
    })

   $urlRouterProvider.otherwise("/home");
})

app.controller("MainController", function ($scope, $http) {

    $scope.message = {};

    $scope.submitForm = function () {
        var data = {
            user: $scope.message.username,
            content: $scope.message.content
        };
        $scope.message = {};
        var config = {
            headers : {
                'Content-Type': 'application/json'
            }
        }

        $http.post('/api/v1/message/', data, config)
        .then(
           function(response){
                $scope.messages.push(response.data[0]);
           }, 
           function(response){
             console.error('Failed to add the message');
           }
        );
    };

    $http.get("/api/v1/message/")
        .then(function (response) {
            $scope.messages = response.data;
    });   

    $scope.deleteMessage = function(message, index){
        $http.delete("/api/v1/message/"+message.pk+"/")
           .then(
               function(response){
                    $scope.messages.splice(index, 1);
               }, 
               function(response){
                 console.error('Failed to removed the message');
               }
            );
    };   
});

app.controller('DetailsController', function($scope, $http, $stateParams) {   
    $http({ url: "/api/v1/message/"+$stateParams.id+"/", 
            method: "get"
        }).then(function (response) {
            $scope.details = response.data[0];
        })
});