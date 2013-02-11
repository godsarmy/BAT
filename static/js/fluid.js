/* Controllers */

function FluidCtrl($scope, $http) {
  $scope.get_detail = function(name) {
    $http.get('ajax?type=fluid&content=detail').success(function(data) {
      $scope.detail = data.detail;
    }).error(function() {
      alert('Fail to get data!');
    });
  }
}
