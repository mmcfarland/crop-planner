(function (N){
    N.models.Variety = Backbone.Tastypie.Model.extend({
        urlRoot: '/api/v0.1/variety/'
    });

    N.collections.Varieties = Backbone.Tastypie.Collection.extend({
        model: N.models.Variety,
        urlRoot: '/api/v0.1/variety/'
    });


}(Planner));