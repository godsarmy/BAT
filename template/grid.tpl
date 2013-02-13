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
    </style>
{% end %}

{% block body %}
    <div class="container-narrow">

      <div class="masthead">
        <h3 class="muted">{{ project_name }}</h3>
      </div>

      <hr>

      <div class="jumbotron">
        <h1>Browser comparison!</h1>
        <p class="lead">There are lots of browsers available in the market. Here is a grid to compare the pros and cons</p>
        <a class="btn btn-large btn-success" href="ajax-grid">Ajax Grid</a>
      </div>

      <hr>

      <div class="row-fluid marketing">
        <table class="table table-hover">
          <tr>
            <th>Name</th> <th>Creator</th> <th>Engine</th> <th>Software License</th>
          </tr>
          {% for row in data %}
            {% block row %}
          <tr>
            <td>{{ row['name'] }}</td>
            <td>{{ row['creator'] }}</td>
            <td>{{ row['engine'] }}</td>
            <td>{{ row['license'] }}</td>
          </tr>
            {% end %}
          {% end %}
        </table>
      </div>

      <hr>

      <div class="footer">
        <p>&copy; Company 2013</p>
      </div>

    </div> <!-- /container -->
{% end %}
