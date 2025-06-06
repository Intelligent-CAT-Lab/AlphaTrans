
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


package org.apache.commons.graph.model;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.Mapper;
import org.apache.commons.graph.model.InMemoryWeightedPath;
import org.apache.commons.graph.weight.Monoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class InMemoryWeightedPath_ESTest extends InMemoryWeightedPath_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer((-1463));
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(anyInt());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer1, integer1, integerWeightBaseOperations0, mapper0);
      inMemoryWeightedPath0.addConnectionInTail(integer1, integer0, integer1);
      assertEquals(2, inMemoryWeightedPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Integer integer0 = new Integer(1264);
      Integer integer1 = Integer.getInteger("", 1264);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<InMemoryWeightedPath<Integer, Integer, Integer>, Integer> mapper0 = (Mapper<InMemoryWeightedPath<Integer, Integer, Integer>, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(mapper0).map(any(org.apache.commons.graph.model.InMemoryWeightedPath.class));
      InMemoryWeightedPath<Integer, InMemoryWeightedPath<Integer, Integer, Integer>, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, InMemoryWeightedPath<Integer, Integer, Integer>, Integer>(integer0, integer1, integerWeightBaseOperations0, mapper0);
      Mapper<Integer, Integer> mapper1 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath1 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer1, integer0, integerWeightBaseOperations0, mapper1);
      inMemoryWeightedPath0.addConnectionInHead(integer0, inMemoryWeightedPath1, integer1);
      assertEquals(2, inMemoryWeightedPath0.getOrder());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Integer integer0 = new Integer(31);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Integer, Integer> mapper0 = (Mapper<Integer, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper0);
      Monoid<InMemoryWeightedPath<Integer, Integer, Integer>> monoid0 = (Monoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn(inMemoryWeightedPath0).when(monoid0).identity();
      Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>> mapper1 = (Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> inMemoryWeightedPath1 = new InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(integer0, integer0, monoid0, mapper1);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath2 = inMemoryWeightedPath1.getWeight();
      assertEquals(0, inMemoryWeightedPath2.getSize());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Object object0 = new Object();
      Monoid<Comparable<Integer>> monoid0 = (Monoid<Comparable<Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Object, Comparable<Integer>> mapper0 = (Mapper<Object, Comparable<Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Object, Object, Comparable<Integer>> inMemoryWeightedPath0 = new InMemoryWeightedPath<Object, Object, Comparable<Integer>>(object0, object0, monoid0, mapper0);
      Iterable<Object> iterable0 = inMemoryWeightedPath0.getVertices0();
      Integer integer0 = new Integer(1);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Mapper<Object, Integer> mapper1 = (Mapper<Object, Integer>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Object, Integer> inMemoryWeightedPath1 = new InMemoryWeightedPath<Integer, Object, Integer>(integer0, integer0, integerWeightBaseOperations0, mapper1);
      // Undeclared exception!
      try { 
        inMemoryWeightedPath0.addConnectionInTail(iterable0, object0, inMemoryWeightedPath1);
        fail("Expecting exception: StackOverflowError");
      
      } catch(StackOverflowError e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Integer integer0 = new Integer(8);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        inMemoryWeightedPath0.addConnectionInTail(integer0, integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null tail
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Integer integer0 = new Integer(8);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        inMemoryWeightedPath0.addConnectionInHead((Integer) null, integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null head
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Integer integer0 = new Integer((-27));
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = null;
      try {
        inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, (Monoid<Integer>) null, (Mapper<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.InMemoryWeightedPath", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Integer integer0 = new Integer(0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = null;
      try {
        inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>((Integer) null, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Path source cannot be null
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Integer integer0 = new Integer(31);
      Monoid<InMemoryWeightedPath<Integer, Integer, Integer>> monoid0 = (Monoid<InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>> mapper0 = (Mapper<Integer, InMemoryWeightedPath<Integer, Integer, Integer>>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, InMemoryWeightedPath<Integer, Integer, Integer>>(integer0, integer0, monoid0, mapper0);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath1 = inMemoryWeightedPath0.getWeight();
      assertNull(inMemoryWeightedPath1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Comparable<Object> comparable0 = (Comparable<Object>) mock(Comparable.class, new ViolatedAssumptionAnswer());
      Monoid<Object> monoid0 = (Monoid<Object>) mock(Monoid.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(monoid0).identity();
      Mapper<Comparable<Object>, Object> mapper0 = (Mapper<Comparable<Object>, Object>) mock(Mapper.class, new ViolatedAssumptionAnswer());
      InMemoryWeightedPath<Comparable<Object>, Comparable<Object>, Object> inMemoryWeightedPath0 = new InMemoryWeightedPath<Comparable<Object>, Comparable<Object>, Object>(comparable0, comparable0, monoid0, mapper0);
      inMemoryWeightedPath0.hashCode();
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Integer integer0 = new Integer(8);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      inMemoryWeightedPath0.hashCode();
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(31);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      boolean boolean0 = inMemoryWeightedPath0.equals(integerWeightBaseOperations0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Integer integer0 = new Integer(0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      boolean boolean0 = inMemoryWeightedPath0.equals(inMemoryWeightedPath0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Integer integer0 = new Integer((-1764));
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        inMemoryWeightedPath0.addConnectionInHead(integer0, integer0, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.InMemoryWeightedPath", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Integer integer0 = new Integer((-1764));
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Comparable<Integer>, Object, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Comparable<Integer>, Object, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Object, Integer>) null);
      String string0 = inMemoryWeightedPath0.toString();
      assertEquals("InMemoryPath [weigth=0, vertices=[], edges=[]]", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Integer integer0 = Integer.valueOf(8);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      // Undeclared exception!
      try { 
        inMemoryWeightedPath0.addConnectionInTail(integer0, integer0, integer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.model.InMemoryWeightedPath", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Integer integer0 = new Integer(0);
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath0 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      InMemoryWeightedPath<Integer, Integer, Integer> inMemoryWeightedPath1 = new InMemoryWeightedPath<Integer, Integer, Integer>(integer0, integer0, integerWeightBaseOperations0, (Mapper<Integer, Integer>) null);
      boolean boolean0 = inMemoryWeightedPath0.equals(inMemoryWeightedPath1);
      assertTrue(boolean0);
  }
}
