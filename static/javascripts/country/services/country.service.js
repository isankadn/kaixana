/**
 * Created by isanka on 2/15/15.
 */
/**
 * Posts
 * @namespace thinkster.posts.services
 */
(function () {
  'use strict';

  angular
    .module('thinkster.country.services')
    .factory('Country', Country);

  Country.$inject = ['$http'];

  /**
   * @namespace Posts
   * @returns {Factory}
   */
  function Country($http) {
    var Country = {
      all: all,
      get: get,
      create: create
    };

    return Country;

    ////////////////////

    /**
     * @name all
     * @desc Get all Posts
     * @returns {Promise}
     * @memberOf thinkster.country.services.country
     */
    function all() {
      return $http.get('/api/v1/country/');
    }


    /**
     * @name create
     * @desc Create a new Post
     * @param {string} content The content of the new Post
     * @returns {Promise}
     * @memberOf thinkster.country.services.country
     */
    function create(content) {
      return $http.country('/api/v1/country/', {
        content: content
      });
    }


    /**
     * @name get
     * @desc Get the Posts of a given user
     * @param {string} username The username to get Posts for
     * @returns {Promise}
     * @memberOf thinkster.country.services.country
     */
    function get(id) {
      return $http.get('/api/v1/country/');
    }
  }
})();
