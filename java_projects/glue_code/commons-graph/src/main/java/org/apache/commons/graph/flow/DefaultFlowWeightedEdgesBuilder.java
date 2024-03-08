package org.apache.commons.graph.flow;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.Mapper;
import static org.apache.commons.graph.utils.Assertions.checkNotNull;
public final class DefaultFlowWeightedEdgesBuilder<V, WE>
    private static Value clz = ContextInitializer.getPythonClass("/flow/DefaultFlowWeightedEdgesBuilder.py", "DefaultFlowWeightedEdgesBuilder");
    private Value obj;
    public DefaultFlowWeightedEdgesBuilder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public <W, M extends Mapper<WE, W>> FromHeadBuilder<V, WE, W> whereEdgesHaveWeights(
            M weightedEdges) {
// 
// weightedEdges =
// checkNotNull(weightedEdges, "Function to calculate edges weight can not be null.");
// return new DefaultFromHeadBuilder<V, WE, W>(graph, weightedEdges);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("whereEdgesHaveWeights", weightedEdges).as(FromHeadBuilder.class);
}
    public DefaultFlowWeightedEdgesBuilder(DirectedGraph<V, WE> graph) {
// 
// this.graph = graph;
// 

this.obj = clz.invokeMember("__init__", graph);
}
}
