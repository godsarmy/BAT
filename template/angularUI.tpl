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
      <ng-form name="dateForm">
        <p><input name="dateField" value="Click Here for Datepicker" ng-model="date" ui-date></p>
      </ng-form>
    </div> <!-- /container -->
{% end %}

{% block script %}
    <script src="static/js/angular-ui.js"></script>
{% end %}
