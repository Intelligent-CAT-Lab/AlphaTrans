/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 15:16:12 GMT 2024
 */

package org.apache.commons.graph.shortestpath;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.shortestpath.ShortestDistances;
import org.apache.commons.graph.weight.OrderedMonoid;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class ShortestDistances_ESTest extends ShortestDistances_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer((-1099));
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      shortestDistances0.setWeight(integer1, integer1);
      shortestDistances0.setWeight(integer0, integer1);
      int int0 = shortestDistances0.compare(integer1, integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer((-1099));
      shortestDistances0.setWeight(integer0, integer0);
      boolean boolean0 = shortestDistances0.alreadyVisited(integer0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer((-1099));
      Integer integer1 = shortestDistances0.getWeight(integer0);
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer(0);
      shortestDistances0.setWeight(integer0, integer0);
      Integer integer1 = new Integer(1065);
      int int0 = shortestDistances0.compare(integer0, integer1);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer(0);
      shortestDistances0.setWeight(integer0, integer0);
      Integer integer1 = new Integer(1065);
      int int0 = shortestDistances0.compare(integer1, integer0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer(0);
      int int0 = shortestDistances0.compare(integer0, integer0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>(integerWeightBaseOperations0);
      Integer integer0 = new Integer(0);
      boolean boolean0 = shortestDistances0.alreadyVisited(integer0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      ShortestDistances<Integer, Integer> shortestDistances0 = new ShortestDistances<Integer, Integer>((OrderedMonoid<Integer>) null);
      shortestDistances0.setWeight((Integer) null, (Integer) null);
      // Undeclared exception!
      try { 
        shortestDistances0.compare((Integer) null, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.shortestpath.ShortestDistances", e);
      }
  }
}