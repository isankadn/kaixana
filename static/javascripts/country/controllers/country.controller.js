/**
 * CountryController
 * @namespace thinkster.country.controllers
 */
(function () {
  'use strict';

  angular
    .module('thinkster.country.controllers')
    .controller('CountryController', CountryController);

  CountryController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Country'];

  /**
   * @namespace CountryController
   */
  function CountryController($rootScope, $scope, Authentication, Snackbar, Country) {
    var vm = this;

    vm.submit = submit;

    /**
     * @name submit
     * @desc Create a new Country
     * @memberOf thinkster.country.controllers.CountryController
     */
    function submit() {
      $rootScope.$broadcast('country.created', {
        content: vm.content,
        author: {
          username: Authentication.getAuthenticatedAccount().username
        }
      });

      $scope.closeThisDialog();

      Country.create(vm.content).then(createCountrySuccessFn, createCountryErrorFn);


      /**
       * @name createCountrySuccessFn
       * @desc Show snackbar with success message
       */
      function createCountrySuccessFn(data, status, headers, config) {
        Snackbar.show('Success! Country created.');
      }

      
      /**
       * @name createCountryErrorFn
       * @desc Propogate error event and show snackbar with error message
       */
      function createCountryErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('country.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();
