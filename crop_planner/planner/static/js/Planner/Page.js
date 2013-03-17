(function (N){
    N.page = {
        models: {},
        collections: {},
        views: {},
        tmpl: {},
        data: {},

        init: function initPage() {
            new N.TemplateLoader().load(N.page.tmpl);
            this.setupAjax();

            Backbone.Tastypie.defaultLimit = 100;
            N.page.collections.crops = new N.collections.Crops();
            N.page.collections.crops.fetch();
            this.loadVarieties();

        },

        loadVarieties: function() {
            var page = this;
            N.page.collections.varieties = new N.collections.Varieties();
            N.page.collections.varieties.fetch().done(function () {
                // Guides will reference varieties, so load when done
                page.loadGuides();

                N.page.views.varietyList = new N.views.VarietyListView({
                    collection: N.page.collections.varieties,
                    el: $('#varieties')[0]
                }).render();
            });
        },

        loadGuides: function() {
            N.page.collections.guides = new N.collections.PlantingGuides();
            N.page.collections.guides.fetch().done(function () {
                N.page.views.guideList = new N.views.PlantingGuideListView({
                    collection: N.page.collections.guides,
                    el: $('#guides')[0]
                }).render();
            });
        },

        setupAjax: function() {
            var csrftoken = $.cookie('csrftoken'),
                csrfSafeMethod = function(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            };

            $.ajaxSetup({
                crossDomain: false,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type)) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
        }

    };

}(Planner));