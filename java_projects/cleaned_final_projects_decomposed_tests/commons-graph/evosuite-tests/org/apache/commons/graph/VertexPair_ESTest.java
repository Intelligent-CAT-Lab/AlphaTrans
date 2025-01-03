/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:15:31 GMT 2024
 */

package org.apache.commons.graph;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.VertexPair;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class VertexPair_ESTest extends VertexPair_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Integer integer0 = new Integer((-1291));
      Object object0 = new Object();
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(integer0, object0);
      Object object1 = vertexPair0.getTail();
      assertSame(object1, object0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Integer integer0 = new Integer((-1291));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      Object object0 = new Object();
      VertexPair<Object> vertexPair1 = new VertexPair<Object>(integer0, object0);
      VertexPair<VertexPair<Integer>> vertexPair2 = new VertexPair<VertexPair<Integer>>(vertexPair0, vertexPair0);
      Object object1 = vertexPair2.getHead();
      boolean boolean0 = vertexPair1.equals(object1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object object0 = new Object();
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(object0, object0);
      VertexPair<VertexPair<Object>> vertexPair1 = new VertexPair<VertexPair<Object>>(vertexPair0, vertexPair0);
      boolean boolean0 = vertexPair1.equals(vertexPair0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(integer0, integer0);
      VertexPair<Integer> vertexPair1 = new VertexPair<Integer>(integer0, integer0);
      boolean boolean0 = vertexPair0.equals(vertexPair1);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Integer integer0 = new Integer((-1291));
      VertexPair<Integer> vertexPair0 = new VertexPair<Integer>(integer0, integer0);
      boolean boolean0 = vertexPair0.equals((Object) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Integer integer0 = new Integer((-997));
      Object object0 = new Object();
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(integer0, object0);
      boolean boolean0 = vertexPair0.equals(vertexPair0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(integer0, integer0);
      boolean boolean0 = vertexPair0.equals(integer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Integer integer0 = new Integer((-1));
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(integer0, integer0);
      vertexPair0.hashCode();
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      Object object0 = new Object();
      VertexPair<Object> vertexPair0 = new VertexPair<Object>(object0, object0);
      String string0 = vertexPair0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      VertexPair<Object> vertexPair0 = null;
      try {
        vertexPair0 = new VertexPair<Object>((Object) null, (Object) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Impossible to construct a Vertex with a null head
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }
}
