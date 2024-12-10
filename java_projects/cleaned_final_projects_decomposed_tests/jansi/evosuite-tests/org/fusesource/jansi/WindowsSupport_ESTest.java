/*
 * This file was automatically generated by EvoSuite
 * Fri Jul 12 04:21:39 GMT 2024
 */

package org.fusesource.jansi;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.fusesource.jansi.WindowsSupport;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class WindowsSupport_ESTest extends WindowsSupport_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      // Undeclared exception!
      try { 
        WindowsSupport.getErrorMessage(877);
        fail("Expecting exception: UnsatisfiedLinkError");
      
      } catch(UnsatisfiedLinkError e) {
         //
         // 'int org.fusesource.jansi.internal.Kernel32.FormatMessageW(int, long, int, int, byte[], int, long[])'
         //
         verifyException("org.fusesource.jansi.internal.Kernel32", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      // Undeclared exception!
      try { 
        WindowsSupport.getLastErrorMessage();
        fail("Expecting exception: UnsatisfiedLinkError");
      
      } catch(UnsatisfiedLinkError e) {
         //
         // 'int org.fusesource.jansi.internal.Kernel32.GetLastError()'
         //
         verifyException("org.fusesource.jansi.internal.Kernel32", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      WindowsSupport windowsSupport0 = new WindowsSupport();
  }
}