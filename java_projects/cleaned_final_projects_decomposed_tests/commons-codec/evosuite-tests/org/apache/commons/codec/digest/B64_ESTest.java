/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 15:28:35 GMT 2024
 */

package org.apache.commons.codec.digest;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Random;
import org.apache.commons.codec.digest.B64;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.util.MockRandom;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class B64_ESTest extends B64_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      B64.b64from24bit((byte) (-120), (byte) (-120), (byte) (-120), (byte) (-120), (StringBuilder) null);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockRandom mockRandom0 = new MockRandom(0);
      String string0 = B64.getRandomSalt(0, mockRandom0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      MockRandom mockRandom0 = new MockRandom(65535);
      // Undeclared exception!
      B64.getRandomSalt(65535, mockRandom0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      // Undeclared exception!
      try { 
        B64.getRandomSalt((byte)63, (Random) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.B64", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      // Undeclared exception!
      try { 
        B64.getRandomSalt((-545), (Random) null);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -545
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder();
      // Undeclared exception!
      B64.b64from24bit((byte)65, (byte)65, (byte)65, 16777215, stringBuilder0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      // Undeclared exception!
      try { 
        B64.b64from24bit((byte)63, (byte)63, (byte)63, (byte)63, (StringBuilder) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      MockRandom mockRandom0 = new MockRandom(2083);
      String string0 = B64.getRandomSalt(2083, mockRandom0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder("");
      B64.b64from24bit((byte)0, (byte)69, (byte)77, (byte)77, stringBuilder0);
      assertEquals("BJ2..........................................................................", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      B64 b64_0 = new B64();
  }
}