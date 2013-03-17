(function (N){
    N.page = {
        models: {},
        collections: {},
        views: {},
        tmpl: {},
        data: {},

        init: function initPage() {
            new N.TemplateLoader().load(N.page.tmpl);

            Backbone.Tastypie.defaultLimit = 100;
            this.loadVarieties(N.page.collections.varieties);

        },

        loadVarieties: function(vStore) {
            vStore = new N.collections.Varieties();
            vStore.fetch().done(function () {
                N.page.views.varietyList = new N.views.VarietyListView({
                    collection: vStore,
                    el: $('#varieties')[0]
                }).render();
            });
        }

    };

}(Planner));