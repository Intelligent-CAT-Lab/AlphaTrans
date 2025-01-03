/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 15:11:43 GMT 2024
 */

package org.apache.commons.graph;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.GraphException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class GraphException_ESTest extends GraphException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable((String) null, (Throwable) null);
      Throwable[] throwableArray0 = mockThrowable0.getSuppressed();
      GraphException graphException0 = new GraphException("", mockThrowable0, throwableArray0);
      GraphException graphException1 = null;
      try {
        graphException1 = new GraphException("%?A?(S~uPlt", graphException0, throwableArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = '?'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable("org.apache.commons.graph.GraphException");
      Object[] objectArray0 = new Object[1];
      GraphException graphException0 = new GraphException("org.apache.commons.graph.GraphException", mockThrowable0, objectArray0);
      GraphException graphException1 = null;
      try {
        graphException1 = new GraphException((String) null, graphException0, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object[] objectArray0 = new Object[8];
      GraphException graphException0 = new GraphException("3yD", (Throwable) null, objectArray0);
      GraphException graphException1 = new GraphException("\"WaDD1~$b_0", graphException0, objectArray0);
      assertFalse(graphException1.equals((Object)graphException0));
  }
}
