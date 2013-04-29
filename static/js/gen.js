/* Controllers */

function SocketIOGenCtrl($scope, $http) {

    $scope.num = 0;
    $scope.result = [];

    var query = new io.connect('http://' + window.location.host);
    // Establish event handlers
    query.on('disconnect', function() {
        query.socket.reconnect();
    });

    // Query
    query.on('response', function(data) {
        $scope.$apply(function () {
            $scope.result.push(data);
        });
    });

    $scope.submit = function() {
        query.emit('query', $scope.num);
        
        $scope.sending = 'Sent ' + $scope.num + '...';
        $scope.num += 1;
    }
}
