
    var Component = require("./static/bower_components/pyxley/build/pyxley.js").FilterChart;
    var filter_style = "''";
var filters = [{"type": "SelectButton", "options": {"alias": "Data", "default": "Sitescope", "label": "Servidor", "items": ["Sitescope001", "Sitescope002", "Sitescope003", "Sitescope004"]}}];
var dynamic = "true";
var charts = [{"type": "MetricsGraphics", "options": {"params": {"left": 40, "top": 40, "chart_type": "histogram", "bins": 20, "init_params": {"Data": "Sitescope"}, "description": "Histogram", "bottom": 30, "width": 450, "animate_on_load": "true", "right": 40, "small_height_threshold": 120, "height": 200, "target": "#myhist", "title": "Histogram", "small_width_threshold": 160, "buffer": 8}, "url": "/mghist/", "chart_id": "myhist"}}, {"type": "Table", "options": {"id": "mytable", "className": "display", "table_options": {"searching": false, "paging": true, "bSort": false, "pageLength": 50}, "params": {"Data": "Sitescope"}, "url": "/mytable/"}}];
    React.render(
        React.createElement(Component, {
        filter_style: filter_style, 
filters: filters, 
dynamic: dynamic, 
charts: charts}),
        document.getElementById("component_id")
    );
    