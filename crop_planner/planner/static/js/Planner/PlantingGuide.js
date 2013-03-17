(function (N){
    N.models.PlantingGuide = Backbone.Tastypie.Model.extend({
        urlRoot: '/api/v0.1/guide/'
    });

    N.collections.PlantingGuides = Backbone.Tastypie.Collection.extend({
        model: N.models.PlantingGuide,
        urlRoot: '/api/v0.1/guide/',
        comparator:N.Util.attrComparator('name')
    });

    N.views.PlantingGuideListView = Backbone.View.extend({
        _subViews: [],
        tagName: 'ul',

        initialize: function() {
            this.listenTo(this.collection, "add remove sort", this.render);
        },

        render: function() {
            var view = this;
            view.$el.empty();
            _.invoke(view._subViews, 'remove');
            view.collection.each(function(guide) {
                var subv = new N.views.PlantingGuideListItemView({model: guide});
                view._subViews.push(subv);
                view.$el.append(subv.render().$el);
            });
        }
    });

    N.views.PlantingGuideListItemView = Backbone.View.extend({
        initialize: function() {
            this.listenTo(this.model, "change", this.render);
        },

        render: function() {
            var html = N.page.tmpl["tmpl-guide-list-item"](this.model.toJSON());
            this.$el.html(html);
            return this;
        }
    });

}(Planner));