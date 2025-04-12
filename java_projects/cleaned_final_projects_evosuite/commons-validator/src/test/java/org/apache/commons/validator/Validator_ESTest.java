

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



package org.apache.commons.validator;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.validator.Validator;
import org.apache.commons.validator.ValidatorResources;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Validator_ESTest extends Validator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Validator validator0 = null;
      try {
        validator0 = new Validator((-438), (ValidatorResources) null, "),v,&x3rV[Vrdw", "),v,&x3rV[Vrdw");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Resources cannot be null.
         //
         verifyException("org.apache.commons.validator.Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Validator validator0 = null;
      try {
        validator0 = new Validator(0, (ValidatorResources) null, "j//EJ", "j//EJ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Resources cannot be null.
         //
         verifyException("org.apache.commons.validator.Validator", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      // Undeclared exception!
      try { 
        Validator.Validator2((ValidatorResources) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Resources cannot be null.
         //
         verifyException("org.apache.commons.validator.Validator", e);
      }
  }
}
