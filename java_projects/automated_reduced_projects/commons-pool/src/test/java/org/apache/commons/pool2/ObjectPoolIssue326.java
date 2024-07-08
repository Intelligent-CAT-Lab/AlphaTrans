/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.pool2;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

import org.apache.commons.pool2.impl.BaseObjectPoolConfig;
import org.apache.commons.pool2.impl.GenericKeyedObjectPoolConfig;

/**
 * On my box with 4 cores this test fails at between 5s and 900s with an average
 * of 240s (data from 10 runs of test).
 *
 * It is hard to turn this in a unit test because it can affect the build
 * negatively since you need to run it for a while.
 */
public final class ObjectPoolIssue326 {

    private class TestObject {
    }
}

/*
 *
 * Example stack trace: java.util.concurrent.ExecutionException:
 * java.lang.NullPointerException at
 * java.util.concurrent.FutureTask.report(FutureTask.java:122) at
 * java.util.concurrent.FutureTask.get(FutureTask.java:192) at
 * threading_pool.ObjectPoolIssue.run(ObjectPoolIssue.java:63) at
 * threading_pool.ObjectPoolIssue.main(ObjectPoolIssue.java:23) at
 * sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at
 * sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
 * at
 * sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.
 * java:43) at java.lang.reflect.Method.invoke(Method.java:498) at
 * com.intellij.rt.execution.application.AppMain.main(AppMain.java:147) Caused
 * by: java.lang.NullPointerException at
 * org.apache.commons.pool2.impl.GenericKeyedObjectPool.returnObject(
 * GenericKeyedObjectPool.java:474) at
 * threading_pool.ObjectPoolIssue$Task.call(ObjectPoolIssue.java:112) at
 * java.util.concurrent.FutureTask.run(FutureTask.java:266) at
 * java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:
 * 1142) at
 * java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:
 * 617) at java.lang.Thread.run(Thread.java:745)
 *
 */
