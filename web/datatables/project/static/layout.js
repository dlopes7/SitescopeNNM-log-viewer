
    var Component = require("./static/bower_components/pyxley/build/pyxley.js").Table;
    var type = "Table";
var options = {"params": {}, "url": "/mytable/", "className": "display", "id": "mytable", "table_options": {"columnDefs": [{"render": "<svg width=\"156\" height=\"20\"><g></g></svg>", "orderable": true, "targets": 3}], "scrollX": true, "pageLength": 9, "bSort": false, "sDom": "<\"top\">rt<\"bottom\"lp><\"clear\">", "paging": true, "deferRender": true, "searching": false, "drawCallback": "\nconfidence_interval(this.api().column(3, {\"page\":\"current\"}).data(), \"mytable\");\n", "initComplete": "\n\nnew $.fn.dataTable.FixedColumns(this, {\n    leftColumns: 1,\n    rightColumns: 0\n});\nconfidence_interval(this.api().column(3, {\"page\":\"current\"}).data(), \"mytable\");\n"}};
    React.render(
        React.createElement(Component, {
        type: type, 
options: options}),
        document.getElementById("component_id")
    );
    