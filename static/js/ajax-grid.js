/* Controllers */

function AjaxGridCtrl($scope, $http) {
    $http.get('ajax?type=grid&content=list').success(function(data) {
      $scope.body = data.body;
      $scope.head = data.head;
    });

    $scope.sort = {
      column: 'name',
    };

    $scope.selectedCls = function(column) {
      return column == $scope.sort.column && 'highlight';
    };

    $scope.changeSorting = function(column) {
      var sort = $scope.sort;
      if (sort.column != column) {
        sort.column = column;
      }
    };
}
