{% extends "base.tpl" %}

{% block head %}
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }
    </style>
    <script src="static/js/socket.io.js"></script>
{% end %}

{% block body %}
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">{{ project_name }}</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="jumbotron" ng-controller="SocketIOGenCtrl">
        <h1>Socket IO assync submit!</h1>
        <p class="lead">Once a request is submitted, the handle response will be received in 3 seconds.</p>
        <form id="chatform">
          <div class="lead">{{!sending}}</div>
          <input id='btn' type='submit' class="btn btn-large btn-success" ng-click="submit()"/>
        </form>
        <div class="lead">
            <div ng-repeat="data in result">{{!data}}<div>
        </div>
    </div>

    <hr>
{% end %}

{% block script %}
  <script>var myApp = angular.module('{{moduleName}}', ['ui']);</script>
  <script src="static/js/gen.js"></script>
{% end %}
