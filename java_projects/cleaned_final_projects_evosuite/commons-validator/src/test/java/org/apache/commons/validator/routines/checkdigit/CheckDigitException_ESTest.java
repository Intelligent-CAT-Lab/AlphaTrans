

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



package org.apache.commons.validator.routines.checkdigit;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.validator.routines.checkdigit.CheckDigitException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CheckDigitException_ESTest extends CheckDigitException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CheckDigitException checkDigitException0 = CheckDigitException.CheckDigitException2();
      assertNotNull(checkDigitException0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      CheckDigitException checkDigitException0 = CheckDigitException.CheckDigitException1("");
      CheckDigitException checkDigitException1 = new CheckDigitException("2fdA33pTvI61m6L-", checkDigitException0);
      assertFalse(checkDigitException1.equals((Object)checkDigitException0));
  }
}
