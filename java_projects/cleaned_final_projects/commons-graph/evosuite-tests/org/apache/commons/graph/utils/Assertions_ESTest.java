/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 15:13:58 GMT 2024
 */

package org.apache.commons.graph.utils;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.FormatFlagsConversionMismatchException;
import java.util.IllegalFormatConversionException;
import java.util.MissingFormatArgumentException;
import java.util.MissingFormatWidthException;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.utils.Assertions;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class Assertions_ESTest extends Assertions_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Object[] objectArray0 = new Object[6];
      // Undeclared exception!
      try { 
        Assertions.checkState(false, "Q%IR", objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = 'I'
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Object[] objectArray0 = new Object[5];
      // Undeclared exception!
      try { 
        Assertions.checkState(false, (String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, "%5Qwl<]@/fAtZ\"", (Object[]) null);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = 'Q'
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Object[] objectArray0 = new Object[7];
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, "t6$|%<0eu", objectArray0);
        fail("Expecting exception: MissingFormatWidthException");
      
      } catch(MissingFormatWidthException e) {
         //
         // %0<e
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Object[] objectArray0 = new Object[7];
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, "%<2bPu?oxXw5@,+", objectArray0);
        fail("Expecting exception: MissingFormatArgumentException");
      
      } catch(MissingFormatArgumentException e) {
         //
         // Format specifier '%<2b'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Object object0 = new Object();
      Object[] objectArray0 = new Object[1];
      objectArray0[0] = object0;
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Integer) null, "k>eVq>Y4-S/Po%ddY", objectArray0);
        fail("Expecting exception: IllegalFormatConversionException");
      
      } catch(IllegalFormatConversionException e) {
         //
         // d != java.lang.Object
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Object[] objectArray0 = new Object[17];
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, "?T1GF0]641W%,b", objectArray0);
        fail("Expecting exception: FormatFlagsConversionMismatchException");
      
      } catch(FormatFlagsConversionMismatchException e) {
         //
         // Conversion = b, Flags = ,
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, (String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Object[] objectArray0 = new Object[0];
      // Undeclared exception!
      try { 
        Assertions.checkArgument(false, "%x", objectArray0);
        fail("Expecting exception: MissingFormatArgumentException");
      
      } catch(MissingFormatArgumentException e) {
         //
         // Format specifier '%x'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Object[] objectArray0 = new Object[2];
      objectArray0[0] = (Object) ":8}79/vFN%e2";
      // Undeclared exception!
      try { 
        Assertions.checkArgument(false, ":8}79/vFN%e2", objectArray0);
        fail("Expecting exception: IllegalFormatConversionException");
      
      } catch(IllegalFormatConversionException e) {
         //
         // e != java.lang.String
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Object[] objectArray0 = new Object[5];
      // Undeclared exception!
      try { 
        Assertions.checkArgument(false, (String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        Assertions.checkArgument(false, "=sDq\"ZS", objectArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // =sDq\"ZS
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Object[] objectArray0 = new Object[2];
      // Undeclared exception!
      try { 
        Assertions.checkState(false, "@ErA-$n|]mRqwH", objectArray0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // @ErA-$n|]mRqwH
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Object[] objectArray0 = new Object[1];
      Assertions.checkState(true, "org.apache.commons.graph.utils.Assertions", objectArray0);
      assertEquals(1, objectArray0.length);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        Assertions.checkNotNull((Object) null, ",NIUv", objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // ,NIUv
         //
         verifyException("org.apache.commons.graph.utils.Assertions", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Object object0 = new Object();
      Object[] objectArray0 = new Object[1];
      Object object1 = Assertions.checkNotNull(object0, "org.apache.commons.graph.utils.Assertions", objectArray0);
      assertSame(object1, object0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        Assertions.checkArgument(false, "*?xPHo4x$%VZId", objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = 'V'
         //
         verifyException("java.util.Formatter$FormatSpecifier", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Object[] objectArray0 = new Object[2];
      Assertions.checkArgument(true, ">F_N7VUY{+^Y_?e", objectArray0);
      assertEquals(2, objectArray0.length);
  }
}
