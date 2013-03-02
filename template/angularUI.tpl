{% extends "base.tpl" %}

{% block head %}
    <!--angular ui and jquery ui js and css -->
    <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/themes/base/jquery-ui.css">
    <link rel="stylesheet" type="text/css" href="http://angular-ui.github.com/angular-ui/build/angular-ui.css">
    <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>
    <script src="http://angular-ui.github.com/angular-ui/build/angular-ui.js"></script>

    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
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
          <a class="brand" href="/">{{ project_name }}</a>
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

    <div class="container" ng-controller="AngularUICtrl">
      <div class="well">
        <h2>Calender Picker</h2>
        <p>Click the input box the pop the calender selector</p>
        <p>Formatted Date: {{! date | date: 'mediumDate'}}</p>
        <p><input name="dateField" value="Click Here for Datepicker" ng-model="date" ui-date></p>
      </div>
      <div class="well">
        <h2>Textbox with Key Event</h2>
        <p>Press [Enter] in following textbox to trigger an alert box</p>
        <textarea ui-keypress="{13:'keypressCallback($event)'}"></textarea>
      </div>
      <div class="well">
        <h2>Textbox with E-Mail address validate</h2>
        <p>Input string in the following textbox</p>
        <input name="email" placeholder="email" type="email" required="" ng-model="email" class="ng-dirty ng-valid-required ng-valid ng-valid-email">
      </div>
    </div> <!-- /container -->
{% end %}

{% block script %}
    <script>var myApp = angular.module('{{moduleName}}', ['ui']);</script>
    <script src="static/js/angular-ui.js"></script>
{% end %}
