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
package org.apache.commons.fileupload;

import java.io.File;

import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

/**
 * Provides a shared GraalVM engine and a method to get Python classes.
 */
public abstract class ContextInitializer {
    /**
     * The shared GraalVM engine.
     */
    private static Engine sharedEngine;

    /**
     * Directory containing the Python source code.
     * TODO: change to actual directory
     */
    private static String codeDirectory = "../commons-fileupload-translated/src/main/python";

    /**
     * Directory containing the Python package.
     * TODO: change to actual directory
     */
    private static String packageDirectory = "../commons-fileupload-translated/src/";

    /** Polyglot context for evaluating Python */
    private static Context context;

    static {
        try {
            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        } catch (Exception e) {
            System.out.println("[-] " + e);
        }
    }

    public static Value[] getPythonClasses(String fileName, String... classNames) {
        try {
            File file = new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }
            return result;
        } catch (Exception e) {
            System.out.println("[-] " + e);
            return null; // ??
        }
    }

    public static Value getPythonClass(String fileName, String className) {
        return getPythonClasses(fileName, className)[0];
    }
}
