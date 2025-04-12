
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


package org.apache.commons.graph.flow;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.LongWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultMaxFlowAlgorithmSelector_ESTest extends DefaultMaxFlowAlgorithmSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Mapper<Long, OrderedMonoid<Long>> mapper0 = (Mapper<Long, OrderedMonoid<Long>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DirectedMutableGraph<Long, Long> directedMutableGraph0 = new DirectedMutableGraph<Long, Long>();
      Long long0 = new Long(0L);
      directedMutableGraph0.addVertex(long0);
      Long long1 = Long.getLong((String) null);
      DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>>(directedMutableGraph0, mapper0, long0, long1);
      OrderedMonoid<OrderedMonoid<Long>> orderedMonoid0 = (OrderedMonoid<OrderedMonoid<Long>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      OrderedMonoid<Long> orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson(orderedMonoid0);
      assertNull(orderedMonoid1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Mapper<Long, OrderedMonoid<Long>> mapper0 = (Mapper<Long, OrderedMonoid<Long>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      DirectedMutableGraph<Long, Long> directedMutableGraph0 = new DirectedMutableGraph<Long, Long>();
      Long long0 = new Long(0L);
      directedMutableGraph0.addVertex(long0);
      Long long1 = Long.getLong((String) null);
      DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>>(directedMutableGraph0, mapper0, long0, long1);
      OrderedMonoid<OrderedMonoid<Long>> orderedMonoid0 = (OrderedMonoid<OrderedMonoid<Long>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(longWeightBaseOperations0).when(orderedMonoid0).identity();
      OrderedMonoid<Long> orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson(orderedMonoid0);
      assertSame(longWeightBaseOperations0, orderedMonoid1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Mapper<Long, OrderedMonoid<Long>> mapper0 = (Mapper<Long, OrderedMonoid<Long>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DirectedMutableGraph<Long, Long> directedMutableGraph0 = new DirectedMutableGraph<Long, Long>();
      Long long0 = new Long(0L);
      directedMutableGraph0.addVertex(long0);
      Long long1 = Long.getLong((String) null);
      DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>>(directedMutableGraph0, mapper0, long0, long1);
      OrderedMonoid<OrderedMonoid<Long>> orderedMonoid0 = (OrderedMonoid<OrderedMonoid<Long>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(orderedMonoid0).identity();
      OrderedMonoid<Long> orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp(orderedMonoid0);
      assertNull(orderedMonoid1);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Mapper<Long, OrderedMonoid<Long>> mapper0 = (Mapper<Long, OrderedMonoid<Long>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      DirectedMutableGraph<Long, Long> directedMutableGraph0 = new DirectedMutableGraph<Long, Long>();
      Long long0 = new Long(0L);
      directedMutableGraph0.addVertex(long0);
      Long long1 = Long.getLong((String) null);
      DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<Long, Long, OrderedMonoid<Long>>(directedMutableGraph0, mapper0, long0, long1);
      OrderedMonoid<OrderedMonoid<Long>> orderedMonoid0 = (OrderedMonoid<OrderedMonoid<Long>>) mock(OrderedMonoid.class, new ViolatedAssumptionAnswer());
      doReturn(longWeightBaseOperations0).when(orderedMonoid0).identity();
      OrderedMonoid<Long> orderedMonoid1 = defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp(orderedMonoid0);
      assertSame(longWeightBaseOperations0, orderedMonoid1);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      Long long0 = new Long(3014L);
      directedMutableGraph0.addEdge(longWeightBaseOperations0, long0, longWeightBaseOperations0);
      directedMutableGraph0.removeVertex(longWeightBaseOperations0);
      Mapper<Long, Long> mapper0 = (Mapper<Long, Long>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, mapper0, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      Long long0 = new Long(0L);
      directedMutableGraph0.addEdge(longWeightBaseOperations0, long0, longWeightBaseOperations0);
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector$MapperWrapper", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, (OrderedMonoid<Long>) null, (OrderedMonoid<Long>) null);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson((OrderedMonoid<Long>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Weight operations can not be null to find the max flow in the graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex org.apache.commons.graph.weight.primitive.LongWeightBaseOperations@2 does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      Long long0 = new Long(3014L);
      directedMutableGraph0.addEdge(longWeightBaseOperations0, long0, longWeightBaseOperations0);
      directedMutableGraph0.removeVertex(longWeightBaseOperations0);
      Mapper<Long, Long> mapper0 = (Mapper<Long, Long>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, mapper0, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, (OrderedMonoid<Long>) null, (OrderedMonoid<Long>) null);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp((OrderedMonoid<Long>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Weight operations can not be null to find the max flow in the graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp((OrderedMonoid<Long>) longWeightBaseOperations0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      LongWeightBaseOperations longWeightBaseOperations1 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      directedMutableGraph0.addVertex(longWeightBaseOperations1);
      Long long0 = new Long(1102L);
      directedMutableGraph0.addEdge(longWeightBaseOperations0, long0, longWeightBaseOperations1);
      Mapper<Long, Long> mapper0 = (Mapper<Long, Long>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyLong());
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, mapper0, longWeightBaseOperations1, longWeightBaseOperations1);
      // Undeclared exception!
      defaultMaxFlowAlgorithmSelector0.applyingFordFulkerson((OrderedMonoid<Long>) longWeightBaseOperations0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      directedMutableGraph0.addVertex(longWeightBaseOperations0);
      Long long0 = new Long(0L);
      directedMutableGraph0.addEdge(longWeightBaseOperations0, long0, longWeightBaseOperations0);
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector$MapperWrapper", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DirectedMutableGraph<OrderedMonoid<Long>, Long> directedMutableGraph0 = new DirectedMutableGraph<OrderedMonoid<Long>, Long>();
      LongWeightBaseOperations longWeightBaseOperations0 = new LongWeightBaseOperations();
      DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long> defaultMaxFlowAlgorithmSelector0 = new DefaultMaxFlowAlgorithmSelector<OrderedMonoid<Long>, Long, Long>(directedMutableGraph0, (Mapper<Long, Long>) null, longWeightBaseOperations0, longWeightBaseOperations0);
      // Undeclared exception!
      try { 
        defaultMaxFlowAlgorithmSelector0.applyingEdmondsKarp((OrderedMonoid<Long>) longWeightBaseOperations0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex org.apache.commons.graph.weight.primitive.LongWeightBaseOperations@2 does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
