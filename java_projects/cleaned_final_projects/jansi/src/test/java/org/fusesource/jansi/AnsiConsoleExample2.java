/*
 * Copyright (C) 2009-2023 the original author(s).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fusesource.jansi;

import java.io.FileInputStream;
import java.io.IOException;

import static org.fusesource.jansi.Ansi.*;

/**
 *
 */
public class AnsiConsoleExample2 {

    private AnsiConsoleExample2() {}

    public static void main(String[] args) throws IOException {
        String file = "src/test/resources/jansi.ans";
        if (args.length > 0) file = args[0];

        // Allows us to disable ANSI processing.
        if ("true".equals(System.getProperty("jansi", "true"))) {
            AnsiConsole.systemInstall();
        }

        System.out.print(ansi0().reset().eraseScreen0().cursor(1, 1));
        System.out.print("=======================================================================");
        FileInputStream f = new FileInputStream(file);
        int c;
        while ((c = f.read()) >= 0) {
            System.out.write(c);
        }
        f.close();
        System.out.println("=======================================================================");
    }
}
