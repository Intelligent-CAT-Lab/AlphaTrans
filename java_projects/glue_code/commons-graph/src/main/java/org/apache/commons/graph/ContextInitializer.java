package org.apache.commons.graph;
import org.apache.commons.graph.collections.FibonacciHeap;import org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations;import org.apache.commons.graph.flow.new AbstractGraphConnection<V,EdgeWrapper<WE>>(...) { ... };import org.apache.commons.graph.flow.EdgeWrapper;import org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector;import org.apache.commons.graph.flow.MapperWrapper;import org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations;import org.apache.commons.graph.elo.DefaultRankingSelector;import org.apache.commons.graph.elo.GameResult;import org.apache.commons.graph.flow.FlowNetworkHandler;import org.apache.commons.graph.export.AbstractExporter;import org.apache.commons.graph.visit.VisitState;import org.apache.commons.graph.visit.DefaultVisitSourceSelector;import org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder;import org.apache.commons.graph.model.RevertedGraph;import org.apache.commons.graph.collections.DisjointSetNode;import org.apache.commons.graph.visit.VisitGraphBuilder;import org.apache.commons.graph.model.InMemoryPath;import org.apache.commons.graph.flow.DefaultFromHeadBuilder;import org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations;import org.apache.commons.graph.utils.Assertions;import org.apache.commons.graph.shortestpath.PredecessorsList;import org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder;import org.apache.commons.graph.builder.DefaultHeadVertexConnector;import org.apache.commons.graph.builder.AbstractGraphConnection;import org.apache.commons.graph.spanning.ReverseDeleteGraph;import org.apache.commons.graph.elo.DefaultKFactorBuilder;import org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector;import org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder;import org.apache.commons.graph.utils.Objects;import org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector;import org.apache.commons.graph.scc.KosarajuSharirAlgorithm;import org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector;import org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector;import org.apache.commons.graph.builder.DefaultLinkedConnectionBuilder;import org.apache.commons.graph.model.MutableSpanningTree;import org.apache.commons.graph.visit.BaseGraphVisitHandler;import org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath;import org.apache.commons.graph.collections.FibonacciHeapNode;import org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector;import org.apache.commons.graph.coloring.UncoloredOrderedVertices;import org.apache.commons.graph.coloring.new Iterator<V>(...) { ... };import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;import org.apache.commons.graph.coloring.ColoredVertices;import org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector;import org.apache.commons.graph.model.BaseMutableGraph;import org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector;import org.apache.commons.graph.shortestpath.DefaultPathSourceSelector;import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;import org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector;import org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations;import org.apache.commons.graph.spanning.SuperVertex;import org.apache.commons.graph.scc.TarjanAlgorithm;import org.apache.commons.graph.builder.DefaultGrapher;import org.apache.commons.graph.coloring.DefaultColorsBuilder;import org.apache.commons.graph.flow.DefaultToTailBuilder;import org.apache.commons.graph.export.DotExporter;import org.apache.commons.graph.spanning.WeightedEdgesComparator;import org.apache.commons.graph.scc.TarjanVertexMetaInfo;import org.apache.commons.graph.model.InMemoryWeightedPath;import org.apache.commons.graph.builder.DefaultTailVertexConnector;import org.apache.commons.graph.spanning.ShortestEdges;import org.apache.commons.graph.connectivity.ConnectedComponentHandler;import org.apache.commons.graph.model.DirectedMutableGraph;import org.apache.commons.graph.model.BaseGraph;import org.apache.commons.graph.export.DefaultExportSelector;import org.apache.commons.graph.model.UndirectedMutableGraph;import org.apache.commons.graph.connectivity.DefaultConnectivityBuilder;import org.apache.commons.graph.collections.DisjointSet;import org.apache.commons.graph.scc.DefaultSccAlgorithmSelector;import org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm;import org.apache.commons.graph.shortestpath.ShortestDistances;
import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/commons-graph/src/main/java/org/apache/commons/graph/";
    private static String packageDirectory = "../../../data/verified_projects/commons-graph/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
.targetTypeMapping(Value.class, FibonacciHeap.class, null, (v) -> new FibonacciHeap(v))
.targetTypeMapping(Value.class, BigDecimalWeightBaseOperations.class, null, (v) -> new BigDecimalWeightBaseOperations(v))
.targetTypeMapping(Value.class, DefaultMaxFlowAlgorithmSelector.new AbstractGraphConnection<V,EdgeWrapper<WE>>(...) { ... }.class, null, (v) -> new DefaultMaxFlowAlgorithmSelector.new AbstractGraphConnection<V,EdgeWrapper<WE>>(...) { ... }(v))
.targetTypeMapping(Value.class, DefaultMaxFlowAlgorithmSelector.EdgeWrapper.class, null, (v) -> new DefaultMaxFlowAlgorithmSelector.EdgeWrapper(v))
.targetTypeMapping(Value.class, DefaultMaxFlowAlgorithmSelector.class, null, (v) -> new DefaultMaxFlowAlgorithmSelector(v))
.targetTypeMapping(Value.class, DefaultMaxFlowAlgorithmSelector.MapperWrapper.class, null, (v) -> new DefaultMaxFlowAlgorithmSelector.MapperWrapper(v))
.targetTypeMapping(Value.class, FloatWeightBaseOperations.class, null, (v) -> new FloatWeightBaseOperations(v))
.targetTypeMapping(Value.class, DefaultRankingSelector.class, null, (v) -> new DefaultRankingSelector(v))
.targetTypeMapping(Value.class, GameResult.class, null, (v) -> new GameResult(v))
.targetTypeMapping(Value.class, FlowNetworkHandler.class, null, (v) -> new FlowNetworkHandler(v))
.targetTypeMapping(Value.class, AbstractExporter.class, null, (v) -> new AbstractExporter(v))
.targetTypeMapping(Value.class, VisitState.class, null, (v) -> new VisitState(v))
.targetTypeMapping(Value.class, DefaultVisitSourceSelector.class, null, (v) -> new DefaultVisitSourceSelector(v))
.targetTypeMapping(Value.class, DefaultFlowWeightedEdgesBuilder.class, null, (v) -> new DefaultFlowWeightedEdgesBuilder(v))
.targetTypeMapping(Value.class, RevertedGraph.class, null, (v) -> new RevertedGraph(v))
.targetTypeMapping(Value.class, DisjointSetNode.class, null, (v) -> new DisjointSetNode(v))
.targetTypeMapping(Value.class, VisitGraphBuilder.class, null, (v) -> new VisitGraphBuilder(v))
.targetTypeMapping(Value.class, InMemoryPath.class, null, (v) -> new InMemoryPath(v))
.targetTypeMapping(Value.class, DefaultFromHeadBuilder.class, null, (v) -> new DefaultFromHeadBuilder(v))
.targetTypeMapping(Value.class, SynchronizedUndirectedGraph.class, null, (v) -> new SynchronizedUndirectedGraph(v))
.targetTypeMapping(Value.class, BigIntegerWeightBaseOperations.class, null, (v) -> new BigIntegerWeightBaseOperations(v))
.targetTypeMapping(Value.class, Assertions.class, null, (v) -> new Assertions(v))
.targetTypeMapping(Value.class, SynchronizedGraph.class, null, (v) -> new SynchronizedGraph(v))
.targetTypeMapping(Value.class, PredecessorsList.class, null, (v) -> new PredecessorsList(v))
.targetTypeMapping(Value.class, DefaultHeuristicBuilder.class, null, (v) -> new DefaultHeuristicBuilder(v))
.targetTypeMapping(Value.class, DefaultHeadVertexConnector.class, null, (v) -> new DefaultHeadVertexConnector(v))
.targetTypeMapping(Value.class, AbstractGraphConnection.class, null, (v) -> new AbstractGraphConnection(v))
.targetTypeMapping(Value.class, VertexPair.class, null, (v) -> new VertexPair(v))
.targetTypeMapping(Value.class, ReverseDeleteGraph.class, null, (v) -> new ReverseDeleteGraph(v))
.targetTypeMapping(Value.class, DefaultKFactorBuilder.class, null, (v) -> new DefaultKFactorBuilder(v))
.targetTypeMapping(Value.class, DefaultVisitAlgorithmsSelector.class, null, (v) -> new DefaultVisitAlgorithmsSelector(v))
.targetTypeMapping(Value.class, DefaultSpanningWeightedEdgeMapperBuilder.class, null, (v) -> new DefaultSpanningWeightedEdgeMapperBuilder(v))
.targetTypeMapping(Value.class, Objects.class, null, (v) -> new Objects(v))
.targetTypeMapping(Value.class, DefaultWeightedEdgesSelector.class, null, (v) -> new DefaultWeightedEdgesSelector(v))
.targetTypeMapping(Value.class, KosarajuSharirAlgorithm.class, null, (v) -> new KosarajuSharirAlgorithm(v))
.targetTypeMapping(Value.class, DefaultColoringAlgorithmsSelector.class, null, (v) -> new DefaultColoringAlgorithmsSelector(v))
.targetTypeMapping(Value.class, DefaultSpanningTreeSourceSelector.class, null, (v) -> new DefaultSpanningTreeSourceSelector(v))
.targetTypeMapping(Value.class, DefaultLinkedConnectionBuilder.class, null, (v) -> new DefaultLinkedConnectionBuilder(v))
.targetTypeMapping(Value.class, MutableSpanningTree.class, null, (v) -> new MutableSpanningTree(v))
.targetTypeMapping(Value.class, BaseGraphVisitHandler.class, null, (v) -> new BaseGraphVisitHandler(v))
.targetTypeMapping(Value.class, AllVertexPairsShortestPath.class, null, (v) -> new AllVertexPairsShortestPath(v))
.targetTypeMapping(Value.class, FibonacciHeapNode.class, null, (v) -> new FibonacciHeapNode(v))
.targetTypeMapping(Value.class, DefaultSpanningTreeAlgorithmSelector.class, null, (v) -> new DefaultSpanningTreeAlgorithmSelector(v))
.targetTypeMapping(Value.class, UncoloredOrderedVertices.class, null, (v) -> new UncoloredOrderedVertices(v))
.targetTypeMapping(Value.class, UncoloredOrderedVertices.new Iterator<V>(...) { ... }.class, null, (v) -> new UncoloredOrderedVertices.new Iterator<V>(...) { ... }(v))
.targetTypeMapping(Value.class, SynchronizedDirectedGraph.class, null, (v) -> new SynchronizedDirectedGraph(v))
.targetTypeMapping(Value.class, LongWeightBaseOperations.class, null, (v) -> new LongWeightBaseOperations(v))
.targetTypeMapping(Value.class, ColoredVertices.class, null, (v) -> new ColoredVertices(v))
.targetTypeMapping(Value.class, DefaultTargetSourceSelector.class, null, (v) -> new DefaultTargetSourceSelector(v))
.targetTypeMapping(Value.class, CommonsGraph.class, null, (v) -> new CommonsGraph(v))
.targetTypeMapping(Value.class, BaseMutableGraph.class, null, (v) -> new BaseMutableGraph(v))
.targetTypeMapping(Value.class, DefaultConnectivityAlgorithmsSelector.class, null, (v) -> new DefaultConnectivityAlgorithmsSelector(v))
.targetTypeMapping(Value.class, DefaultPathSourceSelector.class, null, (v) -> new DefaultPathSourceSelector(v))
.targetTypeMapping(Value.class, IntegerWeightBaseOperations.class, null, (v) -> new IntegerWeightBaseOperations(v))
.targetTypeMapping(Value.class, DefaultShortestPathAlgorithmSelector.class, null, (v) -> new DefaultShortestPathAlgorithmSelector(v))
.targetTypeMapping(Value.class, DoubleWeightBaseOperations.class, null, (v) -> new DoubleWeightBaseOperations(v))
.targetTypeMapping(Value.class, SuperVertex.class, null, (v) -> new SuperVertex(v))
.targetTypeMapping(Value.class, TarjanAlgorithm.class, null, (v) -> new TarjanAlgorithm(v))
.targetTypeMapping(Value.class, DefaultGrapher.class, null, (v) -> new DefaultGrapher(v))
.targetTypeMapping(Value.class, DefaultColorsBuilder.class, null, (v) -> new DefaultColorsBuilder(v))
.targetTypeMapping(Value.class, DefaultToTailBuilder.class, null, (v) -> new DefaultToTailBuilder(v))
.targetTypeMapping(Value.class, DotExporter.class, null, (v) -> new DotExporter(v))
.targetTypeMapping(Value.class, WeightedEdgesComparator.class, null, (v) -> new WeightedEdgesComparator(v))
.targetTypeMapping(Value.class, TarjanVertexMetaInfo.class, null, (v) -> new TarjanVertexMetaInfo(v))
.targetTypeMapping(Value.class, InMemoryWeightedPath.class, null, (v) -> new InMemoryWeightedPath(v))
.targetTypeMapping(Value.class, DefaultTailVertexConnector.class, null, (v) -> new DefaultTailVertexConnector(v))
.targetTypeMapping(Value.class, ShortestEdges.class, null, (v) -> new ShortestEdges(v))
.targetTypeMapping(Value.class, ConnectedComponentHandler.class, null, (v) -> new ConnectedComponentHandler(v))
.targetTypeMapping(Value.class, DirectedMutableGraph.class, null, (v) -> new DirectedMutableGraph(v))
.targetTypeMapping(Value.class, BaseGraph.class, null, (v) -> new BaseGraph(v))
.targetTypeMapping(Value.class, DefaultExportSelector.class, null, (v) -> new DefaultExportSelector(v))
.targetTypeMapping(Value.class, UndirectedMutableGraph.class, null, (v) -> new UndirectedMutableGraph(v))
.targetTypeMapping(Value.class, DefaultConnectivityBuilder.class, null, (v) -> new DefaultConnectivityBuilder(v))
.targetTypeMapping(Value.class, SynchronizedMutableGraph.class, null, (v) -> new SynchronizedMutableGraph(v))
.targetTypeMapping(Value.class, DisjointSet.class, null, (v) -> new DisjointSet(v))
.targetTypeMapping(Value.class, DefaultSccAlgorithmSelector.class, null, (v) -> new DefaultSccAlgorithmSelector(v))
.targetTypeMapping(Value.class, CheriyanMehlhornGabowAlgorithm.class, null, (v) -> new CheriyanMehlhornGabowAlgorithm(v))
.targetTypeMapping(Value.class, ShortestDistances.class, null, (v) -> new ShortestDistances(v))
// TODO: Add other mappings
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowHostAccess(hostAccess)
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        } catch (Exception e) {
            System.out.println("[-] " + e);
        }
    }
    public static Value[] getPythonClasses(String fileName, String... classNames) {
        try {
            File file = new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }
            return result;
        } catch (Exception e) {
            System.out.println("[-] " + e);
            return null; // ??
        }
    }
    public static Value getPythonClass(String fileName, String className) {
        return getPythonClasses(fileName, className)[0];
    }
}
