function AngularUICtrl($scope) {
    $scope.date= new Date();

    $scope.keypressCallback = function($event) {
        alert('I am clicked!');
        $event.preventDefault();
    };
}
