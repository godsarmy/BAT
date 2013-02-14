{% extends "base.tpl" %}

{% block head %}
    <style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 700px;
      }
      .container-narrow > hr {
        margin: 30px 0;
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

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }

      .highlight {
        text-decoration: underline;
      }
    </style>
{% end %}

{% block body %}
    <div class="container-narrow" ng-controller="AjaxGridCtrl">

      <div class="masthead">
        <h3 class="muted">{{ project_name }}</h3>
      </div>

      <hr>

      <div class="jumbotron">
        <h1>Browser comparison!</h1>
        <p class="lead">There are lots of browsers available in the market. Here is a grid to compare the pros and cons. Click the grid head to sort the column.</p>
        <a class="btn btn-large btn-success" href="static-grid">Static Grid</a>
      </div>

      <hr>

      <div class="row-fluid marketing">
        <table class="table table-striped table-bordered">
          <tr>
            <th ng-repeat="t in head" ng:class="selectedCls(t.key)" ng:click="changeSorting(t.key)">{{! t.desc }}</th>
          </tr>
          <tr ng-repeat="row in body | orderBy:sort.column">
            <td>{{! row.name }}</td>
            <td>{{! row.creator }}</td>
            <td>{{! row.engine }}</td>
            <td>{{! row.license }}</td>
          </tr>
        </table>
      </div>

      <hr>

      <div class="footer">
        <p>&copy; Company 2013</p>
      </div>

    </div> <!-- /container -->
{% end %}

{% block script %}
    <script src="static/js/ajax-grid.js"></script>
{% end %}
