(function(N) {
    N.Util = {
        // Attribute comparator for collections
        attrComparator: function(attr) {
            return function(m) {return m.get(attr);}
        },

        pkFromUri: function(resourceName, uri) {
            var re = new RegExp('/api/v0.1/'+ resourceName +'/([0-9]*)/'),
                m = re.exec(uri);

            return parseInt(m[1]);
        }
    }
}(Planner));