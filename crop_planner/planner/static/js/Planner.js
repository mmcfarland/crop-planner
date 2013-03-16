(function (N) {
    "use strict";
    N.Planner = _.clone(Backbone.Events);

    N.Planner.models = {};
    N.Planner.collections = {};
    N.Planner.views = {};

    N.Planner.on('error', function handleError(model, error) {
        console.log("Planner error: " + error);
    });

}(this));