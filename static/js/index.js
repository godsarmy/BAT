/* Controllers */

function IndexCtrl($scope, $http) {
    $http.get('ajax?type=index&content=list').success(function(data) {
      $scope.pages = data;
    });
}
