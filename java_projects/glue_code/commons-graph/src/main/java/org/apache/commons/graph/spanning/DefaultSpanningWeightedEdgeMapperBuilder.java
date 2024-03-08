package org.apache.commons.graph.spanning;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
public final class DefaultSpanningWeightedEdgeMapperBuilder<V, WE>
    private static Value clz = ContextInitializer.getPythonClass("/spanning/DefaultSpanningWeightedEdgeMapperBuilder.py", "DefaultSpanningWeightedEdgeMapperBuilder");
    private Value obj;
    public DefaultSpanningWeightedEdgeMapperBuilder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public <W> SpanningTreeSourceSelector<V, W, WE> whereEdgesHaveWeights(
            Mapper<WE, W> weightedEdges) {
// 
// weightedEdges =
// checkNotNull(weightedEdges, "Function to calculate edges weight can not be null.");
// return new DefaultSpanningTreeSourceSelector<V, W, WE>(graph, weightedEdges);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("whereEdgesHaveWeights", weightedEdges).as(SpanningTreeSourceSelector.class);
}
    public DefaultSpanningWeightedEdgeMapperBuilder(Graph<V, WE> graph) {
// 
// this.graph = graph;
// 

this.obj = clz.invokeMember("__init__", graph);
}
}
