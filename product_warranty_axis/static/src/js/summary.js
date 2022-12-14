odoo.define('product_warranty_axis.helpdesk_dashboard', function (require) {
"use strict";
var BoardView = require('board.BoardView');
var viewRegistry = require('web.view_registry');
var FormRenderer = require('web.FormRenderer');

var BoardView = BoardView.extend({
    config: _.extend({}, BoardView.prototype.config, {
      
    }),

    init: function () {
        this._super.apply(this, arguments);
        this.controllerParams.customViewID = '';
    },
});
viewRegistry.add('board', BoardView);

});



