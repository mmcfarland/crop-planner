(function (N){
    N.page = {
        models: {},
        views: {},
        tmpl: {},
        data: {},

        init: function initPage() {
            Backbone.Tastypie.defaultLimit = 50;
        }

    };

    new TemplateLoader().load(N.page.tmpl);

}(Planner));