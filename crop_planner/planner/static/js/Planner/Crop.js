(function (N){
    N.models.Crop = Backbone.Tastypie.Model.extend({
        urlRoot: '/api/v0.1/crop/'
    });

    N.collections.Crops = Backbone.Tastypie.Collection.extend({
        model: N.models.Crop,
        urlRoot: '/api/v0.1/crop/'
    });

}(Planner));