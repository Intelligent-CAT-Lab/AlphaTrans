
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

import org.evosuite.runtime.annotation.EvoSuiteClassExclude;
import org.junit.BeforeClass;
import org.junit.Before;
import org.junit.After;
import org.junit.AfterClass;
import org.evosuite.runtime.sandbox.Sandbox;
import org.evosuite.runtime.sandbox.Sandbox.SandboxMode;

@EvoSuiteClassExclude
public class JDKStringConverter_ESTest_scaffolding {

  @org.junit.Rule
  public org.evosuite.runtime.vnet.NonFunctionalRequirementRule nfr = new org.evosuite.runtime.vnet.NonFunctionalRequirementRule();

  private static final java.util.Properties defaultProperties = (java.util.Properties) java.lang.System.getProperties().clone(); 

  private org.evosuite.runtime.thread.ThreadStopper threadStopper =  new org.evosuite.runtime.thread.ThreadStopper (org.evosuite.runtime.thread.KillSwitchHandler.getInstance(), 3000);


  @BeforeClass
  public static void initEvoSuiteFramework() { 
    org.evosuite.runtime.RuntimeSettings.className = "org.joda.convert.JDKStringConverter"; 
    org.evosuite.runtime.GuiSupport.initialize(); 
    org.evosuite.runtime.RuntimeSettings.maxNumberOfThreads = 100; 
    org.evosuite.runtime.RuntimeSettings.maxNumberOfIterationsPerLoop = 10000; 
    org.evosuite.runtime.RuntimeSettings.mockSystemIn = true; 
    org.evosuite.runtime.RuntimeSettings.sandboxMode = org.evosuite.runtime.sandbox.Sandbox.SandboxMode.RECOMMENDED; 
    org.evosuite.runtime.sandbox.Sandbox.initializeSecurityManagerForSUT(); 
    org.evosuite.runtime.classhandling.JDKClassResetter.init();
    setSystemProperties();
    initializeClasses();
    org.evosuite.runtime.Runtime.getInstance().resetRuntime(); 
  } 

  @AfterClass
  public static void clearEvoSuiteFramework(){ 
    Sandbox.resetDefaultSecurityManager(); 
    java.lang.System.setProperties((java.util.Properties) defaultProperties.clone()); 
  } 

  @Before
  public void initTestCase(){ 
    threadStopper.storeCurrentThreads();
    threadStopper.startRecordingTime();
    org.evosuite.runtime.jvm.ShutdownHookHandler.getInstance().initHandler(); 
    org.evosuite.runtime.sandbox.Sandbox.goingToExecuteSUTCode(); 
    setSystemProperties(); 
    org.evosuite.runtime.GuiSupport.setHeadless(); 
    org.evosuite.runtime.Runtime.getInstance().resetRuntime(); 
    org.evosuite.runtime.agent.InstrumentingAgent.activate(); 
  } 

  @After
  public void doneWithTestCase(){ 
    threadStopper.killAndJoinClientThreads();
    org.evosuite.runtime.jvm.ShutdownHookHandler.getInstance().safeExecuteAddedHooks(); 
    org.evosuite.runtime.classhandling.JDKClassResetter.reset(); 
    resetClasses(); 
    org.evosuite.runtime.sandbox.Sandbox.doneWithExecutingSUTCode(); 
    org.evosuite.runtime.agent.InstrumentingAgent.deactivate(); 
    org.evosuite.runtime.GuiSupport.restoreHeadlessMode(); 
  } 

  public static void setSystemProperties() {
 
    java.lang.System.setProperties((java.util.Properties) defaultProperties.clone()); 
    java.lang.System.setProperty("user.dir", "/home/ali/Documents/AlphaTrans/java_projects/cleaned_final_projects/joda-convert"); 
    java.lang.System.setProperty("java.io.tmpdir", "/tmp"); 
  }

  private static void initializeClasses() {
    org.evosuite.runtime.classhandling.ClassStateSupport.initializeClasses(JDKStringConverter_ESTest_scaffolding.class.getClassLoader() ,
      "org.joda.convert.TypeStringConverterFactory",
      "org.joda.convert.JDKStringConverter$31",
      "org.joda.convert.JDKStringConverter$30",
      "org.joda.convert.JDKStringConverter",
      "org.joda.convert.JDKStringConverter$28",
      "org.joda.convert.StringConverter",
      "org.joda.convert.JDKStringConverter$9",
      "org.joda.convert.JDKStringConverter$27",
      "org.joda.convert.JDKStringConverter$26",
      "org.joda.convert.JDKStringConverter$25",
      "org.joda.convert.JDKStringConverter$24",
      "org.joda.convert.StringConverterFactory",
      "org.joda.convert.JDKStringConverter$23",
      "org.joda.convert.JDKStringConverter$22",
      "org.joda.convert.JDKStringConverter$21",
      "org.joda.convert.JDKStringConverter$20",
      "org.joda.convert.JDKStringConverter$2",
      "org.joda.convert.OptionalLongStringConverter",
      "org.joda.convert.JDKStringConverter$1",
      "org.joda.convert.JDKStringConverter$4",
      "org.joda.convert.ReflectionStringConverter",
      "org.joda.convert.JDKStringConverter$3",
      "org.joda.convert.JDKStringConverter$6",
      "org.joda.convert.JDKStringConverter$5",
      "org.joda.convert.JDKStringConverter$8",
      "org.joda.convert.AnnotationStringConverterFactory",
      "org.joda.convert.JDKStringConverter$7",
      "org.joda.convert.JDKStringConverter$29",
      "org.joda.convert.JDKStringConverter$17",
      "org.joda.convert.JDKStringConverter$16",
      "org.joda.convert.StringConvert$1",
      "org.joda.convert.JDKStringConverter$15",
      "org.joda.convert.JDKStringConverter$14",
      "org.joda.convert.JDKStringConverter$13",
      "org.joda.convert.JDKStringConverter$12",
      "org.joda.convert.JDKStringConverter$11",
      "org.joda.convert.FromStringConverter",
      "org.joda.convert.JDKStringConverter$10",
      "org.joda.convert.StringConvert",
      "org.joda.convert.TypedFromStringConverter",
      "org.joda.convert.RenameHandler",
      "org.joda.convert.OptionalDoubleStringConverter",
      "org.joda.convert.EnumStringConverterFactory",
      "org.joda.convert.TypedStringConverter",
      "org.joda.convert.ToStringConverter",
      "org.joda.convert.JDKStringConverter$19",
      "org.joda.convert.JDKStringConverter$18",
      "org.joda.convert.OptionalIntStringConverter",
      "org.joda.convert.MethodFromStringConverter"
    );
  } 

  private static void resetClasses() {
    org.evosuite.runtime.classhandling.ClassResetter.getInstance().setClassLoader(JDKStringConverter_ESTest_scaffolding.class.getClassLoader()); 

    org.evosuite.runtime.classhandling.ClassStateSupport.resetClasses(
      "org.joda.convert.JDKStringConverter",
      "org.joda.convert.StringConvert$1",
      "org.joda.convert.OptionalIntStringConverter",
      "org.joda.convert.OptionalLongStringConverter",
      "org.joda.convert.OptionalDoubleStringConverter",
      "org.joda.convert.MethodFromStringConverter",
      "org.joda.convert.ReflectionStringConverter",
      "org.joda.convert.AnnotationStringConverterFactory",
      "org.joda.convert.EnumStringConverterFactory",
      "org.joda.convert.TypeStringConverterFactory",
      "org.joda.convert.StringConvert",
      "org.joda.convert.RenameHandler"
    );
  }
}
