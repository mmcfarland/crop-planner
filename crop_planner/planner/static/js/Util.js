(function(N) {
    N.Util = {
        // Attribute comparator for collections
        attrComparator: function(attr) {
            return function(m) {return m.get(attr);}
        }
    }
}(Planner));