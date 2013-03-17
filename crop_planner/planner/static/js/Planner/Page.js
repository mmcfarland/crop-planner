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
            this.loadGuides(N.page.collections.guides);
        },

        loadVarieties: function(vStore) {
            vStore = new N.collections.Varieties();
            vStore.fetch().done(function () {
                N.page.views.varietyList = new N.views.VarietyListView({
                    collection: vStore,
                    el: $('#varieties')[0]
                }).render();
            });
        },

        loadGuides: function(store) {
            store = new N.collections.PlantingGuides();
            store.fetch().done(function () {
                N.page.views.guideList = new N.views.PlantingGuideListView({
                    collection: store,
                    el: $('#guides')[0]
                }).render();
            });
        }

    };

}(Planner));