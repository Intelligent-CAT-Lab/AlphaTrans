package org.apache.commons.graph;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.List;
import java.util.ArrayList;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.model.BaseLabeledEdge;
import org.apache.commons.graph.model.BaseLabeledVertex;
import static java.util.Collections.unmodifiableList;
public final class NodeSequenceVisitor
    private final List<BaseLabeledVertex> vertices = new ArrayList<BaseLabeledVertex>();
    private static Value clz = ContextInitializer.getPythonClass("/NodeSequenceVisitor.py", "NodeSequenceVisitor");
    private Value obj;
    public NodeSequenceVisitor(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public List<BaseLabeledVertex> onCompleted() {
// 
// return unmodifiableList(vertices);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("onCompleted").as(List.class);
}
    public VisitState discoverVertex(BaseLabeledVertex vertex) {
// 
// vertices.add(vertex);
// return VisitState.CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverVertex", vertex).as(VisitState.class);
}
}
