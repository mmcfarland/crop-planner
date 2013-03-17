(function (N){
    N.models.Variety = Backbone.Tastypie.Model.extend({
        urlRoot: '/api/v0.1/variety/'
    });

    N.collections.Varieties = Backbone.Tastypie.Collection.extend({
        model: N.models.Variety,
        urlRoot: '/api/v0.1/variety/',
        comparator: N.Util.attrComparator('name')
    });

    N.views.VarietyListView = Backbone.View.extend({
        _subViews: [],
        tagName: 'ul',

        initialize: function() {
            this.listenTo(this.collection, "add remove sort", this.render);
        },

        render: function() {
            var view = this;
            view.$el.empty();
            _.invoke(view._subViews, 'remove');
            view.collection.each(function(variety) {
                var subv = new N.views.VarietyListItemView({model: variety});
                view._subViews.push(subv);
                view.$el.append(subv.render().$el);
            });
        }
    });

    N.views.VarietyListItemView = Backbone.View.extend({
        initialize: function() {
            this.listenTo(this.model, "change", this.render);
        },

        render: function() {
            var html = N.page.tmpl["tmpl-variety-list-item"](this.model.toJSON());
            this.$el.html(html);
            return this;
        }
    });

}(Planner));