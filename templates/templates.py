from string import Template

index_header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Table error analysis</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css">
     <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.0/js/jquery.tablesorter.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.0/css/theme.default.min.css">   <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
    $(document).ready(function() {{
        $('#index-table').tablesorter();
    }});
    </script>
  </head>
<body>
<h1>Error analysis</h1>
<table id="index-table" border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
        <th>ID</th>
        {}
    </tr>
  </thead>
  <tbody>
"""

index_content = """
    <tr>
      <td><a href="$ID.html" target="_blank">$ID</a></td>
      {}
    </tr>
"""

index_footer = """
  </tbody>
</table>
</body>
</html>
"""

table_page = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>$title</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css">
     <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.0/js/jquery.tablesorter.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.0/css/theme.default.min.css">   <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
    $(document).ready(function() {{
        $('#index-table').tablesorter();
    }});
    </script>
  </head>
<body>
<h1>$title</h1>
<table id="index-table" border="0" class="dataframe">
  <thead>
    {}
  </thead>
  <tbody>
  <tr>
      $table
  </tr>
   </tbody>
</table>
</body>
</html
"""