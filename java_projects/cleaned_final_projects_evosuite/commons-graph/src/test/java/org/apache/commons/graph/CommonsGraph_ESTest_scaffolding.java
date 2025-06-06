
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.graph;

import org.evosuite.runtime.annotation.EvoSuiteClassExclude;
import org.junit.BeforeClass;
import org.junit.Before;
import org.junit.After;
import org.junit.AfterClass;
import org.evosuite.runtime.sandbox.Sandbox;
import org.evosuite.runtime.sandbox.Sandbox.SandboxMode;

import static org.evosuite.shaded.org.mockito.Mockito.*;
@EvoSuiteClassExclude
public class CommonsGraph_ESTest_scaffolding {

  @org.junit.Rule
  public org.evosuite.runtime.vnet.NonFunctionalRequirementRule nfr = new org.evosuite.runtime.vnet.NonFunctionalRequirementRule();

  private static final java.util.Properties defaultProperties = (java.util.Properties) java.lang.System.getProperties().clone(); 

  private org.evosuite.runtime.thread.ThreadStopper threadStopper =  new org.evosuite.runtime.thread.ThreadStopper (org.evosuite.runtime.thread.KillSwitchHandler.getInstance(), 3000);


  @BeforeClass
  public static void initEvoSuiteFramework() { 
    org.evosuite.runtime.RuntimeSettings.className = "org.apache.commons.graph.CommonsGraph"; 
    org.evosuite.runtime.GuiSupport.initialize(); 
    org.evosuite.runtime.RuntimeSettings.maxNumberOfThreads = 100; 
    org.evosuite.runtime.RuntimeSettings.maxNumberOfIterationsPerLoop = 10000; 
    org.evosuite.runtime.RuntimeSettings.mockSystemIn = true; 
    org.evosuite.runtime.RuntimeSettings.sandboxMode = org.evosuite.runtime.sandbox.Sandbox.SandboxMode.RECOMMENDED; 
    org.evosuite.runtime.sandbox.Sandbox.initializeSecurityManagerForSUT(); 
    org.evosuite.runtime.classhandling.JDKClassResetter.init();
    setSystemProperties();
    initializeClasses();
    org.evosuite.runtime.Runtime.getInstance().resetRuntime(); 
    try { initMocksToAvoidTimeoutsInTheTests(); } catch(ClassNotFoundException e) {} 
  } 

  @AfterClass
  public static void clearEvoSuiteFramework(){ 
    Sandbox.resetDefaultSecurityManager(); 
    java.lang.System.setProperties((java.util.Properties) defaultProperties.clone()); 
  } 

  @Before
  public void initTestCase(){ 
    threadStopper.storeCurrentThreads();
    threadStopper.startRecordingTime();
    org.evosuite.runtime.jvm.ShutdownHookHandler.getInstance().initHandler(); 
    org.evosuite.runtime.sandbox.Sandbox.goingToExecuteSUTCode(); 
    setSystemProperties(); 
    org.evosuite.runtime.GuiSupport.setHeadless(); 
    org.evosuite.runtime.Runtime.getInstance().resetRuntime(); 
    org.evosuite.runtime.agent.InstrumentingAgent.activate(); 
  } 

  @After
  public void doneWithTestCase(){ 
    threadStopper.killAndJoinClientThreads();
    org.evosuite.runtime.jvm.ShutdownHookHandler.getInstance().safeExecuteAddedHooks(); 
    org.evosuite.runtime.classhandling.JDKClassResetter.reset(); 
    resetClasses(); 
    org.evosuite.runtime.sandbox.Sandbox.doneWithExecutingSUTCode(); 
    org.evosuite.runtime.agent.InstrumentingAgent.deactivate(); 
    org.evosuite.runtime.GuiSupport.restoreHeadlessMode(); 
  } 

  public static void setSystemProperties() {
 
    java.lang.System.setProperties((java.util.Properties) defaultProperties.clone()); 
    java.lang.System.setProperty("user.dir", "/home/ali/Documents/AlphaTrans/java_projects/cleaned_final_projects/commons-graph"); 
    java.lang.System.setProperty("java.io.tmpdir", "/tmp"); 
  }

  private static void initializeClasses() {
    org.evosuite.runtime.classhandling.ClassStateSupport.initializeClasses(CommonsGraph_ESTest_scaffolding.class.getClassLoader() ,
      "org.apache.commons.graph.export.GraphExportException",
      "org.apache.commons.graph.elo.RankingSelector",
      "org.apache.commons.graph.Graph",
      "org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder",
      "org.apache.commons.graph.UndirectedGraph",
      "org.apache.commons.graph.builder.DefaultLinkedConnectionBuilder",
      "org.apache.commons.graph.SynchronizedUndirectedGraph",
      "org.apache.commons.graph.shortestpath.PathSourceSelector",
      "org.apache.commons.graph.model.DirectedMutableGraph",
      "org.apache.commons.graph.model.UndirectedMutableGraph",
      "org.apache.commons.graph.builder.GraphConnector",
      "org.apache.commons.graph.export.NamedExportSelector",
      "org.apache.commons.graph.elo.KFactorBuilder",
      "org.apache.commons.graph.SynchronizedDirectedGraph",
      "org.apache.commons.graph.builder.DefaultGrapher",
      "org.apache.commons.graph.flow.FromHeadBuilder",
      "org.apache.commons.graph.visit.VisitSourceSelector",
      "org.apache.commons.graph.scc.SccAlgorithmSelector",
      "org.apache.commons.graph.SynchronizedGraph",
      "org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder",
      "org.apache.commons.graph.builder.GraphConnection",
      "org.apache.commons.graph.elo.GameResult",
      "org.apache.commons.graph.MutableGraph",
      "org.apache.commons.graph.model.BaseGraph",
      "org.apache.commons.graph.Mapper",
      "org.apache.commons.graph.scc.DefaultSccAlgorithmSelector",
      "org.apache.commons.graph.spanning.SpanningTreeSourceSelector",
      "org.apache.commons.graph.CommonsGraph",
      "org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder",
      "org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder",
      "org.apache.commons.graph.utils.Assertions",
      "org.apache.commons.graph.coloring.ColoringAlgorithmsSelector",
      "org.apache.commons.graph.builder.HeadVertexConnector",
      "org.apache.commons.graph.export.ExportSelector",
      "org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector",
      "org.apache.commons.graph.visit.DefaultVisitSourceSelector",
      "org.apache.commons.graph.elo.PlayersRank",
      "org.apache.commons.graph.builder.LinkedConnectionBuilder",
      "org.apache.commons.graph.elo.DefaultRankingSelector",
      "org.apache.commons.graph.export.AbstractExporter",
      "org.apache.commons.graph.connectivity.ConnectivityBuilder",
      "org.apache.commons.graph.export.DefaultExportSelector",
      "org.apache.commons.graph.connectivity.DefaultConnectivityBuilder",
      "org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector",
      "org.apache.commons.graph.flow.FlowWeightedEdgesBuilder",
      "org.apache.commons.graph.model.BaseMutableGraph",
      "org.apache.commons.graph.VertexPair",
      "org.apache.commons.graph.utils.Objects",
      "org.apache.commons.graph.coloring.DefaultColorsBuilder",
      "org.apache.commons.graph.coloring.ColorsBuilder",
      "org.apache.commons.graph.GraphException",
      "org.apache.commons.graph.DirectedGraph",
      "org.apache.commons.graph.SynchronizedMutableGraph",
      "org.apache.commons.graph.export.DotExporter",
      "org.apache.commons.graph.scc.SccAlgorithm",
      "org.apache.commons.graph.visit.VisitAlgorithmsSelector"
    );
  } 
  private static void initMocksToAvoidTimeoutsInTheTests() throws ClassNotFoundException { 
    mock(Class.forName("org.apache.commons.graph.builder.GraphConnection", false, CommonsGraph_ESTest_scaffolding.class.getClassLoader()));
  }

  private static void resetClasses() {
    org.evosuite.runtime.classhandling.ClassResetter.getInstance().setClassLoader(CommonsGraph_ESTest_scaffolding.class.getClassLoader()); 

    org.evosuite.runtime.classhandling.ClassStateSupport.resetClasses(
      "org.apache.commons.graph.CommonsGraph",
      "org.apache.commons.graph.model.BaseGraph",
      "org.apache.commons.graph.model.BaseMutableGraph",
      "org.apache.commons.graph.model.DirectedMutableGraph",
      "org.apache.commons.graph.SynchronizedGraph",
      "org.apache.commons.graph.SynchronizedMutableGraph",
      "org.apache.commons.graph.SynchronizedUndirectedGraph",
      "org.apache.commons.graph.GraphException",
      "org.apache.commons.graph.SynchronizedDirectedGraph",
      "org.apache.commons.graph.model.UndirectedMutableGraph",
      "org.apache.commons.graph.builder.DefaultLinkedConnectionBuilder",
      "org.apache.commons.graph.utils.Assertions",
      "org.apache.commons.graph.builder.DefaultGrapher",
      "org.apache.commons.graph.utils.Objects",
      "org.apache.commons.graph.coloring.DefaultColorsBuilder",
      "org.apache.commons.graph.scc.DefaultSccAlgorithmSelector",
      "org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder",
      "org.apache.commons.graph.elo.DefaultRankingSelector",
      "org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder",
      "org.apache.commons.graph.VertexPair",
      "org.apache.commons.graph.visit.DefaultVisitSourceSelector",
      "org.apache.commons.graph.connectivity.DefaultConnectivityBuilder",
      "org.apache.commons.graph.export.DefaultExportSelector",
      "org.apache.commons.graph.shortestpath.DefaultWeightedEdgesSelector"
    );
  }
}
