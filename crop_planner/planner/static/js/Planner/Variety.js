(function (N){
    N.models.Variety = Backbone.Tastypie.Model.extend({
        urlRoot: '/api/v0.1/variety/'
    });

    N.collections.Varieties = Backbone.Tastypie.Collection.extend({
        model: N.models.Variety,
        urlRoot: '/api/v0.1/variety/'
    });

    N.views.VarietyListView = Backbone.View.extend({
        _subViews: [],
        tagName: 'ul',

        initialize: function() {
            this.listenTo(this.collection, "add remove sort", this.render);
        },

        render: function() {
            this.$el.empty();
            _.invoke(this._subViews, 'remove');
            this.collection.each(function(variety) {
                var view = new N.views.VarietyListItemView({model: variety});
                _subViews.push(view);
                this.$el.append(view.render().$el);
            });
        }
    });

    N.views.VarietyListItemView = Backbone.View.extend({
        initialize: function() {
            this.listenTo(this.model, "change", this.render);
        },

        render: function() {
            var html = N.page.tmpl["tmpl-variety-list"](this.model);
            this.$el.html(html);
            return this;
        }
    });

}(Planner));