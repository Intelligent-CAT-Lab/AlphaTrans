
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


package org.apache.commons.codec.binary;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.OutputStream;
import java.io.PipedOutputStream;
import java.util.NoSuchElementException;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.binary.Base16OutputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Base16OutputStream_ESTest extends Base16OutputStream_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      MockPrintStream mockPrintStream0 = new MockPrintStream(outputStream0, true);
      CodecPolicy codecPolicy0 = CodecPolicy.LENIENT;
      Base16OutputStream base16OutputStream0 = new Base16OutputStream(mockPrintStream0, false, true, codecPolicy0);
      assertFalse(base16OutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Base16OutputStream base16OutputStream0 = Base16OutputStream.Base16OutputStream2((OutputStream) null, false);
      assertFalse(base16OutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Base16OutputStream base16OutputStream0 = Base16OutputStream.Base16OutputStream1((OutputStream) null, true, true);
      assertFalse(base16OutputStream0.isStrictDecoding());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base16OutputStream.Base16OutputStream3(pipedOutputStream0);
      // Undeclared exception!
      try { 
        Base16OutputStream.Base16OutputStream3(pipedOutputStream0);
       //  fail("Expecting exception: NoSuchElementException");
       // Unstable assertion
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.LinkedList", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      Base16OutputStream base16OutputStream0 = Base16OutputStream.Base16OutputStream3(pipedOutputStream0);
      // Undeclared exception!
      try { 
        Base16OutputStream.Base16OutputStream2(base16OutputStream0, false);
       //  fail("Expecting exception: NoSuchElementException");
       // Unstable assertion
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.LinkedList", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Base16OutputStream base16OutputStream0 = Base16OutputStream.Base16OutputStream3((OutputStream) null);
      // Undeclared exception!
      try { 
        Base16OutputStream.Base16OutputStream1(base16OutputStream0, false, false);
       //  fail("Expecting exception: NoSuchElementException");
       // Unstable assertion
      } catch(NoSuchElementException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.LinkedList", e);
      }
  }
}
