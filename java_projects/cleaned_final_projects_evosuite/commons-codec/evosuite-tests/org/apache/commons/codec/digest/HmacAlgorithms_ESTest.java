
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


package org.apache.commons.codec.digest;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.codec.digest.HmacAlgorithms;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class HmacAlgorithms_ESTest extends HmacAlgorithms_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      HmacAlgorithms[] hmacAlgorithmsArray0 = HmacAlgorithms.values();
      assertEquals(6, hmacAlgorithmsArray0.length);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      HmacAlgorithms hmacAlgorithms0 = HmacAlgorithms.valueOf("HMAC_SHA_512");
      assertEquals("HmacSHA512", hmacAlgorithms0.toString());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      HmacAlgorithms hmacAlgorithms0 = HmacAlgorithms.HMAC_SHA_224;
      String string0 = hmacAlgorithms0.toString();
      assertEquals("HmacSHA224", string0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      HmacAlgorithms hmacAlgorithms0 = HmacAlgorithms.HMAC_SHA_1;
      String string0 = hmacAlgorithms0.getName();
      assertEquals("HmacSHA1", string0);
  }
}
