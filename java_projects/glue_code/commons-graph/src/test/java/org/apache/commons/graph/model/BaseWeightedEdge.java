package org.apache.commons.graph;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.io.Serializable;
import org.apache.commons.graph.Mapper;
public final class BaseWeightedEdge<W>
    private static final long serialVersionUID = -2024378704087762740L;
    private static Value clz = ContextInitializer.getPythonClass("/BaseWeightedEdge.py", "BaseWeightedEdge");
    private Value obj;
    public BaseWeightedEdge(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public W map(BaseLabeledWeightedEdge<W> edge) {
// 
// return edge.getWeight();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("map", edge).as(W.class);
}
}
