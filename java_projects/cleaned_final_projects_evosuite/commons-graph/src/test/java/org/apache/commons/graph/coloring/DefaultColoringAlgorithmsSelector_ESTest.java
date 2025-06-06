
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


package org.apache.commons.graph.coloring;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedHashSet;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.UndirectedGraph;
import org.apache.commons.graph.coloring.ColoredVertices;
import org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector;
import org.apache.commons.graph.model.MutableSpanningTree;
import org.apache.commons.graph.model.UndirectedMutableGraph;
import org.apache.commons.graph.weight.Monoid;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultColoringAlgorithmsSelector_ESTest extends DefaultColoringAlgorithmsSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer0 = new Integer(2238);
      undirectedMutableGraph0.addVertex(integer0);
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      Integer integer1 = new Integer(2238);
      undirectedMutableGraph0.addEdge(integer0, coloredVertices0, integer1);
      linkedHashSet0.add(integer0);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      Integer integer0 = new Integer((-212));
      undirectedMutableGraph0.addVertex(integer0);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer1 = new Integer((-1246));
      linkedHashSet0.add(integer1);
      Integer integer2 = new Integer((-3954));
      undirectedMutableGraph0.addVertex(integer2);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingGreedyAlgorithm();
      assertEquals(1, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Monoid<ColoredVertices<Integer, Integer>> monoid0 = (Monoid<ColoredVertices<Integer, Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Integer, ColoredVertices<Integer, Integer>> mapper0 = (Mapper<Integer, ColoredVertices<Integer, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Integer, Integer, ColoredVertices<Integer, Integer>> mutableSpanningTree0 = new MutableSpanningTree<Integer, Integer, ColoredVertices<Integer, Integer>>(monoid0, mapper0);
      DefaultColoringAlgorithmsSelector<Integer, Integer, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, Integer, Integer>(mutableSpanningTree0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      ColoredVertices<Integer, Integer> coloredVertices1 = defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(coloredVertices0);
      assertSame(coloredVertices1, coloredVertices0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, Integer, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, Integer, Integer>((UndirectedGraph<Integer, Integer>) null, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingGreedyAlgorithm();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LinkedHashSet<ColoredVertices<Integer, Integer>> linkedHashSet0 = new LinkedHashSet<ColoredVertices<Integer, Integer>>();
      DefaultColoringAlgorithmsSelector<Integer, Integer, ColoredVertices<Integer, Integer>> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, Integer, ColoredVertices<Integer, Integer>>((UndirectedGraph<Integer, Integer>) null, linkedHashSet0);
      ColoredVertices<Integer, ColoredVertices<Integer, Integer>> coloredVertices0 = new ColoredVertices<Integer, ColoredVertices<Integer, Integer>>();
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(coloredVertices0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1((ColoredVertices<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // PartialColoredVertex must be not null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Monoid<Object> monoid0 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Integer, Object> mapper0 = (Mapper<Integer, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      MutableSpanningTree<Object, Integer, Object> mutableSpanningTree0 = new MutableSpanningTree<Object, Integer, Object>(monoid0, mapper0);
      LinkedHashSet<Comparable<Object>> linkedHashSet0 = new LinkedHashSet<Comparable<Object>>();
      mutableSpanningTree0.addVertex(linkedHashSet0);
      Comparable<Object> comparable0 = (Comparable<Object>) mock(Comparable.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(comparable0).toString();
      linkedHashSet0.add(comparable0);
      DefaultColoringAlgorithmsSelector<Object, Integer, Comparable<Object>> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Object, Integer, Comparable<Object>>(mutableSpanningTree0, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.BaseGraph", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, Integer, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, Integer, Integer>((UndirectedGraph<Integer, Integer>) null, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      Integer integer0 = new Integer((-212));
      undirectedMutableGraph0.addVertex(integer0);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(coloredVertices0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      Integer integer0 = new Integer(340);
      undirectedMutableGraph0.addVertex(integer0);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer1 = new Integer(1);
      undirectedMutableGraph0.addVertex(integer1);
      ColoredVertices<Integer, Integer> coloredVertices0 = new ColoredVertices<Integer, Integer>();
      undirectedMutableGraph0.addEdge(integer0, coloredVertices0, integer1);
      linkedHashSet0.add(integer1);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer0 = new Integer((-1862));
      linkedHashSet0.add((Integer) null);
      undirectedMutableGraph0.addVertex(integer0);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
      assertEquals(1, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer0 = new Integer((-1862));
      undirectedMutableGraph0.addVertex(integer0);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      // Undeclared exception!
      try { 
        defaultColoringAlgorithmsSelector0.applyingGreedyAlgorithm();
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingGreedyAlgorithm();
      assertEquals(0, coloredVertices0.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      Integer integer0 = new Integer((-1862));
      linkedHashSet0.add(integer0);
      undirectedMutableGraph0.addVertex(integer0);
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
      ColoredVertices<Integer, Integer> coloredVertices1 = defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(coloredVertices0);
      assertEquals(1, coloredVertices1.getRequiredColors());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>> undirectedMutableGraph0 = new UndirectedMutableGraph<Integer, ColoredVertices<Integer, Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer> defaultColoringAlgorithmsSelector0 = new DefaultColoringAlgorithmsSelector<Integer, ColoredVertices<Integer, Integer>, Integer>(undirectedMutableGraph0, linkedHashSet0);
      ColoredVertices<Integer, Integer> coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0();
      assertEquals(0, coloredVertices0.getRequiredColors());
  }
}
