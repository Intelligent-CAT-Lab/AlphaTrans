
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


package org.apache.commons.graph.scc;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedHashSet;
import java.util.Set;
import org.apache.commons.graph.DirectedGraph;
import org.apache.commons.graph.model.DirectedMutableGraph;
import org.apache.commons.graph.model.RevertedGraph;
import org.apache.commons.graph.scc.DefaultSccAlgorithmSelector;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultSccAlgorithmSelector_ESTest extends DefaultSccAlgorithmSelector_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      Set<Set<Integer>> set0 = defaultSccAlgorithmSelector0.applyingTarjan();
      assertTrue(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1473));
      directedMutableGraph0.addVertex(integer0);
      DefaultSccAlgorithmSelector<Integer, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, Integer>(directedMutableGraph0);
      Set<Set<Integer>> set0 = defaultSccAlgorithmSelector0.applyingTarjan();
      assertFalse(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      RevertedGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> revertedGraph0 = new RevertedGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>(directedMutableGraph0);
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>>(revertedGraph0);
      Set<LinkedHashSet<Integer>> set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0);
      assertFalse(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DirectedMutableGraph<Integer, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<Integer, LinkedHashSet<Integer>>();
      DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>>(directedMutableGraph0);
      Set<Set<Integer>> set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir0();
      assertEquals(0, set0.size());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>();
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      directedMutableGraph0.addVertex(linkedHashSet0);
      RevertedGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>> revertedGraph0 = new RevertedGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>(directedMutableGraph0);
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>>(revertedGraph0);
      Set<Set<LinkedHashSet<Integer>>> set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir0();
      assertEquals(1, set0.size());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      Integer integer0 = new Integer((-1));
      directedMutableGraph0.addVertex(integer0);
      DefaultSccAlgorithmSelector<Integer, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, Integer>(directedMutableGraph0);
      Set<Set<Integer>> set0 = defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow();
      assertFalse(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer>(directedMutableGraph0);
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingKosarajuSharir1((LinkedHashSet<Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Kosaraju Sharir algorithm cannot be calculated without expressing the source vertex
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DirectedMutableGraph<LinkedHashSet<Integer>, Integer> directedMutableGraph0 = new DirectedMutableGraph<LinkedHashSet<Integer>, Integer>();
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer>(directedMutableGraph0);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Vertex [] does not exist in the Graph
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer>((DirectedGraph<LinkedHashSet<Integer>, Integer>) null);
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DirectedMutableGraph<Integer, Integer> directedMutableGraph0 = new DirectedMutableGraph<Integer, Integer>();
      DefaultSccAlgorithmSelector<Integer, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, Integer>(directedMutableGraph0);
      Set<Set<Integer>> set0 = defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow();
      assertTrue(set0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, LinkedHashSet<Integer>>((DirectedGraph<LinkedHashSet<Integer>, LinkedHashSet<Integer>>) null);
      LinkedHashSet<Integer> linkedHashSet0 = new LinkedHashSet<Integer>();
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<LinkedHashSet<Integer>, Integer>((DirectedGraph<LinkedHashSet<Integer>, Integer>) null);
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingKosarajuSharir0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>> defaultSccAlgorithmSelector0 = new DefaultSccAlgorithmSelector<Integer, LinkedHashSet<Integer>>((DirectedGraph<Integer, LinkedHashSet<Integer>>) null);
      // Undeclared exception!
      try { 
        defaultSccAlgorithmSelector0.applyingTarjan();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.scc.TarjanAlgorithm", e);
      }
  }
}
