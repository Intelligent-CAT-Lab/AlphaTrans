
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


package org.apache.commons.graph.export;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.util.HashMap;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.export.DotExporter;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.InMemoryPath;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DotExporter_ESTest extends DotExporter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(mutableSpanningTree0, "jAwAG4%I*Sh@6E;y1>\"");
      Integer integer0 = new Integer(31);
      Integer integer1 = new Integer(0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      try { 
        dotExporter0.edge(integer0, integer1, integer0, hashMap0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>();
      DotExporter<Integer, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<Integer, RevertedGraph<Integer, Integer>>(undirectedMutableGraph0, "36.");
      Integer integer0 = new Integer(1104);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      try { 
        dotExporter0.edge(revertedGraph0, integer0, integer0, hashMap0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<RevertedGraph<Integer, Integer>, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<RevertedGraph<Integer, Integer>, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DotExporter<RevertedGraph<Integer, Integer>, Integer> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, Integer>(mutableSpanningTree0, ";-");
      MockFile mockFile0 = new MockFile("  %s", "");
      MockPrintStream mockPrintStream0 = new MockPrintStream(mockFile0);
      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(mockPrintStream0, 2);
      dotExporter0.to1(bufferedOutputStream0);
      dotExporter0.startSerialization();
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(directedMutableGraph0, "I9N:)e?b~jm5tP");
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
      dotExporter0.to1(byteArrayOutputStream0);
      dotExporter0.startGraph("");
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer(2);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(inMemoryWeightedPath0, "");
      MockFile mockFile0 = new MockFile("ZQ[M;^odH", "y@tztKj[._7kz");
      dotExporter0.to0(mockFile0);
      dotExporter0.endGraph();
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(inMemoryPath0, "36.");
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(byteArrayOutputStream0);
      dotExporter0.to1(bufferedOutputStream0);
      dotExporter0.comment("^yVN]sQ$/");
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, Integer> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, Integer>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, Integer> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, Integer>(inMemoryPath0, "I9N:)e?b~jm5tP");
      dotExporter0.endSerialization();
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(undirectedMutableGraph0, "org.apache.commons.graph.model.RevertedGraph");
      try { 
        dotExporter0.startSerialization();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.Writer", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>();
      DotExporter<Integer, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<Integer, RevertedGraph<Integer, Integer>>(undirectedMutableGraph0, "s{DqL VW");
      try { 
        dotExporter0.startGraph("org.apache.commons.graph.model.BaseGraph");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      UndirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<RevertedGraph<Integer, Integer>, Integer>();
      DotExporter<RevertedGraph<Integer, Integer>, Integer> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, Integer>(undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath");
      try { 
        dotExporter0.endGraph();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UndirectedMutableGraph<Integer, Integer> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, Integer>();
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(undirectedMutableGraph0, "");
      try { 
        dotExporter0.comment("");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DotExporter<Integer, String> dotExporter0 = null;
      try {
        dotExporter0 = new DotExporter<Integer, String>((Graph<Integer, String>) null, "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      UndirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath");
      PipedInputStream pipedInputStream0 = new PipedInputStream(988);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
      MockPrintStream mockPrintStream0 = new MockPrintStream(pipedOutputStream0, true);
      DataOutputStream dataOutputStream0 = new DataOutputStream(mockPrintStream0);
      dotExporter0.to1(dataOutputStream0);
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      dotExporter0.edge(revertedGraph0, revertedGraph0, revertedGraph0, hashMap0);
      assertTrue(hashMap0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(inMemoryPath0, "36.");
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream(byteArrayOutputStream0);
      dotExporter0.to1(bufferedOutputStream0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      hashMap0.put("36.", revertedGraph0);
      dotExporter0.vertex(revertedGraph0, hashMap0);
      assertFalse(hashMap0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, RevertedGraph<Integer, Integer>>();
      Integer integer0 = new Integer((-2));
      undirectedMutableGraph0.addVertex(integer0);
      DotExporter<Integer, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<Integer, RevertedGraph<Integer, Integer>>(undirectedMutableGraph0, "L");
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<RevertedGraph<Integer, Integer>, Integer, Integer> mutableSpanningTree0 = new MutableSpanningTree<RevertedGraph<Integer, Integer>, Integer, Integer>(integerWeightBaseOperations0, mapper0);
      DotExporter<RevertedGraph<Integer, Integer>, Integer> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, Integer>(mutableSpanningTree0, "");
      Class<Integer> class0 = Integer.class;
      dotExporter0.enlistEdgesProperty("", class0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(inMemoryPath0, "36.");
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      try { 
        dotExporter0.vertex(revertedGraph0, hashMap0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.export.DotExporter", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      DotExporter<Integer, Integer> dotExporter0 = new DotExporter<Integer, Integer>(revertedGraph0, "");
      Class<Integer> class0 = Integer.class;
      dotExporter0.enlistVerticesProperty("", class0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DirectedMutableGraph<Integer, String> directedMutableGraph0 = new DirectedMutableGraph<Integer, String>();
      RevertedGraph<Integer, String> revertedGraph0 = new RevertedGraph<Integer, String>(directedMutableGraph0);
      Monoid<RevertedGraph<Integer, Integer>> monoid0 = (Monoid<RevertedGraph<Integer, Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Integer, RevertedGraph<Integer, Integer>> mapper0 = (Mapper<Integer, RevertedGraph<Integer, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<RevertedGraph<Integer, String>, Integer, RevertedGraph<Integer, Integer>> inMemoryWeightedPath0 = new InMemoryWeightedPath<RevertedGraph<Integer, String>, Integer, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0, monoid0, mapper0);
      DotExporter<RevertedGraph<Integer, String>, Integer> dotExporter0 = new DotExporter<RevertedGraph<Integer, String>, Integer>(inMemoryWeightedPath0, "weight");
      Mapper<RevertedGraph<Integer, String>, String> mapper1 = (Mapper<RevertedGraph<Integer, String>, String>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DotExporter<RevertedGraph<Integer, String>, Integer> dotExporter1 = dotExporter0.withVertexLabels(mapper1);
      assertSame(dotExporter0, dotExporter1);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      UndirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>();
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(undirectedMutableGraph0, "org.apache.commons.graph.model.InMemoryPath");
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter1 = dotExporter0.withEdgeLabels((Mapper<RevertedGraph<Integer, Integer>, String>) null);
      assertSame(dotExporter1, dotExporter0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(inMemoryPath0, "s!V");
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      dotExporter0.to1(byteArrayOutputStream0);
      HashMap<String, Object> hashMap0 = new HashMap<String, Object>();
      hashMap0.put("s!V", "s!V");
      hashMap0.put("%s %s {%n", "s!V");
      dotExporter0.vertex(revertedGraph0, hashMap0);
      assertFalse(hashMap0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      RevertedGraph<Integer, Integer> revertedGraph0 = new RevertedGraph<Integer, Integer>(directedMutableGraph0);
      InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> inMemoryPath0 = new InMemoryPath<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(revertedGraph0, revertedGraph0);
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter0 = new DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>>(inMemoryPath0, "36.");
      Mapper<RevertedGraph<Integer, Integer>, Integer> mapper0 = (Mapper<RevertedGraph<Integer, Integer>, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DotExporter<RevertedGraph<Integer, Integer>, RevertedGraph<Integer, Integer>> dotExporter1 = dotExporter0.withEdgeWeights(mapper0);
      assertSame(dotExporter1, dotExporter0);
  }
}
