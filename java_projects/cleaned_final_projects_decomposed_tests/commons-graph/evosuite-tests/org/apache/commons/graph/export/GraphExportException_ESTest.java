/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:19:34 GMT 2024
 */

package org.apache.commons.graph.export;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.UnknownFormatConversionException;
import org.apache.commons.graph.export.GraphExportException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.lang.MockThrowable;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class GraphExportException_ESTest extends GraphExportException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable();
      Object[] objectArray0 = new Object[7];
      GraphExportException graphExportException0 = null;
      try {
        graphExportException0 = new GraphExportException(mockThrowable0, "4r&}Oo+%1#[Z", objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = '1'
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable("");
      Object[] objectArray0 = new Object[1];
      GraphExportException graphExportException0 = null;
      try {
        graphExportException0 = new GraphExportException(mockThrowable0, (String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      MockThrowable mockThrowable0 = new MockThrowable("");
      Object[] objectArray0 = new Object[1];
      GraphExportException graphExportException0 = new GraphExportException(mockThrowable0, "", objectArray0);
  }
}