
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


package org.joda.convert;

import org.junit.Test;
import static org.junit.Assert.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.StringConverter;
import org.joda.convert.TypeTokenStringConverter;
import org.joda.convert.TypedAdapter;
import org.joda.convert.TypedStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TypedAdapter_ESTest extends TypedAdapter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Class<TypeTokenStringConverter> class0 = TypeTokenStringConverter.class;
      TypedStringConverter<TypeTokenStringConverter> typedStringConverter0 = TypedAdapter.adapt(class0, (StringConverter<TypeTokenStringConverter>) null);
      TypedStringConverter<TypeTokenStringConverter> typedStringConverter1 = TypedAdapter.adapt(class0, (StringConverter<TypeTokenStringConverter>) typedStringConverter0);
      assertSame(typedStringConverter1, typedStringConverter0);
  }
}
