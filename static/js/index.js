/* Controllers */

function IndexCtrl($scope, $http) {
    $http.get('ajax?type=index&content=detail').success(function(data) {
      $scope.pages = data;
    });
}
