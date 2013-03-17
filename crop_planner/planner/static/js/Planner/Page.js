(function (N){
    N.page = {
        models: {},
        views: {},
        tmpl: {},
        data: {},

        init: function initPage() {
            Backbone.Tastypie.defaultLimit = 100;

            // TODO: load varieties and render
        }

    };

    new TemplateLoader().load(N.page.tmpl);

}(Planner));