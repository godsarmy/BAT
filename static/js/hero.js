/* Controllers */

function HeroCtrl($scope, $http) {
  $scope.get_detail = function(name) {
    $http.get('ajax?type=hero&content=detail').success(function(data) {
      $scope.detail = data.detail;
      alert('success!');
    }).error(function() {
      alert('Fail to get data!');
    });
  }
}
