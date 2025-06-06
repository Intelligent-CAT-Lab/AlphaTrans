/*
 * This file was automatically generated by EvoSuite
 * Fri Jul 12 04:27:16 GMT 2024
 */

package org.apache.commons.exec.util;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.exec.util.DebugUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class DebugUtils_ESTest extends DebugUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      boolean boolean0 = DebugUtils.isLenientEnabled();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      boolean boolean0 = DebugUtils.isDebugEnabled();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      DebugUtils.handleException("org.apache.commons.exec.util.DebugUtils", (Exception) null);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DebugUtils debugUtils0 = new DebugUtils();
      assertTrue(debugUtils0.isLenientEnabled());
  }
}
