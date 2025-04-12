

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



package org.apache.commons.fileupload;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.fileupload.FileCountLimitExceededException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FileCountLimitExceededException_ESTest extends FileCountLimitExceededException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      FileCountLimitExceededException fileCountLimitExceededException0 = new FileCountLimitExceededException("", 0L);
      long long0 = fileCountLimitExceededException0.getLimit();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      FileCountLimitExceededException fileCountLimitExceededException0 = new FileCountLimitExceededException("", 1214L);
      long long0 = fileCountLimitExceededException0.getLimit();
      assertEquals(1214L, long0);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      FileCountLimitExceededException fileCountLimitExceededException0 = new FileCountLimitExceededException(";e%Q.", (-1598L));
      long long0 = fileCountLimitExceededException0.getLimit();
      assertEquals((-1598L), long0);
  }
}
