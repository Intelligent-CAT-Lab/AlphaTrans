/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:30:31 GMT 2024
 */

package org.apache.commons.graph.weight.primitive;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class IntegerWeightBaseOperations_ESTest extends IntegerWeightBaseOperations_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer((-181));
      Integer integer1 = new Integer((-181));
      Integer integer2 = integerWeightBaseOperations0.append(integer0, integer1);
      assertEquals((-362), (int)integer2);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      assertEquals(0, (int)integer1);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(3019);
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      assertFalse(integer1.equals((Object)integer0));
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer((-181));
      Integer integer1 = integerWeightBaseOperations0.inverse(integer0);
      int int0 = integerWeightBaseOperations0.compare(integer1, integer0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(0);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      assertEquals(0, (int)integer1);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(183);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      assertEquals(366, (int)integer1);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer(2490);
      Integer integer1 = integerWeightBaseOperations0.append(integer0, (Integer) null);
      assertNull(integer1);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer((-181));
      Integer integer1 = integerWeightBaseOperations0.append(integer0, integer0);
      assertNotNull(integer1);
      
      int int0 = integerWeightBaseOperations0.compare(integer1, integer0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.append((Integer) null, (Integer) null);
      assertNull(integer0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      // Undeclared exception!
      try { 
        integerWeightBaseOperations0.inverse((Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = integerWeightBaseOperations0.identity();
      // Undeclared exception!
      try { 
        integerWeightBaseOperations0.compare(integer0, (Integer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.Integer", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegerWeightBaseOperations integerWeightBaseOperations0 = new IntegerWeightBaseOperations();
      Integer integer0 = new Integer((-84));
      int int0 = integerWeightBaseOperations0.compare(integer0, integer0);
      assertEquals(0, int0);
  }
}
